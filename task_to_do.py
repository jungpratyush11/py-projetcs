def task():
    tasks=[]
    print("------WELCOME TO TASK MANAGEMENT APP-----")
    total_task=int(input("Enter total task you want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}=")
        tasks.append(task_name)
    print(f"Tasks for today {tasks}")
        
    while True:
        check=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Quit\n"))
        if check==1:
            add=input("Enter task to add=")
            tasks.append(add)
            
        elif check==2:
            update=input("Enter task to update=")
            if update in tasks:
                up=input("Enter new task to add=")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"Task updated to {up}")
            else:
                print("Task not found!!!")
                
        elif check==3:
            del_value=input("Enter task to delete=")
            if del_value in tasks:
                ind=tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} has been deleted")
            else:
                print("Task not found!!!")
                
        elif check==4:
            print(f"Tasks are {tasks}")
        
        elif check==5:
            print("Thank you for using this app")
            break
        else:
            print("Invalid Choice")
            
task()