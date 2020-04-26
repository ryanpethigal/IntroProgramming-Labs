def main():
    print("Python guessing game")

    animal ="tiger"

    while True:
        print("The program is thinking of an animal")
        print("If at any time you would like to quit, type 'quit' ")
        guess = input("Guess the name of the animal: ").lower()
        if guess == animal:
            print("That is correct!")
            answer = input("Do you like this animal? If yes, Type 'y', if no, type 'n': ").lower()
            if answer == "y":
                print("I also like tigers!")
            else:
                print("You should like tigers! They are very cool!")
            print("Thanks for playing")
            break
        elif guess[0] == 'q':
            print("Thanks for playing")
            break
        else:
            print("Wrong animal, guess again")

main()