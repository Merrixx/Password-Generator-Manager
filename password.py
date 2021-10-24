import random

#Possible Characters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
specials = ["!", "§", "%", "&", "?", "#", "*", "+"]


def generate_passwords(amount):
    """
    Creates multiple Passwords
    """
    amount = int(amount)
    while amount > 1:
        generate_password()
        amount -= 1

def generate_password(saving_for=""):
    """
    Creates one Password
    """

    #Values
    length = 0
    passwd = ""

    #Loop
    while length != 16:
        append = get_next()
        passwd = f"{passwd}{append}"
        length += 1
    if saving_for:
        return passwd
    else:
        print("\t  " + passwd)
        
def get_next():
    """
    Choose the Character
    """
    i = random.randint(1,4)

    #Check for the Character selected
    if i == 1 or i == 4:
        #Letter Character Case
        next_letter = letter()
        return next_letter
    elif i == 2:
        #Special Character Case
        next_letter = special()
        return next_letter
    elif i == 3:
        #Number Character Case
        next_letter = number()
        return next_letter

def roll(data):
    """
    Get the Character
    """
    database = int(len(data))
    cur = random.randint(1, database)
    if data[1] == int:
        character = data[cur - 1]
        return character
    else:
        character = data[cur - 1]
        return character

def cap_or_not(cur):
    """
    Randomizes for Capital or not
    """
    if cur == 1:
        char = roll(letters)
        return char
    elif cur == 2:
        char = roll(letters)
        char = str(char)
        char = char.upper()
        return char

def letter():
    """
    Case for letter
    """
    cur = random.randint(1,2)
    appending = cap_or_not(cur)
    return appending

#Case for special
def special():
    """
    Case for special
    """
    char = roll(specials)
    return char

#Case for number
def number():
    """
    Case for number
    """
    char = roll(numbers)
    return char