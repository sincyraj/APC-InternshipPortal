from Include.User import User

class Student(User):
    def __init__(self, name, id, address, phone_number, email_id, course, university_id):
        super().__init__(name, id, address, phone_number, email_id)
        self.course=course
        self.university_id=university_id

    def display_student(self):
        print(f"The Student details are {self.name,self.course,self.university_id}")


    def submit_proposal(self):
        pass


stu=Student("Sincy","101","Perk","919345372819","sincy.raj@vub.be","MAC","VUB")
stu.display_student()



