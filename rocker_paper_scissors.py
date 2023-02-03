import random

def get_computer_choice():
    choices = ['Pierre', 'Papier', 'Ciseaux']
    return random.choice(choices)

def play_round(player_selection, computer_selection):
    if (player_selection == computer_selection):
        print(f"Les deux sélectionnés {player_selection}. C'est un match nul.")
        return 0
    elif (player_selection == "Pierre" and computer_selection == "Ciseaux" or 
         player_selection == "Papier" and computer_selection == "Pierre" or 
         player_selection == "Ciseaux" and computer_selection == "Papier"):
        print(f"{player_selection} bat  {computer_selection} \nFélicitations Vous avez gagné !" )
        return 1
    else:
        print(f"{computer_selection} bat {player_selection} \nTu as perdu !")
        return -1

def game():
    player_score = 0
    computer_score = 0

    for i in range(5):
        player_selection = input("\nFaites votre choix, 'Pierre', 'Papier' ou 'Ciseaux' : ")
        computer_selection = get_computer_choice()

        result = play_round(player_selection, computer_selection)

        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

    if player_score > computer_score:
        print(f"\nScore final : {player_score} - {computer_score}. Vous avez gagné la partie !")
    elif player_score < computer_score:
        print(f"\nScore final : {player_score} - {computer_score}. Vous avez perdu la partie !")
    else:
        print(f"\nScore final : {player_score} - {computer_score}. Le jeu est nul !")

game()