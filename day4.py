#operators
#1
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print(a + b)
print(a - b)
print(a * b)
if b != 0:
    print(a / b)
else:
    print("Division by zero is not allowed.")

#2
a = int(input("Enter a value: "))
print("even" if a % 2 == 0 else "odd")

#3
a = int(input("Enter mark1 value: "))
b = int(input("Enter mark2 value: "))
c = int(input("Enter mark3 value: "))
total = (a + b + c) / 3
print("Total marks:", total)
if total >= 40:
    print("Pass")
else:
    print("Fail")