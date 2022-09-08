from ._anvil_designer import SubscriptionDetailPanelTemplate
from ..ActiveSubscriptionOptions import ActiveSubscriptionOptions
from ..Status import Status, status_map
from ..SubscriptionTemplate import SubscriptionTemplate


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

    def populate_template(self, subscription):
        if subscription['status'] in ['suspended', 'terminated']:
            self.halted_subscription_template.visible = True
        else:
            self.halted_subscription_template.visible = False
            self.control_panel.add_component(
                SubscriptionTemplate(self.subscription),
                full_width_row=True,
            )

    def __init__(self, page, product, subscription, multi_subscription, **properties):
        self.product = product
        self.subscription = subscription
        self.multi_subscription = multi_subscription
        self.page = page
        self.halted_subscription_template.visible = False

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.populate_option_panel(product, subscription)
        self.populate_template(subscription)

    def halted_subscription_template_back_button_click(self, **event_args):
        self.page.select_product(self.product)
