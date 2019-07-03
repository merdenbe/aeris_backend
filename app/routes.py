import os
import falcon

from .modules.reauthenticate.resources import ReauthenticateResource

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Creates an instance of the api
def create_api():
    # Initialize  api instance
    api = falcon.API()

    # Initialize database connection
    Api_Engine= create_engine(os.environ["DATABASE_URL"], echo=False)
    Api_Session = sessionmaker(bind=Api_Engine)

    # Initialize resoure instances
    reauthenticate_resource = ReauthenticateResource(Api_Session)

    # Declare routes
    api.add_route('/reauthenticate', reauthenticate_resource)

    return api
