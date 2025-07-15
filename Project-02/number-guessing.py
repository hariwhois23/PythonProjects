import random as ra


a = input("Enter a upper limit for the range you are gonna guess ")

if a.isdigit():
    up = int(a)

    if up <= 0:
        print("enter a number greater than zero ")
        exit()
else:
    print("Enter a number brat.")
    exit()

guesses = 0
random_number = ra.randint(1, up)

while True:
    usr = input("Make a guess: ")
    guesses += 1

    if usr.isdigit():
        usr = int(usr)
    else:
        print("Please enter a valid number ")
        continue  # redirect to the start of the loop if didnt get a porper number as an input

    if usr == random_number:
        print("")
        print("you got the number right in " + str(guesses) + " guesses.")
        print("The number was " + str(random_number))
        break  # to stop asking if the condition is satisfied

    else:
        if usr < random_number:
            print("Try higher")
        else:
            print("Try lower")
