#loops
#1
for i in range(1, 11):
    print(i)

#2
user = int(input("Enter a number: "))
for i in range(1, 11):
    print(user * i)

#3
n = int(input("Enter a number: "))
a = 0
for i in range(1, n+1):
    a += i
    print(a)