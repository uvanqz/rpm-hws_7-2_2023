HOST = '127.0.0.1'
PORT = 8001

# TEMPLATES
MAIN_TEMPLATE = 'index.html'
EVENTS_TEMPLATE = 'events.html'
PLACES_TEMPLATE = 'maps.html'

# PAGES
EVENTS = '/events'
PLACES = '/maps'
MAIN = '/'
PAGES = EVENTS, PLACES

# db
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}'
GET_TOKEN = "SELECT token FROM token WHERE username='{username}'"
EVENTS_ALL_ATTRS = ['id', 'event', 'date_s', 'description', 'location']
EVENTS_REQ_ATTRS = ['event', 'description', 'location']
POST_URL = f'http://{HOST}:{PORT}{EVENTS}?id='

# HTTTP codes
OK = 200
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERR = 500

# CODING
ENCODING = 'KOI8-R'

# maps consts
URL = "https://static-maps.yandex.ru/1.x/?l=map&ll={}&size=650,450&z={}&l=map&pt=37.620070,55.753630,pmwtm1~37.64,55.76363,pmwtm99"
places = {
    "lyceum": URL.format("39.98161706,43.40416754", "17"),
    "sigma": URL.format("39.98015207,43.40067092", "17"),
    "arena": URL.format("39.95343842,43.40890090", "17"),
    "karaganda": URL.format("73.08149641,49.81310069", "11"),
}

# headers' names
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'
