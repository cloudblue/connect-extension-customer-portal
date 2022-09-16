from ._anvil_designer import ProductListTemplate
from ..ProductCard import ProductCard
from ..ProductDetailPanel import ProductDetailPanel
from ...scripts.client import list_products


class ProductList(ProductListTemplate):
    def show_product_details(self, product, **event_args):
        if not self.page.product_detail_panel:
            self.page.product_detail_panel = ProductDetailPanel(
                self.page,
                product,
                self.products,
            )
        else:
            self.page.product_detail_panel.select_product(product)

        self.page.clear()
        self.page.add_component(
            self.page.product_detail_panel,
            full_width_row=True,
        )

    def __init__(self, page, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.page = page

        self.products = list_products()
        if self.products:
            for product in self.products:
                product_card = ProductCard(product=product)
                product_card.add_event_handler(
                    'show_detail',
                    self.show_product_details,
                )
                self.product_list_flow_panel.add_component(product_card)
