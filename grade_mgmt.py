student_grades={}

def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with obtained marks {grade}")
    
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks updated to {grade}")
    else:
        print("Student Not Found!!!")
        
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted")
    else:
        print("Student Not Found!!!")
        
def display():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("Student Not Found!!!")
        
            
def main():
    while True:
        print("---Student Grade Management System---")
        print("1-ADD\n2-Update\n3-Delete\n4-View\n5-Exit\n")
        
        choice=int(input("Enter your choice="))
        if choice==1:
            name=input("Enter student name=")
            grade=int(input("Enter Grade="))
            add_student(name,grade)
        
        elif choice==2:
            name=input("Enter student name=")
            grade=int(input("Enter Grade="))
            update_student(name,grade)
            
        elif choice==3:
            name=input("Enter student name=")
            delete_student(name)
        
        elif choice==4:
            display()
            
        elif choice==5:
            print("Quitting program")
            break
        else:
            print("Invalid Choice")
            
main()
        