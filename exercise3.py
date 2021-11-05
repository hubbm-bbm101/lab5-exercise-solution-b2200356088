import random 
number = random.randint(0,100)

while True:
    guess =int(input("Number:"))
    if guess > number:
        print("Decrease your number")
    elif guess < number :
        print("Increase your number")
    else:
        print("Your guess is correct")
        break