def main():
    print("Python guessing game")

    animal ="tiger"

    while True:
        print("The program is thinking of an animal")
        print("If at any time you would like to quit, type 'quit' ")
        guess = input("Guess the name of the animal: ").lower()
        if guess == animal:
            print("That is correct!")
            print("Thanks for playing")
            break
        elif guess == 'quit':
            print("Thanks for playing")
            break
        else:
            print("Wrong animal, guess again")

main()