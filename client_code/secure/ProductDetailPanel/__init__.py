from ._anvil_designer import ProductDetailPanelTemplate
from ..SubscriptionDetailPanel import SubscriptionDetailPanel
from ...scripts.client import list_product_subscriptions
from ...scripts.view import (
    fix_height_to_window_end,
    is_handheld,
)


class ProductDetailPanel(ProductDetailPanelTemplate):

    def list_product_subscriptions(self):
        subscriptions = list_product_subscriptions(self.selected_product['id'])
        if subscriptions:
            self.product_subscription_map[
                self.selected_product['id']] = subscriptions

        return subscriptions

    def is_multi_subscription(self):
        return len(self.product_subscription_map[self.selected_product['id']]) > 1

    def update_top_panel(self, product):
        self.product_details.item = product
        self.subscription_short.product_id = product['id']
        self.subscription_short.subscription = self.selected_subscription

        if is_handheld():
            self.subscription_short.align = 'left'

    def select_product(self, product, **event_args):
        self.selected_product = product

        self.product_list_menu.select_product_menu(product)

        if self.selected_product['id'] in self.product_subscription_map.keys():
            subscriptions = self.product_subscription_map[self.selected_product['id']]
        else:
            subscriptions = self.list_product_subscriptions()

        if subscriptions:
            self.ccp_container.clear()
            self.ccp_container.visible = True
            if len(subscriptions) == 1:
                self.subscription_list.visible = False
                self.selected_subscription = subscriptions[0]
                self.ccp_container.add_component(
                    SubscriptionDetailPanel(
                        self.page,
                        product,
                        self.selected_subscription,
                        False,
                    ),
                    full_width_row=True,
                )
            else:
                self.selected_subscription = None
                self.ccp_container.visible = False
                self.subscription_list.visible = True
                self.subscription_list.subscriptions = subscriptions

        self.update_top_panel(product)
        fix_height_to_window_end('fix-height')

    def __init__(self, page, product, product_list, **properties):
        self.selected_product = product
        self.selected_subscription = None
        self.product_subscription_map = {}
        self.product_list = product_list
        self.page = page
        self.subscription_list.visible = False
        self.ccp_container.visible = False

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.select_product(product)

    def show_subscription_detail(self, subscription, **event_args):
        self.subscription_list.visible = False
        self.ccp_container.visible = True
        self.selected_subscription = subscription

        self.ccp_container.clear()
        self.ccp_container.add_component(
            SubscriptionDetailPanel(
                self,
                self.selected_product,
                subscription,
                self.is_multi_subscription(),
            ),
            full_width_row=True,
        )

        self.update_top_panel(self.selected_product)
        fix_height_to_window_end('fix-height')
