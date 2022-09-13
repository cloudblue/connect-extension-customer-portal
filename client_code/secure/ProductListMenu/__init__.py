from ._anvil_designer import ProductListMenuTemplate
from ..ProductMenuItem import ProductMenuItem


class ProductListMenu(ProductListMenuTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.product_menu_map = {}
        self.item = properties.get('products')
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    @property
    def products(self):
        return self.item

    @products.setter
    def products(self, value):
        self.item = value

    def produce_show_details_event(self, product, **event_params):
        self.raise_event('show_details', product=product)

    def form_refreshing_data_bindings(self, **event_args):
        self.clear()
        if self.item:
            for product in self.item:
                menu_item = ProductMenuItem()
                menu_item.item = product
                menu_item.add_event_handler(
                    'show_detail',
                    self.produce_show_details_event,
                )
                self.add_component(menu_item)
                self.product_menu_map[product['id']] = menu_item

    def select_product_menu(self, product):
        for product_id, menu_item in self.product_menu_map.items():
            if product_id == product['id']:
                menu_item.role = 'menu-item-selected'
            else:
                menu_item.role = None
