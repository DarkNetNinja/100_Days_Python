import random

rock  = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = input("What do you choose? Type 0 for Rock,1 for paper or 2 for scissors. \n")
collection = [rock,paper,scissor]
if int(user_choice) < 0 or int(user_choice )> 2:
    print("Invalid choice")
    print("Number should be 0,1 or 2.")
else:
    choice = collection[int(user_choice)]
    print("User choice")
    print(choice)

    computer_choice = random.choice(collection)
    print("Computer choice")
    print(computer_choice)

    if (choice == rock and computer_choice == paper) or (choice == paper and computer_choice == scissor) or (choice == scissor and computer_choice == rock):
        print("YOU LOSE")
    elif (choice == computer_choice):
        print("TIE")
    else:
        print("YOU WIN")