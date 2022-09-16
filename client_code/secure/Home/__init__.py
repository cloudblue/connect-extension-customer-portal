from ._anvil_designer import HomeTemplate
from ..ProductList import ProductList

from anvil import ColumnPanel, alert, open_form
from anvil.js import window
from anvil.users import logout

from ...scripts.view import fix_height_to_window_end, set_opacity


def do_action(event):
    fix_height_to_window_end('fix-height')


class Home(HomeTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.content_panel = ColumnPanel(
            spacing_above=None,
            spacing_below=None,
            col_spacing=None,
        )
        self.add_component(self.content_panel)
        self.product_list_panel = ProductList(self.content_panel)
        self.content_panel.product_detail_panel = None

        self.content_panel.add_component(
            self.product_list_panel,
            full_width_row=True,
        )

        window.onresize = do_action

    def lnk_home_click(self, **event_args):
        self.content_panel.clear()

        if not self.product_list_panel:
            self.product_list_panel = ProductList(self.content_panel)

        self.content_panel.add_component(
            self.product_list_panel,
            full_width_row=True,
        )

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

    def form_show(self, **event_args):
        set_opacity('grecaptcha-badge', 0)
