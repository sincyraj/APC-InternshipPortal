from Include.User import User


class Company(User):
    def __init__(self, name, id, address, phone_number, email_id, internships, internship_coordinator_name, internship_coordinator_Id):
        super().__init__(name, id, address, phone_number, email_id)
        self.internships=internships
        self.internship_coordinator_name=internship_coordinator_name
        self.internship_coordinator_Id=internship_coordinator_Id

    def create_internship(self):
        pass
    def track_progress(self):
        pass