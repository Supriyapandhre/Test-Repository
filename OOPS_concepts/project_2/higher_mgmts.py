from OOPS_concepts.project_2.school_mgmt import school

school_name = "Valley International School"
school_address = "Mumbai"
st_email = 'John@gmail.com'
st_name = 'John'
tech_name = 'Marrycom'
tech_email = 'Marycom@gmail.com'
acc_name = 'Rohan sharma'
acc_email = 'rohan@gmail.com'


sch_obj = school(school_name, school_address, st_email, st_name, tech_name, tech_email, acc_name, acc_email)

# Access Students Details

sch_obj.show_student_name()
sch_obj.show_student_email()
print("_"*50)
# Access Teachers Details

sch_obj.tech_obj.show_teacher_name()
sch_obj.tech_obj.show_teacher_email()
print("_"*50)
# Account details

sch_obj.acc_obj.show_account_name()
sch_obj.acc_obj.show_account_email()


