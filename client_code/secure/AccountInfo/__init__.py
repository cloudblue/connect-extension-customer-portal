from ._anvil_designer import AccountInfoTemplate


class AccountInfo(AccountInfoTemplate):

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.account = properties.get('account') or {}

        self.init_components(**properties)

    @property
    def account(self):
        return self.item

    @account.setter
    def account(self, value):
        self.item = value
        if self.item:
            phone = self.item['contact_info']['contact']['phone_number']
            self.item['phone'] = f"{phone['country_code']}-{phone['area_code']}-{phone['phone_number']}"
