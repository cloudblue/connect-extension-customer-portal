from ._anvil_designer import SubscriptionRowTemplate
from ....scripts.view import change_status_background_color


class SubscriptionRow(SubscriptionRowTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        change_status_background_color(
            self.subscription_status,
            self.item['status'],
        )

    def view_details_click(self, **event_args):
          if self.parent:
              self.parent.raise_event(
                  'x-show_subscription_detail',
                  subscription=self.item,
              )
          else:
              self.raise_event(
                  'show_subscription_detail',
                  subscription=self.item,
              )
