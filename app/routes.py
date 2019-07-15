import os
import falcon

from .modules.reauthenticate.resources import ReauthenticateResource
from .modules.register.resources import RegisterResource
from .modules.majors.resources import MajorResource
from .modules.course_requests.resources import CourseRequestResource
from .modules.feedback.resources import FeedbackResource

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Creates an instance of the api
def create_api():
    # Initialize  api instance
    api = falcon.API()

    # Initialize database connection
    Api_Engine = create_engine(os.environ["DATABASE_URL"], echo=False)
    Api_Session = sessionmaker(bind=Api_Engine)

    # Initialize resoure instances
    reauthenticate_resource = ReauthenticateResource(Api_Session)
    register_resource = RegisterResource(Api_Session)
    major_resource = MajorResource(Api_Session)
    course_request_resource = CourseRequestResource(Api_Session)
    feedback_resource = FeedbackResource()

    # Declare routes
    api.add_route('/reauthenticate', reauthenticate_resource)
    api.add_route('/register', register_resource)
    api.add_route('/majors', major_resource)
    api.add_route('/course_requests', course_request_resource)
    api.add_route('/feedback', feedback_resource)

    return api
