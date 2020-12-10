from Include.User import User

class University(User):

    def __init__(self, name, id, address, phone_number, email_id, course_codes, university_instructor_name, university_instructor_id):
        super().__init__(name, id, address, phone_number, email_id)
        self.course_names=course_codes
        self.university_instructor_name=university_instructor_name
        self.university_instructor_id=university_instructor_id

    def approve_internship(self):
        pass
    def reject_internship(self):
        pass


