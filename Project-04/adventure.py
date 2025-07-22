name = input("Hiya What's your name? ")
print(f"Welcome to the adventure {name}" )
answer = input ("Now pick a direction left or right ").lower()

if answer == "left":
    print("You've entered pochinki")
    q2 = input(("Now L or R" : )).lower
    
    if q2 == "l" or q2 == "r":
        print("you've been killed ")
    else: 
        print("You're dead mother fucker")
        quit()
        
    
elif answer == "right":
    print("You are dead")
    quit()
else:
    print("You lose, Enter a valid direction you fool.! ")
    quit()
    
""" 

# FUNCTION FOR SLOW PRINTING 
 
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 
    
"""