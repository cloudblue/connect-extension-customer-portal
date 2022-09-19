from ._anvil_designer import SubscriptionTemplateTemplate
from ..ItemList import ItemList
from ...scripts.client import get_activation_template, is_debug
from ...scripts.utils import normalized_object
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
    make_target_new_tab,
)


class SubscriptionTemplate(SubscriptionTemplateTemplate):
        
    def __init__(self, subscripiton, **properties):
        self.subscription_properties.visible = False
        if 'template' not in subscripiton.keys():
            subscripiton['template'] = get_activation_template(subscripiton['id'])

        self.item = subscripiton
        
        if is_debug():
            self.subscription_properties.visible = True
        
        if subscripiton['status'] in ['active', 'terminating']:
            self.items_panel.visible = True
        
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        
        make_target_new_tab(self.content)

    def form_show(self, **event_args):
        add_class(self, 'fix-height')
        fix_height_to_window_end('fix-height')
