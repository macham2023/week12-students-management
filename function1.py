students_db ={}
def start():
    while True:
        print(
        '''
        1.Add student
        2.Delete student
        3.Update student record
        4.Get student record
        5.Display student record
        6.Search student by name
        7.Number of students in the system
        ''')
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            add_student()
        elif user_choice == 2:
            delete()
        elif user_choice == 3:
            student_update()
        elif user_choice == 4:
            student_record()
        elif user_choice == 5: 
            display_info()
        elif user_choice == 6:
            search_student_by_name()
        elif user_choice == 7:
            students_count()
        elif user_choice == 8:
            filter_by_age()
        else:
            print("Invalid user choice")

def add_student():
    student_id = 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    key = len(students_db) + 1
    students_db[key]={"name":name,"age":age,"department":department}
    print(students_db)


def delete():
    student_id = int(input("Enter id: "))
    if student_id in students_db:
        del students_db[student_id]
        print(f"student with id {student_id} has been deleted")
    else:
        print("id not found!")

def student_update():
    print('''
    1.update name
    2.update age
    3.update deparment
    ''')
    
    student_id = int(input("Enter id : "))
    if student_id in students_db:
        choice = int(input("Enter your choice here: "))
        if choice == 1:
            name = input("Enter your name to update: ")
            students_db[student_id].update({"name":name})
            print(students_db)    
       
        elif choice == 2:
            age = int(input("Enter age to be updated: "))
            students_db[student_id].update({"age":age})
            print(students_db)

        elif choice == 3:
       
            department = input("Enter name of department to be updated: ")
            students_db[student_id].update({"department":department})
            print(students_db)

    else:
        print("Invalid option")

def student_record():
    student_id = int(input("Enter the student id: "))
    if student_id in students_db:
        print(f'my name is {students_db[student_id]["name"]},  i am {students_db[student_id]["age"]}, from {students_db[student_id]["department"]} department')
   

def display_info():
    print(students_db)
            
def search_student_by_name():
    name_search = input("Enter  name to search: ")
    student_found = False
    for key,value in students_db.items():
        if value["name"] == name_search:
            print(f'id:{key},name:{value["name"]},age:{value["age"]},department:{value["department"]}')
            found = True
    if not found:
         print(f"student with name {name} does not exist")

def students_count():
    length = len(students_db)
    print(f"Ther are {length} students in the system")

def filter_by_age():
    age_filter = int(input("Enter minimum age: "))
    found = False
    for key,value in students_db.items():
        if value["age"] >  age_filter:
            print(f'id :{key},name:{value["name"]},age:{value["age"]},department:{value["department"]}')
            found = True
    if not found:
        print(f"Student with age less than {age_filter} does not exist")

start()












