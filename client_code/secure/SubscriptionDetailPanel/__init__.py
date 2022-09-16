from ._anvil_designer import SubscriptionDetailPanelTemplate
from ..StatusProgressBar import status_map
from ..SubscriptionTemplate import SubscriptionTemplate
from ...scripts.client import get_product_actions, get_action_link

from anvil.js import window


class SubscriptionDetailPanel(SubscriptionDetailPanelTemplate):

    def populate_actions(self, product):
        if 'actions' not in product.keys():
            product['actions'] = get_product_actions(product['id'])
        self.actions = product['actions']

    def populate_links(self, product):
        ui_config = product.get('customer_ui_settings')
        self.download_links = []
        self.document_links = []

        if ui_config:

            if ui_config.get('download_links'):
                self.download_links = ui_config.get('download_links')

            if ui_config.get('documents'):
                self.document_links = ui_config.get('documents')

    def populate_option_panel(self, subscription):
        subscription_status = subscription['status']
        deactivate = subscription_status in status_map.keys()
        self.active_subscription_options.visible = not deactivate
        self.status_progress_bar.visible = deactivate

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
        self.active_subscription_options.visible = False
        self.status_progress_bar.visible = False

        self.populate_links(product)
        self.populate_actions(product)

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.populate_option_panel(subscription)
        self.populate_template(subscription)

    def halted_subscription_template_back_button_click(self, **event_args):
        self.page.select_product(self.product)

    def active_subscription_options_action_click(
            self,
            action_id,
            product_id,
            subscription_id,
            **event_args,
    ):
        link = get_action_link(
            product_id,
            subscription_id,
            action_id,
        )

        if link:
            window.open(link, '_blank')
