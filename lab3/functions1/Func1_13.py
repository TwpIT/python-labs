from random import randint

def game():
    player = {
        "name" : None, 
        "number" : None,
        "guesses": 1
    }
    player["name"] = input("Hello! What is your name?\n")
    player["number"] = int(input(f"\nWell, {player['name']}, I am thinking of a number between 1 and 20. \nTake a guess.\n"))
    guess_number = randint(1, 20)
    while player["number"] != guess_number:
        player["number"] = int(input("\nYour guess is too low.\nTake a guess.\n")) if player["number"] < guess_number else int(input("\nYour guess is too hight.\nTake a guess.\n"))
        player["guesses"]+=1
    print(f"\nGood job, {player['name']}! You guessed my number in {player['guesses']} guesses!")

if __name__ == "__main__":
    game()


    