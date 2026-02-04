#loop control
#1
i = 0
while i < 10:
    i += 1
    if i == 6:
        break
    print(i)

#2
j = 0
while j < 10:
    j += 1
    if j % 3 == 0:
        continue
    print(j)

#3
while True:
    user = int(input("Enter a number: "))
    if user < 0:
        break
    if user % 5 == 0:
        continue
    print(user)
    