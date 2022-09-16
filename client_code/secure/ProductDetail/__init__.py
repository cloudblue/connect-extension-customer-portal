from ._anvil_designer import ProductDetailTemplate


class ProductDetail(ProductDetailTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.item = properties.get('product') or {}
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    @property
    def product(self):
        return self.item

    @product.setter
    def product(self, value):
        self.item = value

    def product_icon_mouse_up(self, x, y, button, **event_args):
        self.raise_event('show_details', product=self.item)
