import json
import falcon

class Info:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = {}
        data['message'] = "Hello World, Roellie!!"
        resp.body = json.dumps(data)