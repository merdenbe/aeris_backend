from .models import Question
from ..utils import Session_Maker


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def listQuestions(self):
        # Get Majors
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            questions = session.query(Question).all()
            return [{'question': q.content, 'answer': q.answer} for q in questions]
