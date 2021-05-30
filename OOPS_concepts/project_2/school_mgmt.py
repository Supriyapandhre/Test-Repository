from OOPS_concepts.project_2.student_details import student
from OOPS_concepts.project_2.teachers_details import teacher
from OOPS_concepts.project_2.account_details import account


class school(student, teacher, account):
    def __init__(self, school_name, school_address, st_email, st_name, tech_name, tech_email, acc_name, acc_email):
        super().__init__(st_name, st_email)
        self.school_name = school_name
        self.school_address = school_address
        self.tech_obj = teacher(tech_name, tech_email)
        self.acc_obj = account(acc_name, acc_email)

    def show_school_name(self):
        print("School Name :", self.school_name)

    def show_school_addres(self):
        print("School Address :", self.school_address)



