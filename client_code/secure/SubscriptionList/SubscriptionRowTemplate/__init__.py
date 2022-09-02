from ._anvil_designer import SubscriptionRowTemplateTemplate
from ....scripts.view import change_status_background_color


class SubscriptionRowTemplate(SubscriptionRowTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        change_status_background_color(
            self.subscription_status,
            self.item['status'],
        )

    def view_details_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.parent.page.show_subscription_detail(self.item)
