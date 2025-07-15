import random

def number_guessing_game():
    number_to_guess=random.randint(1,100)
    print(number_to_guess)
    attempts=0
    print("Welcom to the number guess Game")
    print("I'am thinking  of a number between 1 and 100\n")

    while True:
        try:
            guess=int(input("Enter your Guess.\n"))
            attempts+=1

            if guess<number_to_guess:
                print("too low!Try again\n")
            elif guess>number_to_guess:
                print("Too high!Try again")
            else:
                print(f"Congratulation !You guess it in {attempts} attempts")
                break
        except ValueError:
            print("Please Enter a valid number")

number_guessing_game()