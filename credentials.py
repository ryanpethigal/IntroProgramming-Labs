# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Ryan Pethigal
# Created: 2020-04-09
def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first + "." + last
    # ask user to create a new password
    def password():
        passwd = input("Create a new password: ")
        while True:
            if len(passwd) < 8:
                print("Fool of a Took! That password is feeble! ")
                password()
            elif len(passwd) >= 8:
                print("The force is strong in this one...")
            break
    password()

    print("Account configured. Your new email address is", uname + "@marist.edu")
main()