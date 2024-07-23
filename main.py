import os
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
exit=True
while exit:
    user_choice=int(input("Enter your choice:\n"
    "0 for rock \n"
    "1 for papper\n"
    "2 for scissors\n"
    "3 for exit\n"))
    if user_choice==3:
        exit=False
        os.system('clear')
    elif user_choice not in [0,1,2]:
        os.system('clear')
        print("Invalid choice\n\n")
    else:
         all_choices=[rock,paper,scissors]

         choice=all_choices[user_choice]
         print(choice)

         computer_choice=random.randint(0,2)
         all_choices=[rock,paper,scissors]

         choice=all_choices[computer_choice]
         print(choice)  
         result=[["draw","lose","win"],["win","draw","lose"],["lose","win","draw"]]    
         print(f"{result[user_choice][computer_choice]}\n")