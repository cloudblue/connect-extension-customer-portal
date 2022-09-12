from anvil import server, users
from anvil.tables import app_tables

from .connect.client import ConnectClient
from .utils import handle_response


def invent_inquiring_status(subscription):
    if 'pending_request' in subscription and subscription[
      'pending_request']['status'] == 'inquiring':
        subscription['status'] = 'inquiring'
    
    return subscription


def cache_subscription_data():
    connect_client = ConnectClient()
    user = users.get_user()

    if user:
        server.session['subscriptions'] = []
        server.session['products'] = []

        accounts = app_tables.accounts.search(user=user)
        tier_ids = [account['tier_id'] for account in accounts]

        subscriptions = list(connect_client.get_assets_for_customers(tier_ids))
        server.session['subscriptions'] = [invent_inquiring_status(subscription) for subscription in subscriptions]

        if subscriptions:
            product_id_list = [subscription['product']['id'] for subscription in subscriptions]

            if product_id_list:
                products = connect_client.get_product_list(product_id_list)
                server.session['products'] = list(products)


@server.callable(require_user=True)
@handle_response
def list_products():
    products = server.session['products']

    if products:
        return products
    else:
        raise Exception('Unable to fetch your product list.')


@server.callable(require_user=True)
@handle_response
def list_product_actions(product_id):
    connect_client = ConnectClient()

    actions = list(connect_client.get_product_subscription_actions(product_id))

    if actions:
        return actions
    else:
        raise Exception('Unable to fetch your product actions.')


@server.callable(require_user=True)
@handle_response
def get_action_link(product_id, asset_id, action_id):
    connect_client = ConnectClient()

    link = connect_client.get_action_link(product_id, asset_id, action_id)

    if link:
        return link
    else:
        raise Exception('Unable to fetch action link for Product '
                        f'{product_id}, Subscription ID {asset_id} and Action {action_id}.')


@server.callable(require_user=True)
@handle_response
def list_product_subscriptions(product_id):
    subscriptions = list(
        filter(
            lambda subscription: subscription['product']['id'] == product_id,
            server.session['subscriptions'],
        ),
    )

    if subscriptions:
        return subscriptions
    else:
        raise Exception(f'Subscription is not available for the product {product_id}')


@server.callable(require_user=True)
@handle_response
def get_activation_template(subscription_id):
    connect_client = ConnectClient()
    activation_template = None
    #activation_template = connect_client.get_subscription_template(subscription_id) New Implementation
    
    last_approved_request = connect_client.get_last_transition_asset_request(subscription_id)

    if last_approved_request:
        if last_approved_request['status'] == 'inquiring':
            activation_template = last_approved_request.get('template').get('message')
        else:
            activation_template = last_approved_request.get('activation_key')

    if activation_template:
        return activation_template
    else:
        raise Exception('Subscription template is not available! Try again later.')
