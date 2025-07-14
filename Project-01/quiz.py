print("WELCOME TO THE QUIZ MOTHERFUCKERS...")

name = input("Whats your name? ")
player = input(f"Do you wanna play {name}? ")
score = 0

if player != "yes":
    print(f"GTFO {name}!")
    quit()

print("Welcome to the game you son of a bitch.")

q1 = input("Who's the best Max or GR? ").upper()

if q1 == "GR":
    print("you are GODDAMN RIGHT 👍🏻 ")
    score += 1
else:
    print("It's wrong, You piece of shit ")


q2 = input("Who cries more Verstappen or Norris? ").upper()

if q2 == "MAX" or "VERSTAPPEN":
    print("you are GODDAMN RIGHT 👍🏻 ")
    score += 1
else:
    print("It's wrong, You piece of shit ")


q3 = input("Who's 2021 Driver's Champion? ").upper()

if q3 == "LEWIS" or q3 == "HAMILTON":
    print("you are GODDAMN RIGHT 👍🏻 ")
    score += 1
else:
    print("It's wrong, You piece of shit ")

match (score):
    case 3:
        print("The score is 3 outta 3")
    case 2:
        print("The score is 2 outta 3")
    case 1:
        print("The score is 1 you dumbass")
    case _:
        print("The score is 0 you fucking shit")


print(f"Thanks {name} for trying out the quiz, and your point is " + str(score))
print(str((score / 3) * 100) + "percentage")
