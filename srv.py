import json
# import falcon
from falcon import App
from falcon_cors import CORS
from rest import info

cors = CORS(allow_origins_list=['http://localhost:3000'])

api = App(middleware=[cors.middleware])
api.add_route('/info', info.Info())
