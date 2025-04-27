import random

print("Welcome to the game of fate. You hold a single bullet in your gun. If it fires, your fate is sealed. You each begin with a 3 heartbeat <3 ... Good luck surviving.")

player1_name = input("Enter the first player's name: ")
player2_name = input("Enter the second player's name: ")

player1_health = player2_health = 1

bullet_position1 = random.randint(1, 6)
bullet_position2 = random.randint(1, 6)

while player1_health > 0 and player2_health > 0:
    print(f"\nIt's {player1_name}'s turn...")
    bullet1 = random.randint(1, 6)
    choice_1 = input()
    if choice_1 == "me":
        if bullet1 == bullet_position1:
        	player1_health -= 1
        	print("The gun fires... darkness claims you.")
        else:
        	print(f"{player1_name} hears an empty click... safe, for now.")
        	
        if player1_health == 0:
            break
    else:
        if bullet1 == bullet_position1:
        	player2_health -= 1
        	print("The gun fires... darkness claims you.")
        else:
            print(f"{player2_name} hears an empty click... safe, for now.")
        if player2_health == 0:
            break
    print(f"\nIt's {player2_name}'s turn...")
    bullet2 = random.randint(1, 6)
    if bullet2 == bullet_position2:
        player2_health -= 1
        print("The gun fires... shadows take you.")
    else:
        print(f"{player2_name} survives... but the silence is deafening.")
        
print(f"\nGame Over. {player1_name} has fallen." if player1_health == 0 else f"\nGame Over. {player2_name} has fallen.")