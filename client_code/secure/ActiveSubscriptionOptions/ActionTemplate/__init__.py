from ._anvil_designer import ActionTemplateTemplate
from ....scripts.client import get_action_link

from anvil.js import window


class ActionTemplate(ActionTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    def action_link_click(self, **event_args):
        link = get_action_link(
            self.parent.product_id,
            self.parent.subscription_id,
            self.item['id'],
        )

        if link:
            window.open(link, '_blank')
