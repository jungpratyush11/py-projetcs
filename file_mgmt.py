import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f" File {filename} has been created")
    except FileExistsError:
        print(f" File {filename} already exists")
    except Exception as E:
       print("An error occured") 
       
def view_files():
    files=os.listdir()
    if not files:
        print("File not found")
    else:
        print("File is in directory")
        for file in files:
            print(file)
            
def delete_files(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occured") 
        
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"{filename} has content - {content}")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occured") 

def edit_file(filename):

    try:
        if not os.path.exists(filename):
            print("File not found")
            return

        with open(filename,'a') as f:
            content=input("Enter data to add=")
            f.write(content+"\n")
            print(f"content added to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}") 
        
def main():
   while True:
       print("---Welcome to File Management System---")
       
       print("1-create")
       print("2-view")
       print("3-delete")
       print("4-read")
       print("5-edit")
       print("6-exit")
       
       choice=int(input("Enter your choice="))
       
       if choice==1:
           filename=input("Enter file name to create=")
           create_file(filename)
           
       elif choice==2:
           view_files()
           
       elif choice==3:
           filename=input("Enter file name to delete=")
           delete_files(filename)
           
       elif choice==4:
           filename=input("Enter file name to read=")
           read_file(filename)
           
       elif choice==5:
           filename=input("Enter file name to edit=")
           edit_file(filename)
           
       elif choice==6:
           print("Exiting Program")
           exit()
           
       else:
           print("Invalid choice")
           
main()