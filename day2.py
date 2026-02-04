#variables + input + output
#1
user = input("Enter your favorite movie: ")
print(f"Your favorite movie is {user}")

#2
country = input("Enter country name: ")
capital = input("Enter capital of that country: ")
print(f"The capital of {country} is {capital}")

#3
name = input("Enter Product name: ")
quantity = int(input("Enter the quantity in grams: "))
price = 100
total = price * (quantity/1000)
print(f"You brought {quantity} grams {name} for a total of {total} rupees.")