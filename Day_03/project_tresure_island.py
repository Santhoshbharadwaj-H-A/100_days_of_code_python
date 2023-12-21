print("welcome to Tresure_Island")
print("your mission is to find the treasure.")
choice = input("you're at a the cross road where do you want to go? Type 'left' or 'right'\n").lower()

# if choice == 'right' or choice == '':
#     print("Fall  into a hole game over")

if choice == 'left':
    choice = input("swim or wait\n").lower()
    if choice == 'wait':
        choice = input("which doar\n").lower()
        if choice == 'yellow':
            print("you win")
        elif choice == 'red':
            print("burned by fire game over")
        elif choice == 'blue':
            print("eaten by beast, game over")
        else :
            print("game over")
    else:
        print("attaked by trout game over")
else:
    print("fall into the hole game over")
print("you played the game very well tank you for playing the game")


    
