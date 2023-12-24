# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
# computer_option = random.randint(0,2) 
# rock = 0
# paper = 1
# scissors = 2 

# if user_option < 3:
#     if user_option == computer_option:
#         print("The match draw")
#     elif user_option == 0 and computer_option == 2:
#         print(f"you choosed\n{rock}")
#         print(f"computer choosaed\n{scissors}")
#         print("You won")
#     elif user_option == 2 and computer_option == 1:
#         print(f"you choosed\n{scissors}")
#         print(f"computer choosaed\n{paper}") 
#         print("you won")
#     elif user_option == 1 and computer_option == 0:
#         print(f"you choosed\n{paper}")
#         print(f"computer choosaed\n{rock}")
#         print("you won")
#     else:
#         if computer_option == 0 and user_option == 2:
#             print(f"you choosed\n{scissors}")
#             print(f"computer choosaed\n{rock}")
#             print("You Lost")
#         elif computer_option == 2 and user_option == 1:
#             print(f"you choosed\n{paper}")
#             print(f"computer choosaed\n{scissors}")
#             print("you Lost")
#         elif computer_option == 1 and user_option == 0:
#             print(f"you choosed\n{rock}")
#             print(f"computer choosaed\n{paper}")
#             print("you Lost")
# else:
#     print("invalid option Please Choose the vaid option")


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end