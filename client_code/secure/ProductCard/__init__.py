from ._anvil_designer import ProductCardTemplate
from ..ProductDetailPanel import ProductDetailPanel


class ProductCard(ProductCardTemplate):
    def __init__(self, page, product, product_list, **properties):
        self.init_components(**properties)

        self.product = product
        self.product_list = product_list
        self.page = page

        self.item = product

    def lnk_view_more_click(self, **event_args):
        if not self.page.product_detail_panel:
            self.page.product_detail_panel = ProductDetailPanel(
                self.page,
                self.product,
                self.product_list,
            )
        else:
            self.page.product_detail_panel.select_product(self.product)
        
        self.page.clear()
        self.page.add_component(
            self.page.product_detail_panel,
            full_width_row=True,
        )
