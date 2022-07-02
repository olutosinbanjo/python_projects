"""

A mad lib is a word game, in which texts in a paragraph are replaced with blank spaces;

The user is then asked to fill in the blank spaces using named identifiers.

The resulting paragraph is read out loud for fun and laughter.

02-07-2022

"""

def science_():
    
    adj = input("adjective: ")
    v1 = input("verb1: ")
    v2 = input("verb2: ")
    v3 = input("verb3: ")
    name = input("name_of_person: ")

    science = (
        f"Science is full of {adj} stuffs! It {v1} real life problems,"
        f"while often {v2} them complex!"
        f"I still {v3} Science! Tell me {name}, do you love Science ?"
    )
    
    print("\nMAD LIB: \n")
    
    return print(science)


def history_():
    
    adj1 = input("adjective: ")
    v1 = input("verb1: ")
    adj2 = input("adjective: ")
    v2 = input("verb2: ")
    name = input("name_of_person: ")
    
    history = (
        f"History is full of {adj1} stuffs! It {v1} never forget events,"
        f"it can be quite {adj2}!"
        f"I still {v2} History! Tell me {name}, do you love History ?"
        )

    print("\nMAD LIB: \n")
    
    return print(history)

def play():
    
    print("Mad lib for SCIENCE or HISTORY!\n")

    print("Please enter player name: ")
    name = input()
    print('\n')
    
    print("Please enter 0 to play for SCIENCE or 1 to play for HISTORY:\n")
    user_input = input()
    print('\n')


    if (user_input == 0):
        print(f"Dear {name}, you have entered 0 to play for SCIENCE.\n")
        print("Now Enter words.\n")
        science_()
    else:
        print(f"Dear {name}, you have entered 1 to play for HISTORY.\n")
        print("Now Enter words.\n")
        history_()

play()
