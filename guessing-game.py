def main():
    print("Python guessing game")

    animal ="tiger"

    while True:
        print("The program is thinking of an animal")
        guess = input("Guess the name of the animal: ")
        if guess == animal:
            print("That is correct!")
            break
        else:
            print("Wrong animal, guess again")

main()