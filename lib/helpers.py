from models.department import Department

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            location = input("Enter the department's new location: ")
            department.name = name
            department.location = location
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')
