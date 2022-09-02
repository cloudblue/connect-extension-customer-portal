from ._anvil_designer import HaltedSubscriptionTemplateTemplate
from ...scripts.view import (
    add_class,
    fix_height_to_window_end,
)

description_map = {
    'terminated': 'Sorry, this service has been terminated. Go to your account to manage your subscriptions.',
    'suspended': 'Sorry, this service is unavailable at the moment.',
}


class HaltedSubscriptionTemplate(HaltedSubscriptionTemplateTemplate):

    def __init__(self, page, product, subscription, multi_subscription, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.subscription = subscription
        self.product = product
        self.page = page
        self.multi_subscription = multi_subscription

        status = subscription['status']
        self.template_header.text = f'Subscription {status}'
        self.template_description.text = description_map[status]

        if not multi_subscription:
            self.back_button.visible = False

    def form_show(self, **event_args):
        add_class(self, 'fix-height')
        fix_height_to_window_end('fix-height')

    def back_button_click(self, **event_args):
        if self.multi_subscription:
            self.page.select_product(self.product)
