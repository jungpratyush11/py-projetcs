rent=int(input("enter your per month rent="))
foods=int(input("enter the amount spend per month on food="))
electricity=int(input("enter total electricity bill="))
units=int(input("enter per units on electricity="))
persons=int(input("enter no. of persons lives in room="))

total_electricityBill=electricity*units

sharing=(foods+total_electricityBill+rent)//persons

print("individuals should pay=",sharing)