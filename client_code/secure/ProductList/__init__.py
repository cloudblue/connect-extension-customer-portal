from ._anvil_designer import ProductListTemplate
from ..ProductCard import ProductCard
from ...scripts.client import get_connect_base_url, list_products


def cut_short(value, size):
    return (value[0:(size - 3)] + '...') if len(value) > size else value


def prepare(portal_url, product):
    product['vendor'] = f"by {product['owner']['name']}"
    product['icon'] = f"{portal_url}{product['icon']}"

    product['minimize_short_description'] = cut_short(
        product['short_description'],
        135,
    )

    product['minimize_name'] = cut_short(product['name'], 25)

    return product


class ProductList(ProductListTemplate):
    def __init__(self, page, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.page = page
        self.portal_url = get_connect_base_url()

        products = list_products()
        if products:
            for product in products:
                product_card = ProductCard(page, product, products)
                product_card.item = prepare(self.portal_url, product)
                self.product_list_flow_panel.add_component(product_card)
