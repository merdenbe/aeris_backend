import falcon

from .modules.test_route.resource import TestResource

# Creates an instance of the api
def create_api():
    # Initialize  api instance
    api = falcon.API()

    # Initialize resoure instances
    test_route = TestResource()

    # Declare routes
    api.add_route('/test_route', test_route)

    return api
