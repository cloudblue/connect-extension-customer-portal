import re

from ._anvil_designer import LoginTemplate
from ..LoginVerify import LoginVerify
from ..scripts.client import initiate_auth
from ..scripts.view import set_opacity
from ..scripts.recaptcha import enforce_recaptcha


from anvil import *


class Login(LoginTemplate):

  def validate_email(self, email):
      regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      
      return email and re.search(regex, email)
      
      
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @enforce_recaptcha
  def continue_button_click(self, recaptcha_token, **event_args):
      
      email = self.item['email'].strip()
      
      if self.validate_email(email):
          self.error_label.visible = False
          result = initiate_auth(email, recaptcha_token)
          if result:
              login_verify_form = LoginVerify(email)
              self.content_panel.clear()
              self.content_panel.add_component(login_verify_form)
      else:
          self.error_label.visible = True
      

  def email_txt_box_change(self, **event_args):
      self.continue_button.enabled = self.email_txt_box.text.strip()
      self.error_label.visible = not self.email_txt_box.text.strip()

  def form_show(self, **event_args):
    self.email_txt_box.focus()
    set_opacity('grecaptcha-badge', 100)

