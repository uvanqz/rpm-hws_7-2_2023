from config import EVENTS_TEMPLATE, MAIN_TEMPLATE, PLACES_TEMPLATE


def list_to_paragraphs(data: list):
    return ''.join([f'<ul>{value}</ul>' for value in data]) if data else '<p>No data given.</p>'


def events(events_data: dict) -> str:
    with open(EVENTS_TEMPLATE, 'r') as fun:
        return fun.read().format(**events_data)


def main_page() -> str:
    with open(MAIN_TEMPLATE, 'r') as fun:
        return fun.read()


def places(place: str) -> str:
    with open(PLACES_TEMPLATE, 'r') as fun:
        return fun.read().format(place)
