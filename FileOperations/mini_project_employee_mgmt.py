
def add_employee_details(emp_db='employee_db.txt', **kwargs):
    employee_info = kwargs

    with open(emp_db, 'r') as file:
        alllines = file.readlines()
        last_line = alllines[-1]
        recent_data = last_line.split("=")
        print(recent_data)
        user_data = recent_data[0].split("_")
        print("user_data :", user_data)
        recent_id = user_data[1]
        new_id = int(recent_id)+1
        print(new_id)

    with open(emp_db, 'a') as file2:
        new_entry = f"\nuser_{new_id}={employee_info}"
        file2.write(new_entry)


#add_employee_details(name='john', age=50, surname='doe', address='Newyork')
#add_employee_details(name='rahul', age=60, surname='sharma', address='Newyork')


def overwrite_emp_info(emp_id, emp_db='employee_db.txt',  **kwargs):
    new_data = ''
    with open(emp_db, 'r') as file:
        alllines = file.readlines()
        for line in alllines:
            user_id = line.split("=")[0]
            if user_id == emp_id:
                new_line= f"{user_id}={kwargs}"
                new_data = new_data + new_line+"\n"
            else:
                new_data = new_data + line

    with open(emp_db, 'w') as file2:
        file2.write(new_data)


overwrite_emp_info('user_2', name='Tejas', surname='sharma', salary=56660, age=34)

# Assingment
#remove employee details
#show employee details


# Resturant management project

#1 add items
#2 Remove items
#3 shows items
#4 purchase items
#5 generate bill