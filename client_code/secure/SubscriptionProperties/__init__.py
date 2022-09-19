from ._anvil_designer import SubscriptionPropertiesTemplate
from ...scripts.utils import normalized_object


class SubscriptionProperties(SubscriptionPropertiesTemplate):
  def __init__(self, **properties):
    self.subscription = properties.get('subscription') or {}
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  @property
  def subscription(self):
      return self._subscription
  
  @subscription.setter
  def subscription(self, value):
      self._subscription = value
      self.sub_property_repeating_panel.items = normalized_object(value)
  