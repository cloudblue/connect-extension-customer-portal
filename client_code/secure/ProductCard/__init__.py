from ._anvil_designer import ProductCardTemplate
from ...scripts.client import get_connect_base_url


class ProductCard(ProductCardTemplate):

    def cut_short(self, value, size):
        return (value[0:(size - 3)] + '...') if len(value) > size else value

    def prepare(self, portal_url, product):
        product['vendor'] = f"by {product['owner']['name']}"
        if not product['icon'].startswith('http'):
            product['icon'] = f"{portal_url}{product['icon']}"
    
        product['minimize_short_description'] = self.cut_short(
            product['short_description'],
            135,
        )
    
        product['minimize_name'] = self.cut_short(product['name'], 25)
    
        return product
  
    def __init__(self, **properties):
        self.portal_url = get_connect_base_url()
        self.init_components(**properties)

        self.product = properties.get('product')
    
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self.prepare(self.portal_url, value)
        self._product = value

    def lnk_view_more_click(self, **event_args):
        self.raise_event(
          'show_detail',
          product=self.product,
        )
