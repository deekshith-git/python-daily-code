#conditions
#1
user = int(input("Enter a value: "))
if user > 0:
    print("Positive")
elif user < 0:
    print("Negative")
else:
    print("zero")

#2
user = int(input("Enter your age: "))
if user < 13:
    print("child")
elif user >= 13 and user <= 19:
    print("Teenager")
else:
    print("Adult")

#3
username = input("Enter username: ")
password = input("Enter a password: ")
if username == "admin" and password == "1234":
    print("successful")
else:
    print("Failed")
