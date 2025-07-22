import time

# Slow printing effect
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Game starts
name = input("👾 Hiya! What's your name, warrior? ")
slow_print(f"🛡️ Welcome to the ultimate adventure, {name}!\n")

time.sleep(1)
answer = input("➡️ Choose your path — type 'left' or 'right': ").lower()

if answer == "left":
    slow_print("🚪 You take the left path... it's foggy. You hear footsteps.")
    time.sleep(1)
    slow_print("🏚️ You’ve entered... *Pochinki*. The air is tense.")
    time.sleep(1)

    q2 = input("❓ A fork ahead — go 'L' or 'R'? ").lower()

    if q2 == "l" or q2 == "r":
        slow_print("💥 Ambush! You’ve been killed by a lurking enemy.")
        slow_print("☠️ GAME OVER.")
    else:
        slow_print("🤯 Wrong move. You tripped on a landmine.")
        slow_print("💀 You're dead, brave one.")
        quit()

elif answer == "right":
    slow_print("💀 Bad luck. A sniper spotted you from a rooftop.")
    slow_print("☠️ You're dead before you even blinked.")
    quit()

else:
    slow_print("🤦‍♂️ Invalid choice, my friend.")
    slow_print("👻 You wandered into the void and were never seen again.")
    slow_print("☠️ GAME OVER.")
    quit()
