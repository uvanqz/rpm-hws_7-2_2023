# server host and port
HOST = '127.0.0.1'
PORT = 8001

# pages
MAPS = '/maps'
EVENTS = '/events'
PAGES = (MAPS, EVENTS)

# templates paths
TEMPLATES = 'templates/'
MAIN_PAGE = f'{TEMPLATES}index.html'
EVENTS_TEMPLATE = f'{TEMPLATES}events.html'
MAPS_TEMPLATE = f'{TEMPLATES}maps.html'
ERROR_PAGE = f'{TEMPLATES}error.html'

# HTTP headers
CONTENT_LENGTH = 'Content-Length'
CONTENT_TYPE = 'Content-Type', 'text/html'
AUTH = 'Authorization'

# HTTP server error codes
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
INTERNAL_ERROR = 500

# HTTP OK codes
OK = 200
CREATED = 201
NO_CONTENT = 204

# other HTTP codes
NOT_IMPLEMENTED = 501

# db requests
RETURN_ID = " returning id"
SELECTOR = 'SELECT id, event, date_s, description, location FROM events'
GET_TOKEN = 'SELECT token FROM token WHERE username=\'{username}\''
INSERT = 'INSERT INTO {table} ({keys}) VALUES ({values}) RETURNING id'
UPDATE = 'UPDATE {table} SET {request}'
DELETE = 'DELETE FROM {table} '
EVENTS_REQ_ATTRS = ['event', 'description', 'location', 'date_s']
EVENTS_ALL_ATTRS = ['id', 'event', 'date_s', 'description', 'location']
MAPS_ATTRS = ['places']

# page str to byte coding
CODING = 'KOI8-R'
# maps things
URL = "https://static-maps.yandex.ru/1.x/?l=map&ll={}&size=650,450&z={}&l=map&pt=37.620070,55.753630,pmwtm1~37.64,55.76363,pmwtm99"
places = {
        "lyceum": URL.format("39.98161706,43.40416754", "17"),
        "sigma": URL.format("39.98015207,43.40067092", "17"),
        "arena": URL.format("39.95343842,43.40890090", "17"),
        "karaganda": URL.format("73.08149641,49.81310069", "11")
    }
