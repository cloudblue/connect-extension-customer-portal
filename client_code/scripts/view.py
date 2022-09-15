from anvil.js import get_dom_node, window
from anvil.js.window import jQuery


def change_status_background_color(component, subscription_status):
    status = get_dom_node(component)
    class_list = status.getElementsByTagName(
        'span',
    )[0].classList

    for to_remove in ['active', 'processing', 'terminating', 'terminated', 'suspended', 'inquiring']:
        class_list.remove(to_remove)

    class_list.add(subscription_status)


def __set_element_height_to_window_end(self, element):
    client_rect = element.getBoundingClientRect()
    if window.innerWidth > 768:
        element.style.height = f'{window.innerHeight - client_rect.top}px'
    else:
        element.style.height = 'auto'


def set_com_height_to_window_end(component):
    flex_column = get_dom_node(component)
    __set_element_height_to_window_end(None, flex_column)


def add_class(component, css_class):
    element = get_dom_node(component)
    element.classList.add(css_class)


def fix_height_to_window_end(css_class):
    jQuery(f'.{css_class}').each(__set_element_height_to_window_end)


def make_target_new_tab(component):
    element = get_dom_node(component)
    a_elements = element.getElementsByTagName('a')
    for a in a_elements:
        a.target = '_blank'


def set_opacity(clazz, opacity):
    def set_element_opacity(self, element):
        element.style.opacity = opacity

    jQuery(f'.{clazz}').each(set_element_opacity)
