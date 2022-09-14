from ._anvil_designer import ProductDetailPanelTemplate
from ..ProductMenuItem import ProductMenuItem
from ..SubscriptionDetailPanel import SubscriptionDetailPanel
from ..SubscriptionList import SubscriptionList
from ...scripts.client import list_product_subscriptions
from ...scripts.view import (
    add_class,
    set_com_height_to_window_end,
)


class ProductDetailPanel(ProductDetailPanelTemplate):

    def populate_left_menu(self):
        for p in self.product_list:
            product_menu = ProductMenuItem()
            product_menu.product = p
            self.product_menu_map[p['id']] = product_menu
            product_menu.add_event_handler(
              'show_detail',
              self.select_product,
            )
            self.left_menu.add_component(product_menu)

    def select_product_menu(self):
        for product_id, product_menu in self.product_menu_map.items():
            if product_id == self.selected_product['id']:
                product_menu.role = 'menu-item-selected'
            else:
                product_menu.role = None

    def list_product_subscriptions(self):
        subscriptions = list_product_subscriptions(self.selected_product['id'])
        if subscriptions:
            self.product_subscrption_map[
                self.selected_product['id']] = subscriptions

        return subscriptions

    def is_multi_subscription(self):
        return len(self.product_subscrption_map[self.selected_product['id']]) > 1

    def select_product(self, product, **event_args):
        self.selected_product = product

        self.product_list_menu.select_product_menu(product)

        if self.selected_product['id'] in self.product_subscrption_map.keys():
            subscriptions = self.product_subscrption_map[self.selected_product['id']]
        else:
            subscriptions = self.list_product_subscriptions()

        if subscriptions:
            self.ccp_container.clear()
            if len(subscriptions) == 1:
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
                self.ccp_container.add_component(
                    SubscriptionList(self, subscriptions),
                    full_width_row=True,
                )

        self.product_details.item = product
        self.subscription_short.product_id = product['id']
        self.subscription_short.subscription = self.selected_subscription

    def __init__(self, page, product, product_list, **properties):
        self.selected_product = product
        self.selected_subscription = None
        self.product_subscrption_map = {}
        self.product_list = product_list
        self.page = page

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.select_product(product)

        add_class(self.ccp_container, 'fix-height')

    def show_subscription_detail(self, subscription):
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

        self.product_details.item = self.selected_product
        self.subscription_short.product_id = self.selected_product['id']
        self.subscription_short.subscription = subscription
