#Basic If Statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You are too young.")

#Password Checker
password = input("Enter password: ")
if password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")

#Compare two numbers and print which one is larger.
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
if Num1 > Num2:
    print (str(Num1),"is greater than",str(Num2))
elif Num2 > Num1:
    print (str(Num2),"is greater than",str(Num1))
else:
    print ("Both numbers are equal")


#Discount Checker
membership = True
coupon = True
if membership and coupon:
    print ("You are eligible for a discount")
elif membership:
    print ("You do not have coupon")
elif coupon:
    print ("You do not have a membership")
else:
    print ("You have not met any of the requirements")

#Nested Condition Example
score = int(input ("What did you score on the exam? "))
if score >= 50 and score <= 100 and score >= 0:
    print ("You passed")
    if score >= 90:
        print ("Your score is excellent!!")
elif score > 100 or score < 0:
    print ("Range Error : Enter a value between 0-100")
else:
    print ("You failed")

#Login and Access Control System
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print ("Welcome. You have been granted access to the control panel")
else:
    print ("Invalid credentials")
    role = input("What's your role (user/guest)? ")
    if role == "user":
        print ("Welcome. You have been granted acess to the dashboard")
    elif role == "guest":
        print ("Welcome. You have been given limited access")
    else:
        print ("Invalid input")

#Odd and Even Checker
NumEO = int(input("Enter A Number: "))
if NumEO%2 == 0:
    print ("The inputted number is even")
else:
    print ("The inputted number is odd")

#Grade Checking System
score = int(input("Enter exam score: "))
if score <= 100 and score >= 90:
    print ("You got an A")
elif score <= 89 and score >= 80:
    print ("You got an B")
elif score <= 79 and score >= 70:
    print ("You got an C")
elif score > 100 or score < 0:
    print ("Range Error. Enter a value between 0 and 100")
else:
    print ("You failed")




