from ._anvil_designer import StatusProgressBarTemplate
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
)

status_map = {
    'processing': [
        {'description': 'Subscription Created', 'status': 'complete'},
        {'description': 'Processing', 'status': 'complete'},
        {'description': 'Pending', 'status': 'in_progress'},
        {'description': 'Active', 'status': 'pending'},
    ],
    'inquiring': [
        {'description': 'Subscription Created', 'status': 'complete'},
        {'description': 'Inquiring', 'status': 'in_progress'},
        {'description': 'Processing', 'status': 'pending'},
        {'description': 'Active', 'status': 'pending'},
    ],
    'terminated': [
        {'description': 'Subscription Created', 'status': 'complete'},
        {'description': 'Processing', 'status': 'complete'},
        {'description': 'Active', 'status': 'complete'},
        {'description': 'Terminating', 'status': 'complete'},
        {'description': 'Terminated', 'status': 'complete'},
    ],
    'suspended': [
        {'description': 'Subscription Created', 'status': 'complete'},
        {'description': 'Processing', 'status': 'complete'},
        {'description': 'Active', 'status': 'complete'},
        {'description': 'Suspended', 'status': 'in_progress'},
    ],
}


class StatusProgressBar(StatusProgressBarTemplate):
    def update_bar(self, status):
        progress_bar_list = status_map.get(status)

        if progress_bar_list:
            self.status_repeating_panel.items = progress_bar_list

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.item = properties.get('subscription_status')
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.update_bar(self.item)

    @property
    def subscription_status(self):
        return self.item

    @subscription_status.setter
    def subscription_status(self, value):
        self.item = value
        self.update_bar(self.item)

    def form_show(self, **event_args):
        add_class(self, 'fix-height')
        fix_height_to_window_end('fix-height')
