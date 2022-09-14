from ._anvil_designer import SubscriptionShortTemplate
from ...scripts.view import change_status_background_color

class SubscriptionShort(SubscriptionShortTemplate):
  def subscription_options(self, show):
        self.subscription_id_label.visible = show
        self.subscription_id_value.visible = show
        self.subscription_status.visible = show
  
  def set_subscription_values(self, subscription):
      self.item['subscription'] = subscription
      self.item['subscription_id'] = f"{subscription.get('id')} ({subscription.get('external_id')})"
      self.item['subscription_status'] = subscription.get('status')
      change_status_background_color(
        self.subscription_status,
        self.item['subscription_status'],
      )
      if subscription:
          self.subscription_options(True)
      else:
          self.subscription_options(False)

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    subscription = properties.get('subscription') or {}
    self.set_subscription_values(subscription)
    
    self.item['align'] = properties.get('align')
    self.item['product_id'] = properties.get('product_id')
    
    self.init_components(**properties)
  
  @property
  def product_id(self):
      return self.item['product_id']
  
  @product_id.setter
  def product_id(self, value):
      self.item['product_id'] = value
      self.refresh_data_bindings()
  
  @property
  def subscription(self):
      return self.item['subscription']
  
  @subscription.setter
  def subscription(self, value):
      subscription = value or {}
      self.set_subscription_values(subscription)
      self.refresh_data_bindings()
      
  
  @property
  def align(self):
      return self.item['align']
  
  @subscription.setter
  def align(self, value):
      self.item['align'] = value
      self.refresh_data_bindings()
  