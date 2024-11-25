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
choices = [rock, paper, scissors]

choice_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choice_computer = random.randint(0,2)

print(f"\nYou chose: {choices[choice_player]}")
print(f"Computer chose: {choices[choice_computer]}")

if choice_player == choice_computer:
    print("Draw.")
elif(choice_player == 0 and choice_computer == 2) or \
    (choice_player == 1 and choice_computer == 0) or \
    (choice_player == 2 and choice_computer == 1):
    print("You win!")
else:
    print("You lose.")