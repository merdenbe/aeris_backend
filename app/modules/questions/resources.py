class QuestionResource:

    # Return a list of majors for a given university
    def on_get(self, req, resp):

        resp.media = {'msg': 'Hello World'}

    def on_post(self, req, resp):

        resp.media = {'msg': 'Hello World'}

    def __init__(self, Api_Session):
        # self.db = db(Api_Session)
        self.Api_Session = Api_Session
