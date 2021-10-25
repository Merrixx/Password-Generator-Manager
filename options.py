from password import *
from save import *
from decrypt import *
from logo.ascii import *
import os


def give_options():
    """
    Gives Possible Options:
    """
    print(
          "\n"
          "  1. ... Generate random Pa$$w0rd\n"
          "  2. ... Save A Pa$$w0rd for your Purpose\n"
          "  3. ... Get a Pa$$w0rd from key\n"
          "  4. ... Show Possible Pa$$w0rd's\n"
          "  5. ... Leave Programm\n"
          )

def keep_going():
    """
    Prompts to continue the Program
    """
    print("\n\n\n __________")
    continues = input("  Continue: ")

def main_screen():
    """
    Keeps the Screen clean
    """
    os.system("cls" if os.name == "nt" else "clear")
    print(show_ascii)

def create_value():
    """
    Creates key if not allready existing:
    """
    get_encrypt()

def get_choice():
    """
    Prompts for User input:
    """
    choice = input("Choose Option: ")
    try:
        choice = int(choice)
        if choice == 1:
            amount = input("Amount [default:1]")
            print("\n   Generated Password's are: ")
            if amount:
                generate_passwords(amount)
            generate_password()

        elif choice == 2:
            try:
                purpose = input("-What do you want to save it for: ")
                if purpose == "":
                    print("Choose a Valid Name")
                    return False
                
                question = input("-Do you want to Enter a Email aswell: [yes/no] ")
                if (question == "yes") or (question == ""):
                    mail = input("Enter your Mail: ")
                    to_save = generate_password(purpose)
                    savethis(purpose, to_save, email=mail)
                else: 
                    to_save = generate_password(purpose)
                    savethis(purpose, to_save)
                print(f"\tPa$$w0rd created: {to_save}")
            except:
                print("Choose a Valid Name")

        elif choice == 3:
            purpose = input("From where do you want to call the Pa$$w0rd: ")
            try:
                readit(purpose)
            except:
                print("\tERROR ACCURED\nPlease input existing file!")
            pass

        elif choice == 4:
            path = "./purposes/Passwords"
            path2 = "./purposes/Mail"
            dir_files = os.listdir(path)
            dir_files2 = os.listdir(path2)
            print("\nYou saved Pa$$w0rd's for:")
            for files in dir_files:
                if files == "Description.md":
                    continue
                
                
                if files in dir_files2:
                    files = files.replace(".bin","")
                    print(f"\t-{files} -- [EMAIL-INCLUDED]") 
                else:
                    files = files.replace(".bin","")
                    print(f"\t-{files}")

        elif choice == 5:
            os.system("cls" if os.name == "nt" else "clear")
            exit()
    except ValueError:
        print("\n\tERROR USE A VALID NUMBER")