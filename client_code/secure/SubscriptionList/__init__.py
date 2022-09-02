from ._anvil_designer import SubscriptionListTemplate


class SubscriptionList(SubscriptionListTemplate):
    def __init__(self, page, subscriptions, **properties):
        # Set Form properties and Data Bindings.
        self.subscriptions = subscriptions
        self.page = page

        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.subscription_repeating_panel.page = page
        self.subscription_repeating_panel.items = subscriptions
