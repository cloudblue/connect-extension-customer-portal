from ._anvil_designer import ActiveSubscriptionOptionsTemplate
from ...scripts.client import get_product_actions
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
)


class ActiveSubscriptionOptions(ActiveSubscriptionOptionsTemplate):

    def populate_actions(self, product):
        if 'actions' not in product.keys():
            product['actions'] = get_product_actions(product['id'])
        self.action_repeating_panel.items = product['actions']

    def populate_links(self, product):
        ui_config = product.get('customer_ui_settings')

        if ui_config:
            download_links = ui_config.get('download_links')

            if download_links:
                self.document_link_repeating_panel.visible = True
                self.download_link_repeating_panel.items = download_links
            else:
                self.document_link_repeating_panel.visible = False

            document_links = ui_config.get('documents')

            if document_links:
                self.document_link_repeating_panel.visible = True
                self.document_link_repeating_panel.items = document_links
            else:
                self.document_link_repeating_panel.visible = False

    def __init__(self, product, subscrpiton, **properties):
        self.product = product
        self.subscription = subscrpiton

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.action_repeating_panel.product_id = product['id']
        self.action_repeating_panel.subscription_id = subscrpiton['id']

        self.populate_actions(product)
        self.populate_links(product)

    def form_show(self, **event_args):
        add_class(self, 'fix-height')
        fix_height_to_window_end('fix-height')
