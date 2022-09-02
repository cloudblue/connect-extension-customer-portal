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
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        if 'template' not in subscripiton.keys():
            subscripiton['template'] = get_activation_template(subscripiton['id'])

        self.item = subscripiton
        
        if subscripiton['status'] in ['active', 'terminating']:
            self.items_panel.add_component(
                ItemList(subscripiton['items']),
                full_width_row=True,
            )
        make_target_new_tab(self.content)
        
        if is_debug():
            self.sub_property_repeating_panel.items = normalized_object(subscripiton)
            self.subscription_properties_label.visible = True
            self.subscription_data_grid.visible = True

    def form_show(self, **event_args):
        add_class(self, 'fix-height')
        fix_height_to_window_end('fix-height')
