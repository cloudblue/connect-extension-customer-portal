from ._anvil_designer import ItemListTemplate
class ItemList(ItemListTemplate):
    def __init__(self, items, **properties):
        # Set Form properties and Data Bindings.
        self.items = items

        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.item_repeating_panel.items = items
