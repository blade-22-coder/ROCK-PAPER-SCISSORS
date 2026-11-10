import random
import time

#GAME SETTINGS
choices = ["rock", "paper", "scissors"]

player_health = 100
computer_health = 100

coins = 0
xp = 0
streak = 0

#INTRODUCTION
print("\t\t" + "=" *50)
print("\t\t\t\tROCK PAPER SCISSOR")
print("\t\t" + "=" *50)

player_name = input("\nEnter your warrior name: ")

print(f"\nWelcome to the arena, {player_name}!")
print("Your opponent is waiting....")
time.sleep(1)

#choose difficulty
print("\nChoose your difficulty:")
print("1. Easy")
print("2. Normal")
print("3. Hard")

difficulty = input("\nEnter choice: ")

if difficulty == "1":
    damage = 15
    computer_name = "Rookie Bot"

elif difficulty == "2":
    damage = 20
    computer_name = "Battle Bot"
else:
    damage = 25
    computer_name = "Master Bot"

print(f"\nYour Opponent is {computer_name}!")
time.sleep(1)

#game loop

while player_health > 0 and computer_health > 0:
    print("\n\t" + "=" *50)

    print(f"\t {player_name} @ Player Health/Total Percentage\n\t\t\t{player_health}/100")
    print(f"\t {computer_name} @ Computer Health/Total Percentage\n\t\t\t{computer_health}/100")
    print(f"\t Coins: {coins}")
    print(f"\t XP: {xp}")
    print(f"\t Streak: {streak}")

    print("\t" + "=" *50)

    print("\nChoose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Run away")

    player_choice = input("\nYour Choice: ")

    #run away
    if player_choice == "4":
        print("\n\t You escaped the arena!")
        print("\t FORFEIT!")
        print(f"\t {computer_name} automatically wins!!!")
        computer_health = 0
        player_health = 0
        break

    #validate the input
    if player_choice not in ["1", "2", "3"]:
        print("\nInvalid Choice")
        print("Choose 1, 2, or 3")
        continue
    player_move = choices[int(player_choice) -1]

    #computer choice
    computer_move = random.choice(choices)
    print("\nPreparing for Battle....")
    time.sleep(1)

    print(f"You chose: {player_move.upper()}")
    print(f"Computer chose: {computer_move.upper()}")
    time.sleep(1)

    #check result
    if player_move == computer_move:
        print("\n\t\tDRAW")
        print("\t\tNobody takes damage.")

        streak = 0

    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or
        (player_move == "scissors" and computer_move == "paper")
        ):

        #player wins
        print("\n\t\tYOU WIN THE ROUND!")

        #critical hit
        critical = random.randint(1,5)
        if critical == 5:
            attack_damage = damage + 15

            print("\t\tCRITICAL HIT!!!!!!")
            print(f"\t\tYou impact {attack_damage}% damage!")

        else:
            attack_damage = damage
            print(f"\t\tYou impact {attack_damage}% damage!")

        computer_health -= attack_damage
        coins +=10
        xp += 20
        streak += 1

        print("\t\t+10 coins")
        print("\t\t+20 XP")

        if streak >= 3:
            print("\n\t\tCOMBO STREAK!")
            print("\t\tBonus reward: +20 coins!")

            coins += 20

    else:
        print("\n\t\tCOMPUTER WINS THE ROUND!")
        attack_damage = damage

        #critical hit
        critical = random.randint(1, 5)
        if critical == 5:
            attack_damage +=15
            print("\t\tCOMPUTER CRITICAL HIT!")
        print(f"\t\t{computer_name} impacts {attack_damage}% damage!")
        player_health -=attack_damage
        streak = 0
    time.sleep(1)


#game results
print("\n\t\t" + "=" *50)
print("\t\t\t\tBATTLE OVER")
print("\t\t" + "=" *50)

if player_health <= 0:
    print(f"\n\t\t\t{player_name} has been defeated!")
    print("\t\t\tBetter luck next time!")

elif computer_health <= 0:
    print(f"\n\t\t\tVICTORY!")
    print(f"\t\t\t{player_name} defeated {computer_name}!")

    coins += 50
    xp += 100

    print("\n\t\t\tVICTORY REWARDS")
    print("\t\t\t+50 coins")
    print("\t\t\t+100 XP")
else:
    print("\n\t\t\tYou escaped the battle!")

#final stats
print("\n\t\t\tFINAL STATS")
print("\t\t\t" + "-" * 20)

print()
print(f"\t\t\tWarrior: {player_name}")
print(f"\t\t\tHealth: {max(player_health, 0)}")
print(f"\t\t\tCoins: {coins}")
print(f"\t\t\tXP: {xp}")

#determine level

level = (xp // 100) + 1
print(f"\t\t\tLevel: {level}")
print("\n\t\t\tThanks for playing!")






















        
    
    
    
