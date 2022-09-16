from ._anvil_designer import SubscriptionListTemplate


class SubscriptionList(SubscriptionListTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.subscription_repeating_panel.items = properties.get('subscriptions')
        self.subscription_repeating_panel.add_event_handler(
            'x-show_subscription_detail',
            self.raise_show_subscription_detail_event,
        )

        self.init_components(**properties)

    @property
    def subscriptions(self):
        return self.subscription_repeating_panel.items

    @subscriptions.setter
    def subscriptions(self, value):
        self.subscription_repeating_panel.items = value
        self.refresh_data_bindings()

    def raise_show_subscription_detail_event(self, subscription, **event_args):
        self.raise_event(
            'show_subscription_detail',
            subscription=subscription,
        )
