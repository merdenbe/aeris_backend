import os
import falcon

from .modules.login.resource import LoginResource

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Creates an instance of the api
def create_api():
    # Initialize  api instance
    api = falcon.API()

    # Initialize database connection
    engine = create_engine(os.environ["DATABASE_URL"], echo=False)
    session = sessionmaker(bind=engine)

    # Initialize resoure instances
    login_resource = LoginResource()

    # Declare routes
    api.add_route('/login', login_resource)

    return api
