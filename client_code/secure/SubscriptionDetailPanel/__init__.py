from ._anvil_designer import SubscriptionDetailPanelTemplate
from ..ActiveSubscriptionOptions import ActiveSubscriptionOptions
from ..HaltedSubscriptionTemplate import HaltedSubscriptionTemplate
from ..Status import Status, status_map
from ..SubscriptionTemplate import SubscriptionTemplate
from ...scripts.view import (
    set_com_height_to_window_end,
)


def fix_height(component):
    def handler(**event_args):
        set_com_height_to_window_end(component)

    return handler


class SubscriptionDetailPanel(SubscriptionDetailPanelTemplate):

    def populate_option_panel(self, product, subscription):
        self.subscription_option_panel.clear()

        subscription_status = subscription['status']
        if subscription_status in status_map.keys():
            self.subscription_option_panel.add_component(
                Status(subscription_status),
                full_width_row=True,
            )
        else:
            self.subscription_option_panel.add_component(
                ActiveSubscriptionOptions(product, subscription),
                full_width_row=True,
            )

    def populate_template(self, page, subscription, multi_subscription):
        self.control_panel.clear()
        if subscription['status'] in ['suspended', 'terminated']:
            self.control_panel.add_component(
                HaltedSubscriptionTemplate(
                    page,
                    self.product,
                    self.subscription,
                    multi_subscription,
                ),
                full_width_row=True,
            )
        else:
            self.control_panel.add_component(
                SubscriptionTemplate(self.subscription),
                full_width_row=True,
            )

    def __init__(self, page, product, subscription, multi_subscription, **properties):
        self.product = product
        self.subscription = subscription

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.populate_option_panel(product, subscription)
        self.populate_template(page, subscription, multi_subscription)
