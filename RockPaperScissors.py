import random

user_score = 0
computer_score = 0
choices = ['Rock', 'Paper', 'Scissors']

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Rock, Paper, or Scissors? Choose one: ").strip().capitalize()
    
    if user_choice not in choices:
        print("You entered something wrong!")
    else:
        print(f"\nComputer chose {computer_choice}")
        if computer_choice == user_choice:
            print("It's a tie!")
        elif (computer_choice == 'Rock' and user_choice == 'Paper') or \
             (computer_choice == 'Paper' and user_choice == 'Scissors') or \
             (computer_choice == 'Scissors' and user_choice == 'Rock'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    
    play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
    if play_again != 'Y':
        print("-----------------------------------------")
        print(f"Total scores:\nYou: {user_score}\nComputer: {computer_score}")
        if user_score > computer_score:
            print("Congratulations! You win!")
        elif computer_score > user_score:
            print("Sorry, you lost!")
        else:
            print("It's a tie overall.")
        break