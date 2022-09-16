from ._anvil_designer import ProductMenuItemTemplate


class ProductMenuItem(ProductMenuItemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.item = properties.get('product') or {}
        self.init_components(**properties)

    @property
    def product(self):
        return self.item

    @product.setter
    def product(self, value):
        self.item = value

    def lnk_product_menu_click(self, **event_args):
        self.raise_event('show_detail', product=self.item)
