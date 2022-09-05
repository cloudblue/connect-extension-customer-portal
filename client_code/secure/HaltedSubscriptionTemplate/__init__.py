from ._anvil_designer import HaltedSubscriptionTemplateTemplate
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
)


class HaltedSubscriptionTemplate(HaltedSubscriptionTemplateTemplate):

    def __init__(self, **properties, ):
        self._subscription_status = properties.get('subscription_status')
        self._show_back_button = properties.get('show_back_button')
        self._description_map = {
            'terminated': properties.get('terminated_msg'),
            'suspended': properties.get('suspended_msg'),
        }
        self._show_back_button = properties.get('show_back_button')
        self._extend_height = properties.get('extend_height_to_page_end')

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.update_template_description()
        self.back_button.visible = self._show_back_button

    def update_template_description(self):
        self.template_header.text = f'Subscription {self._subscription_status}'
        self.template_description.text = self._description_map.get(
            self._subscription_status)

    @property
    def subscription_status(self):
        return self._subscription_status

    @subscription_status.setter
    def subscription_status(self, value):
        self._subscription_status = value
        self.update_template_description()

    @property
    def show_back_button(self):
        return self._show_back_button

    @show_back_button.setter
    def show_back_button(self, value):
        self._show_back_button = value
        self.back_button.visible = self._show_back_button

    @property
    def terminated_msg(self):
        return self._terminated_msg

    @terminated_msg.setter
    def terminated_msg(self, value):
        self._description_map['terminated'] = value
        self.update_template_description()

    @property
    def suspended_msg(self):
        return self._suspended_msg

    @suspended_msg.setter
    def suspended_msg(self, value):
        self._description_map['suspended'] = value
        self.update_template_description()

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

    def back_button_click(self, **event_args):
        self.raise_event('back_button_click')
