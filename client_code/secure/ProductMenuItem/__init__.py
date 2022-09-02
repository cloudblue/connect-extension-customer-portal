from ._anvil_designer import ProductMenuItemTemplate


class ProductMenuItem(ProductMenuItemTemplate):
    def __init__(self, page, product, **properties):
        # Set Form properties and Data Bindings.
        self.page = page
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.item = product

    def lnk_product_menu_click(self, **event_args):
        self.page.select_product(self.item)
