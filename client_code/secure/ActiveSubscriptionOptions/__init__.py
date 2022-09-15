from ._anvil_designer import ActiveSubscriptionOptionsTemplate
from .ActionTemplate import ActionTemplate
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
)


class ActiveSubscriptionOptions(ActiveSubscriptionOptionsTemplate):

    def populate_download_links(self, download_links):

        if download_links:
            self.document_link_repeating_panel.visible = True
            self.download_link_repeating_panel.items = download_links
        else:
            self.document_link_repeating_panel.visible = False

    def populate_document_links(self, document_links):
        if document_links:
            self.document_link_repeating_panel.visible = True
            self.document_link_repeating_panel.items = document_links
        else:
            self.document_link_repeating_panel.visible = False
    
    def populate_action_buttons(self, actions):
        if actions:
            self.actions_column_panel.visible = True
            for action in actions:
                action_button = ActionTemplate()
                action_button.action = action
                action_button.product_id = self.product_id
                action_button.subscription_id = self.subscription_id
                action_button.add_event_handler(
                  'action_click',
                  self.action_link_click_event_handler,
                )
                self.actions_column_panel.add_component(action_button)

    def __init__(self, **properties):
        self.subscription_id = properties.get('subscription_id')
        self.product_id = properties.get('product_id')
        self.actions = properties.get('actions')
        self.download_links = properties.get('download_links')
        self.document_links = properties.get('document_links')
        self.extend_height_to_page_end = properties.get('extend_height_to_page_end')

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.populate_download_links(self._download_links)
        self.populate_document_links(self._document_links)
        self.populate_action_buttons(self._actions)
    
    @property
    def subscription_id(self):
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    
    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    
    @property
    def download_links(self):
        return self._download_links
    
    @download_links.setter
    def download_links(self, value):
        self._download_links = value
        self.populate_download_links(self._download_links)
    
    @property
    def document_links(self):
        return self._document_links
    
    @document_links.setter
    def document_links(self, value):
        self._document_links = value
        self.populate_document_links(self._document_links)
    
    @property
    def actions(self):
        return self._actions
    
    @actions.setter
    def actions(self, value):
        self._actions = value
        self.populate_action_buttons(self._actions)
    
    @property
    def extend_height_to_page_end(self):
        return self._extend_height
    
    @extend_height_to_page_end.setter
    def extend_height_to_page_end(self, value):
        self._extend_height = value

    def form_show(self, **event_args):
        if self._extend_height:
            add_class(self, 'fix-height')
            fix_height_to_window_end('fix-height')
    
    def action_link_click_event_handler(
      self,
      action_id,
      product_id,
      subscription_id,
      **event_args,
    ):
        self.raise_event(
            'action_click',
            action_id=action_id,
            product_id=product_id,
            subscription_id=subscription_id,
        )
