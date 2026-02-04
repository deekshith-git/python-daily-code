#1
amount = int(input("Enter the total amount: "))
membership = input("Have membership? yes/no: ").strip().lower()
print("Original amount: ", amount)

if amount >= 5000 and membership == "yes":
    price = amount * ((100 - 20)/100)
    print("20% Discount applied ")
elif amount >= 5000 and membership == "no":
    price = amount * ((100 - 10)/100)
    print("10% Discount applied ")
else:
    price = amount
    print("no discount")

print("Final payable amount: ", price)

#2
year = int(input("Enter Experience in years: "))
rate = int(input("Enter Performance rating(1-5): "))
salary = int(input("Enter current salary: "))

if year >= 3 and rate >= 5:
    bonus_rate = 0.20
    print("20% bonus added: ")
elif year >= 3 and rate >= 4:
    bonus_rate = 0.10
    print("10% bonus added: ")
else:
    bonus_rate = 0
    print("no bonus")

bonus = salary * bonus_rate
total = salary + bonus
print(f"bonus amount: {bonus}")
print(f"total pay: {total}")

