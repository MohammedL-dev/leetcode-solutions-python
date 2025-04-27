import random

def russian_roulett_game():
    num_bullet = 0
    switch_turn = True 
    player1_health = player2_health = 1
    #bullet_position = random.randint(1, 6)
    player_start = random.choice([1, 2])
    list_length = random.randint(3, 8)
    random_list = [random.choice([0, 1]) for _ in range(list_length)]
    #random_list.append(1)
    random.shuffle(random_list)
    print("Welcome to the game of fate. You hold a single bullet in your gun. If it fires, your fate is sealed. You each begin with a 3 heartbeat <3 ... Good luck surviving.")
    player1_name = input("Enter the first player's name: ")
    player2_name = input("Enter the second player's name: ")
    
    
    for bullet in random_list:
    	num_bullet += bullet
    void_bullet = list_length - num_bullet
    if num_bullet == 0:
        random_list.append(1)
        random.shuffle(random_list)
        num_bullet += 1
    print(f"You have {num_bullet} prepared bullets and {void_bullet} empty bullets.")
    
    while player1_health > 0 and player2_health > 0:
        
        current_player = player1_name if player_start == 1 else player2_name
        print(f"\nIt's {current_player}'s turn...")
        bullet = random.randint(1, 6)
        choice = input("Type 'me' to take your turn: ")
        
        
        if choice.lower() == "me":
        
            if random_list[0] == 1:
                if player_start == 1:       
                    player1_health -= 1
                else:
                	player2_health -=1
                print("The gun fires... darkness claims you.")
            else:
                print(f"{current_player} hears an empty click... safe, for now.")
                switch_turn = False
            
            if player1_health == 0 or player2_health == 0:
                break
            
        else:
        
            if random_list[0] == 1:
                if player_start == 1:       
                    player2_health -= 1
                else:
                	player1_health -=1
                print("The gun fires... darkness claims you.")
            
            else:
                print(f"{player1_name if player_start == 1 else player2_name} hears an empty click... safe, for now.")
                
        random_list.pop(0)
        
        if switch_turn:
            player_start = 2 if player_start == 1 else 1
    print(f"\nGame Over. {player1_name} has fallen." if player1_health == 0 else f"\nGame Over. {player2_name} has fallen.")
russian_roulett_game()



#    switch_turn()
   


#def switch_turn():
#    global current_player
#    global player_health 
#    if return_turn:
#        if current_player == player2_name:
#	        current_player = player1_name
#	        player_health = player1_health
#        else:
#        	current_player = player2_name
#        	player_health = player2_health


#if player_start == 1:
#	current_player = player1_name
#	player_health = player1_health
#	other_current_player = player2_name
#	other_player_health = player2_health
#else:
#	current_player = player2_name
#	player_health = player2_health
#	other_current_player = player1_name
#	other_player_health = player1_health
#	
#	
#while player1_health > 0 and player2_health > 0:
#    return_turn = True
#    print(f"\nIt's {current_player}'s turn...")
#    bullet = random.randint(1, 6)
#    choice = input("Type 'me' to take your turn: ")
#    
#    if choice.lower() == "me":
#        
#        if bullet == bullet_position:
#            player_health -= 1
#            print("The gun fires... darkness claims you.")
#            
#        else:
#            print(f"{current_player} hears an empty click... safe, for now.")
#            return_turn = False
#            
#        if player_health == 0:
#            break
#            
#    else:
#        
#        if bullet == bullet_position:
#            other_player_health -= 1
#            print("The gun fires... darkness claims you.")
#            
#        else:
#            print(f"{other_player_health} hears an empty click... safe, for now.")
#            
#    switch_turn()
        
