from ._anvil_designer import ItemListTemplate

class ItemList(ItemListTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.subscription_items = properties.get('subscription_items')

        self.init_components(**properties)
    
    @property
    def subscription_items(self):
        return self._subscription_items
    
    @subscription_items.setter
    def subscription_items(self, value):
        self.item_repeating_panel.items = value
        self._subscription_items = value
    
    @property
    def header(self):
        return self._header
    
    @header.setter
    def header(self, value):
        self._header = value
    
    
