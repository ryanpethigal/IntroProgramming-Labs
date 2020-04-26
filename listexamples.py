colors= ["RED","ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET"]

def showTitle():
    print("Colour Preference Evaluator")

def promptForColor():
    myCol = input("Enter color name: ")
    return myCol.strip().upper()

def confirmColor(myCol):
    pick = input("Your color is " + myCol + " Is this color correct? Enter 'Y' or 'N': ")
    return pick == 'Y'

def containsElement(myCol):
    for any in colors:
        if any == myCol:
            return True
    return False

def praiseUser():
    print("That was a good guess ")

def ridiculeUser():
    print("Wrong answer, try again please")

def main():
    myCol = ""
    showTitle()
    while 1:
        myCol = promptForColor()
        if confirmColor(myCol):
            break
    if containsElement(myCol):
        praiseUser()
    else:
        ridiculeUser()

main()