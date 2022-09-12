from anvil import (
    email,
    http,
    secrets,
    server,
    tables,
    users,
)
from anvil.tables import app_tables, in_transaction

from datetime import datetime, timedelta
import math
import random

from .connect.client import ConnectClient
from .recaptcha import ensure_recaptcha
from .subscription import cache_subscription_data
from .utils import handle_response


def generate_token():
    digits = "0123456789"
    otp = ""
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]

    return otp


def clean_tokens(user):
    tokens = app_tables.auth_tokens.search(user=user)
    for token in tokens:
        token.delete()


def generate_and_send_token(user):
    token = generate_token()
    app_tables.auth_tokens.add_row(
        token=token,
        user=user,
        valid_till=datetime.now() + timedelta(minutes=int(secrets.get_secret('AUTH_TOKEN_VALIDITY'))),
    )

    email.send(
        from_name='Sample Application',
        to=user['email'],
        subject='Sample Application Login OTP',
        text=f'Your login OPT is {token}',
    )

    
def find_and_store_user(email):
    connect_client = ConnectClient()
    accounts = list(connect_client.list_tier_accounts(email))
    if accounts:
        user = app_tables.users.add_row(email=email, enabled=True)
        for account in accounts:
            app_tables.accounts.add_row(user=user, tier_id=account['id'])
        return user
    else:
        return None


def update_accounts(user):
    connect_client = ConnectClient()
    accounts = list(connect_client.list_tier_accounts(user['email']))
    if accounts:
        for account in accounts:
            db_account = app_tables.accounts.get(user=user, tier_id=account['id'])
            if not db_account:
                app_tables.accounts.add_row(user=user, tier_id=account['id'])


@server.callable
@in_transaction
@handle_response
@ensure_recaptcha
def initiate_auth(email, recaptcha_token):
    user = app_tables.users.get(email=email, enabled=True)
      
    if not user:
        user = find_and_store_user(email)
    else:
        update_accounts(user)

    if user:
        clean_tokens(user)
        generate_and_send_token(user)
  
    return True


@server.callable
@in_transaction
@handle_response
@ensure_recaptcha
def validate_token(email, token, recaptcha_token):
    user = app_tables.users.get(email=email, enabled=True)
    if user:
        token = app_tables.auth_tokens.get(user=user, token=token)
        if token and token['valid_till'].replace(tzinfo=None) > datetime.now():
            users.force_login(user)
            token.delete()
            cache_subscription_data()
            return True
        elif token:
            token.delete()
        
        raise Exception('OTP is not correct!')
