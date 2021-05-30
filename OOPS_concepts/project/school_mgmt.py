from OOPS_concepts.project.student_details import student
from OOPS_concepts.project.teachers_details import teacher
from OOPS_concepts.project.account_details import account


class school():
    def __init__(self, school_name, school_address, st_email, st_name, tech_name, tech_email, acc_name, acc_email):
        self.school_name = school_name
        self.school_address = school_address
        self.st_obj = student(st_name, st_email)
        self.tech_obj = teacher(tech_name, tech_email)
        self.acc_obj = account(acc_name, acc_email)

    def show_school_name(self):
        print("School Name :", self.school_name)

    def show_school_addres(self):
        print("School Address :", self.school_address)



