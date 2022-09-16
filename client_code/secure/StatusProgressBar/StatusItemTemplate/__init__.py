from ._anvil_designer import StatusItemTemplateTemplate

status_icon_map = {
    'complete': 'fa:check-circle',
    'in_progress': 'fa:circle',
    'pending': 'fa:circle',
}


class StatusItemTemplate(StatusItemTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        status = self.item.get('status')
        if status:
            self.status_label.role = f'status-{status}'
            self.status_label.icon = status_icon_map.get(status)
