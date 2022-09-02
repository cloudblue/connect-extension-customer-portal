from ._anvil_designer import ProductShortTemplate
from ...scripts.view import change_status_background_color


class ProductShort(ProductShortTemplate):
    def subscription_options(self, show):
        self.subscription_id_label.visible = show
        self.subscription_id_value.visible = show
        self.subscription_status.visible = show

    def process_subscription(self, subscription, product):
        self.subscription = subscription
        if subscription:
            external_id = f"({self.subscription['external_id']})" if 'external_id' in self.subscription else ''
            product['subscription_id'] = f"{self.subscription['id']} {external_id}"
            product['subscription'] = self.subscription
            self.subscription_options(True)
            change_status_background_color(
                self.subscription_status,
                self.subscription['status']
            )
        else:
            self.subscription_options(False)

    def __init__(self, page, product, subscription, multi_subscription=False, **properties):
        # Set Form properties and Data Bindings.
        self.page = page
        self.product = product
        self.multi_subscription = multi_subscription
        self.item = product

        self.process_subscription(subscription, product)

        self.init_components(**properties)

    def product_icon_mouse_up(self, x, y, button, **event_args):
        """This method is called when a mouse button is released on this component"""
        if self.subscription and self.multi_subscription:
            self.page.select_product(self.product)
