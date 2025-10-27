#  write a programm to guess a number which is hidden in the code we just have to give only 5 cahance to guess

import random

def play_game(max_chances = 5):
    guessed_number = random.randint(0,20)
    chances = max_chances

    print(f"You have {chances} chances to guess the number between 0 to 20.")

    while chances > 0:
        try:
            user_input = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        chances -= 1

        if user_input == guessed_number:
            used = max_chances - chances
            print("Congratulations! You guessed the correct number.")
            
            if used == 1:
                print(f"You took {used} chance to guess the correct number.")
            else:
                print(f"You took {used} chances to guess the correct number.")
                
            return True

        if user_input > guessed_number:
            print("Guess a lesser number.")
        else:
            print("Guess a greater number.")

        if chances > 0:
            print(f"You have {chances} remaining {'chance' if chances == 1 else 'chances'} to guess the number.")
        else:
            print("Game Over! The correct number was:", guessed_number)
            return False

if __name__ == "__main__":
    play_game()
