from ._anvil_designer import LinkTemplateTemplate


class LinkTemplate(LinkTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.link = properties.get('link')
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
