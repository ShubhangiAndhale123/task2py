print("Mini Calculator")

num1 = float(input("enter the first number here:"))
num2 = float(input("enter the second number here:"))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \n press 4 for division")

choice = int(input("enter your choice from 1 to 4:"))

if choice == 1:
    print("the addition of two numbers=",num1 + num2)
elif choice == 2:
    print("the subtraction of two numbers=",num1 - num2)    
elif choice == 3:
    print("the multiplication of two numbers=",num1 * num2)   
elif choice == 4:
    print("the division of two numbers=",num1 / num2)   
else:
    print("invalid input")
