import ujson

from falcon import HTTP_NO_CONTENT

class LoginResource:

    def on_post(self, req, resp):
        body = ujson.loads(req.stream.read())
        print(body["email"])
        print(body["password"])

        resp.status = HTTP_NO_CONTENT
