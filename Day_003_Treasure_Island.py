print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')

print("Welcome to Treasure Island!\nYour mission is to find the treasure\nYou're at a cross road. Where do you want to go?")
choice1 = input('Type "left" or "right"\n')
if choice1 == "left" or choice1 == "Left":
    choice2 = input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across.\n''')
    if choice2 == "wait" or choice2 == "Wait":
        choice3 = input('''You've entered a room with three doors- blue, red or yellow. Which one will you choose?\n''')
        if choice3 == "blue" or choice3 == "Blue":
            print("You got eaten by beasts. Game Over.")
        elif choice3 == "red" or choice3 == "Red":
            print("You got burned by fire. Game Over.")
        elif choice3 == "yellow" or choice3 == "Yellow":
            print("There is a huge golden chest behid the door. You Win!")
        else:
            print("You chose a door that does not exist. Game Over.")
    else:
        print("You got attacked by a trout. Game Over.")
else: 
    print("You fell into a hole. Game Over")