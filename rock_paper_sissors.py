import random

items = ["Rock", "Paper", "Scissor"]

user = input("enter your choice=Rock,Paper,Scissor ")
comp = random.choice(items)

print(f"the user choice is {user},computer choice is {comp}")

if user == comp:
    print("TIE")

elif user == "Rock":
    if comp == "Paper":
        print("Computer Wins")
    else:
        print("You Win")

elif user == "Paper":
    if comp == "Scissor":
        print("Computer Wins")
    else:
        print("You Win")

elif user == "Scissor":
    if comp == "Rock":
        print("Computer Wins")
    else:
     print("You Win") 