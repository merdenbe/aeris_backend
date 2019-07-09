from .models import Major
from ..utils import Session_Maker


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def listMajors(self):
        # Get Majors
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            majors = session.query(Major).all()
            return [major.name for major in majors]
