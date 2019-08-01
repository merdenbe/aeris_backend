import os
import falcon

from .modules.reauthenticate.resources import ReauthenticateResource
from .modules.register.resources import RegisterResource
from .modules.majors.resources import MajorResource
from .modules.course_requests.resources import CourseRequestResource
from .modules.feedback.resources import FeedbackResource
from .modules.questions.resources import QuestionResource
from .modules.profile.resources import ProfileResource
from .modules.coupons.resources import CouponResource
from .modules.topics.resources import TopicResource
from .modules.find_tutor.resources import FindTutorResource
from .modules.cancel_session.resources import CancelSessionResource
from .modules.log_session.resources import LogSessionResources

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
    feedback_resource = FeedbackResource(Api_Session)
    question_resource = QuestionResource(Api_Session)
    profile_resource = ProfileResource(Api_Session)
    coupon_resource = CouponResource(Api_Session)
    topic_resource = TopicResource(Api_Session)
    find_tutor_resource = FindTutorResource(Api_Session)
    cancel_session_resource = CancelSessionResource(Api_Session)
    log_session_resource = LogSessionResource(Api_Session)

    # Declare routes
    api.add_route('/reauthenticate', reauthenticate_resource)
    api.add_route('/register', register_resource)
    api.add_route('/majors', major_resource)
    api.add_route('/course_requests', course_request_resource)
    api.add_route('/feedback', feedback_resource)
    api.add_route('/questions', question_resource)
    api.add_route('/profile', profile_resource)
    api.add_route('/coupons', coupon_resource)
    api.add_route('/topics/{course_id:int()}', topic_resource)
    api.add_route('/find_tutor', find_tutor_resource)
    api.add_route('/cancel', cancel_session_resource)
    api.add_route('/log', log_session_resource)

    return api
