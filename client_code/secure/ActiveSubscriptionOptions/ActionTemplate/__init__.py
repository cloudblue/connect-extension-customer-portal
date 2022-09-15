from ._anvil_designer import ActionTemplateTemplate


class ActionTemplate(ActionTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.item = properties.get('action') or {}
        self.product_id = properties.get('product_id')
        self.subscription_id = properties.get('subscription_id')
        
        self.init_components(**properties)
    
    @property
    def action(self):
        return self.item
    
    @action.setter
    def action(self, value):
        self.item = value
    
    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def product_id(self, value):
        self._product_id = value
        self.refresh_data_bindings()
    
    @property
    def subscription_id(self):
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
        self.refresh_data_bindings()

    def action_link_click(self, **event_args):
        self.raise_event(
            'action_click',
            action_id=self.item['id'],
            product_id=self.product_id,
            subscription_id=self.subscription_id,
        )
