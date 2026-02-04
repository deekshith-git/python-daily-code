#logical operators and nested condition
#1
a = int(input("Enter first number: "))
if a in range(1, 101):
    print("valid")
else:
    print("Invalid")

#2
a = int(input("Enter maths mark: "))
b = int(input("Enter science mark: "))
if (a >= 40) and (b >= 40):
    print("pass")
else:
    print("Fail")

#3
age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ").lower()
if age >= 18 and license == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")