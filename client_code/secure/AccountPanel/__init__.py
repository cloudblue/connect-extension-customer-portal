from ._anvil_designer import AccountPanelTemplate

from anvil import alert, open_form
from anvil.users import logout


class AccountPanel(AccountPanelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    def logout_click(self, **event_args):
        result = alert(
            content="You will be logged out immediately. Are you sure?",
            title="Logout",
            buttons=[
                ("Yes", "YES"),
                ("Cancel", "NO"),
            ],
        )

        if result == 'YES':
            logout()
            open_form('Login')
