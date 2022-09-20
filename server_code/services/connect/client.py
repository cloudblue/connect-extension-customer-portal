from anvil import secrets

from connect.client import ConnectClient as Client, R


class ConnectClient:
    def __init__(self):
        self.client = Client(
            api_key=secrets.get_secret('CONNECT_TOKEN'),
            endpoint=secrets.get_secret('CONNECT_API_URL'),
            use_specs=False,
        )
    
    def list_tier_accounts(self, email):
        return self.client('tier').accounts.filter(
            R().contact_info.contact.email.eq(email),
        )
    
    def get_account(self, account_id):
        return self.client('tier').accounts[account_id].get()

    def get_assets_for_customers(self, customer_list):
        return self.client.assets.filter(
            f"in(tiers.customer.id,({','.join(customer_list)}))",
            f'ne(status,draft)',
        ).select(
            '-params',
            '-tiers',
            '-configuration',
            #'+pending_request',
        )

    def get_product_list(self, product_id_list):
        return self.client.products.filter(
            f"in(id,({','.join(product_id_list)}))",
        ).order_by('name')

    def get_product_subscription_actions(self, product_id):
        return self.client.products[product_id].actions.filter(
            R().type.eq('button'),
            R().scope.eq('asset'),
        )

    def get_action_link(self, product_id, asset_id, action_id):
        action_link = self.client.products[product_id].actions[action_id](
            'actionLink',
        ).get(params={'asset_id': asset_id})

        return action_link['link'] if action_link else None

    def get_subscription_template(self, asset_id):
        return self.client.assets[asset_id]('render').get()
    
    def get_last_transition_asset_request(self, asset_id):
        return self.client.requests.filter(
            R().asset.id.eq(asset_id),
            status__in=('approved', 'inquiring', 'pending', 'tiers_setup'),
        ).select(
            '-asset.items',
            '-asset.params',
            '-asset.tiers',
            '-asset.configuration',
        ).order_by('-created').limit(1).first()
