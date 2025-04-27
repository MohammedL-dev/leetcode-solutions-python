import random
import time

def russian_roulette_game():
    # Game initialization
    player1_health = player2_health = 3  # Players start with 3 health
    chamber_size = 6  # Standard revolver has 6 chambers
    
    # Welcome message
    print("\n" + "="*60)
    print(" "*15 + "RUSSIAN ROULETTE - GAME OF FATE")
    print("="*60)
    print("\nWelcome to the game of fate. You each begin with 3 heartbeats <3")
    print("A revolver with a single bullet awaits. Will luck be on your side?")
    
    # Player setup
    player1_name = input("\nEnter the first player's name: ")
    player2_name = input("Enter the second player's name: ")
    
    # Determine who goes first
    player_turn = random.choice([1, 2])
    current_player = player1_name if player_turn == 1 else player2_name
    print(f"\n{current_player} will go first.")
    
    # Game setup
    bullet_position = random.randint(1, chamber_size)
    current_position = 1
    round_number = 1
    
    # Main game loop
    while player1_health > 0 and player2_health > 0:
        # Display round information
        print("\n" + "-"*50)
        print(f"Round {round_number} | Current turn: {current_player}")
        print(f"{player1_name}'s health: {'♥ ' * player1_health}")
        print(f"{player2_name}'s health: {'♥ ' * player2_health}")
        print("-"*50)
        
        # Player options
        print("\nOptions:")
        print("1. Pull the trigger (point at yourself)")
        print("2. Point at opponent and pull the trigger")
        print("3. Spin the chamber (randomizes bullet position)")
        
        # Get player choice
        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): "))
                if 1 <= choice <= 3:
                    break
                else:
                    print("Please enter a number between 1-3.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Process player choice
        if choice == 3:
            # Spin the chamber
            print("\nSpinning the chamber...")
            time.sleep(1)
            bullet_position = random.randint(1, chamber_size)
            current_position = 1
            print("*click* *click* *click* The chamber spins...")
            continue
            
        # Dramatic pause
        print("\n*click*")
        time.sleep(1)
        
        # Check if the bullet fires
        bullet_fired = current_position == bullet_position
        
        if bullet_fired:
            print("\n💥 BANG! The gun fires!")
            time.sleep(1)
            
            # Determine who gets hurt
            if choice == 1:  # Self
                if player_turn == 1:
                    player1_health -= 1
                    print(f"{player1_name} takes damage! {player1_health} hearts remaining.")
                else:
                    player2_health -= 1
                    print(f"{player2_name} takes damage! {player2_health} hearts remaining.")
            else:  # Opponent
                if player_turn == 1:
                    player2_health -= 1
                    print(f"{player2_name} takes damage! {player2_health} hearts remaining.")
                else:
                    player1_health -= 1
                    print(f"{player1_name} takes damage! {player1_health} hearts remaining.")
            
            # Reset after firing
            bullet_position = random.randint(1, chamber_size)
            current_position = 1
            print("\nThe gun has been reloaded with a single bullet in a random chamber.")
        else:
            print("*click* Empty chamber. The tension builds...")
            # Move to next chamber
            current_position += 1
            if current_position > chamber_size:
                current_position = 1
        
        # Switch turns
        player_turn = 2 if player_turn == 1 else 1
        current_player = player1_name if player_turn == 1 else player2_name
        round_number += 1
        
        # Continue prompt
        input("\nPress Enter to continue...")
    
    # Game over
    print("\n" + "="*60)
    print(" "*20 + "GAME OVER")
    print("="*60)
    
    if player1_health <= 0:
        print(f"\n{player1_name} has fallen. {player2_name} survives to live another day!")
    else:
        print(f"\n{player2_name} has fallen. {player1_name} survives to live another day!")

if __name__ == "__main__":
    russian_roulette_game()