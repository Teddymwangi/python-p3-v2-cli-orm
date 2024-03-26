from helpers import *

def main():
    while True:
        print("""
        Please select an option:
        0. Exit the program
        1. List all departments
        2. Find department by name
        3. Find department by id
        4. Create department
        5. Update department
        6. Delete department
        """)
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            find_department_by_name()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            create_department()
        elif choice == "5":
            update_department()
        elif choice == "6":
            delete_department()
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
