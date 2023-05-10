from config import *
from requests import get


def list_to_view(iterable: list):
    res = ''
    if iterable:
        for item in iterable:
            res = res + '<tr>'
            for line in item:
                res = res + f'<td>{line}</td>'
            res = res + '</tr>'
    else:
        res = '<tr><td>No data given.</td></tr>'
    return res


def events(events_data: dict) -> str:
    with open(EVENTS_TEMPLATE, 'r') as template:
        page = template.read()
        return page.format(**events_data)


def maps(maps_data: dict) -> str:
    image_url = get_place(maps_data)
    with open(MAPS_TEMPLATE, 'r') as template:
        return template.read().format(image_url)


def main_page() -> str:
    with open(MAIN_PAGE, 'r') as template:
        return template.read()


def error_page(error: str) -> str:
    with open(ERROR_PAGE, 'r') as template:
        return template.read().format(error=error)

def get_place(query: dict) -> str:
    def g_image(url):
        response = get(url, timeout=(5, 5))
        if response.status_code != OK:
            return BAD_REQUEST
        elif response.status_code == OK:
            return url

    if query:
        if query['places'] == 'arena':
            return g_image(places['arena'])
        elif query['places'] == 'sigma':
            return g_image(places['sigma'])
        elif query['places'] == 'lyceum':
            return g_image(places['lyceum'])
    else:
        return g_image(places['karaganda'])
