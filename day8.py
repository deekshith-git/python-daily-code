#while loop
#1
i = 1
while i <= 10:
    print(i)
    i += 1

#2
total = 0
user = int(input("Enter :"))

while user != 0:
    total += user
    user = int(input("Enter :"))
print("sum:",total)

a = 0
while True:
    user = int(input("Enter :"))
    if user == 0:
        break
    total += user
print("Sum: ", total)

#3
secret_number = 18
while True:
    user = int(input("Guess a number: "))
    if user == secret_number:
        print("Correct guess")
        break
    elif user < secret_number:
        print("Try a higher number")
    else:
        print("Try a lower number")

#4
import random
while True:
    number = random.randint(1, 50)
    attempts = 5
    score = 0
    print("\nGuess the number between 1 and 50")
    print("You have 5 attempts.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == number:
            score = attempts * 10
            print("Correct guess")
            print("Score: ",score)
            break
        elif guess < number:
            print("Try a higher number")
        else:
            print("Try a lower number")

        attempts -= 1
        print("Attempts left: ", attempts)

    if attempts == 0:
        print("Game over")
        print("secret number ", number)
    
    again = input("play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for playing!")
        break
