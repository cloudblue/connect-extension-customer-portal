from ._anvil_designer import LoginVerifyTemplate
from ..scripts.recaptcha import enforce_recaptcha
from ..scripts.client import (
    initiate_auth,
    validate_token,
)

from anvil import *
from anvil.js import get_dom_node, window

PASSCODE_LENGTH = 6


def add_passcode_keyup_event(form, element):
    def event_listener(event):
        form.passcode_change(key=event.key, sender=element)

    return event_listener


class LoginVerify(LoginVerifyTemplate):

    def setup_passcodes(self):
        for num in range(1, PASSCODE_LENGTH + 1):
            element = getattr(self, f'pc_{num}')

            element.tag = {
                'pre': None if num == 1 else getattr(self, f'pc_{num - 1}'),
                'next': None if num == PASSCODE_LENGTH else getattr(self, f'pc_{num + 1}'),
            }

            html_element = get_dom_node(element)
            html_element.autocomplete = 'nope'
            html_element.onkeyup = add_passcode_keyup_event(self, element)

    def passcode_available(self):
        return all(
            element.text or element.text == 0 for element in [
                getattr(self, f'pc_{num}') for num in range(1, PASSCODE_LENGTH + 1)]
        )

    def mask(self, email):
        index = email.find('@')
        if index > 0:
            return email[0] + '******' + email[index - 1:]

    def get_passcode(self):
        passcode = ''

        for num in range(1, PASSCODE_LENGTH + 1):
            element = getattr(self, f'pc_{num}')
            passcode = f'{passcode}{element.text}'

        return passcode

    def clear_passcode(self):
        for num in range(1, PASSCODE_LENGTH + 1):
            element = getattr(self, f'pc_{num}')
            element.text = ''

    def __init__(self, email, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.email = email
        self.setup_passcodes()
        self.resent_otp_timeout = None
        self.instruction_label.text = f'An email with verification code was just sent to {self.mask(email)}'

    def handle_resend_otp(self):
        timeout = 31

        def recalculate_timeout(t):
            self.new_code_label.visible = True
            self.resent_link.visible = False
            self.resent_label.visible = True
            t = t - 1
            self.new_code_label.text = f'You can request a new code after {t} seconds.'

            if t > 0:
                window.setTimeout(recalculate_timeout, 1000, t)
            else:
                self.new_code_label.visible = False
                self.resent_link.visible = True

        if not self.resent_otp_timeout:
            self.resent_otp_timeout = window.setTimeout(
                recalculate_timeout,
                1000,
                timeout,
            )

    @enforce_recaptcha
    def verify_click(self, recaptcha_token, **event_args):
        result = validate_token(self.email, self.get_passcode(), recaptcha_token)

        if result:
            open_form('secure.Home')
        else:
            self.validation_error_label.visible = True
            self.clear_passcode()
            self.pc_1.focus()

    def passcode_change(self, **event_args):
        self.validation_error_label.visible = False
        element = event_args['sender']
        pre = element.tag['pre']
        key = event_args['key']
        value = element.text

        if key.__eq__('Backspace'):
            if value.__eq__('') and pre:
                pre.focus()
        else:
            value = element.text
            no_digit = True
            for char in value:
                if char.isdigit() and element:
                    no_digit = False
                    element.text = char
                    element = element.tag['next']

                if element:
                    element.focus()

            if no_digit:
                element.text = ''

        self.verify.enabled = self.passcode_available()

    def form_show(self, **event_args):
        self.pc_1.focus()
        window.setTimeout(self.handle_resend_otp, 30000)

    @enforce_recaptcha
    def resent_link_click(self, recaptcha_token, **event_args):
        self.new_code_label.visible = False
        self.resent_link.visible = False
        self.resent_label.visible = False
        self.validation_error_label.visible = False
        self.resent_otp_timeout = None
        initiate_auth(self.email, recaptcha_token)
        self.clear_passcode()
        self.pc_1.focus()
        window.setTimeout(self.handle_resend_otp, 30000)
