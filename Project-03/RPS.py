import random as ra

usr_wins = 0
computer_wins = 0
draw = 0
options = ["rock", "paper", "scissor"]


while True:
    usr_input = input("Type Rock/Paper/scissor to play or 'q' to quit: ").lower()

    if usr_input == "q":
        break

    if usr_input not in options:
        print("Enter a valid object to play")
        continue

    random_number = ra.randint(0, 2)
    computer_pick = options[random_number]

    print(f"Computer had picked {computer_pick} as it's choice. ")

    if usr_input == "rock" and computer_pick == "scissors":
        print("you won")
        usr_wins += 1
    elif usr_input == "paper" and computer_pick == "rock":
        print("you won")
        usr_wins += 1
    elif usr_input == "scissor" and computer_pick == "paper":
        print("you won")
        usr_wins += 1
    elif usr_input == computer_pick:
        print("draw")
        draw += 1
    else:
        print("You lost")
        computer_wins += 1
        continue


print("\n")
print(f"You won {usr_wins} times")
print(f"Computer won {computer_wins} times")
print(f"Matches drawed {draw} times")

print("good BYE")
