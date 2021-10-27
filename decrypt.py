from encrypt import get_encrypt
import os

def readit(ifile):
    """
    Read the Password of a file
    """
    crypter = get_encrypt()
    direc = os.path.join("./purposes/Passwords",f"{ifile}.bin")
    dir_files2 = os.listdir("./purposes/Mail")
    dir_mail = os.path.join("./purposes/Mail",f"{ifile}.bin")
    mail = False
    
    if (f"{ifile}.bin" in dir_files2):
        """
        Check if an email is included
        """
        with open(dir_mail, "r") as f:
            text_mail = f.readline()
        with open(direc, "rb") as f:
            text = f.readline()
            mail = True
    else:
        """
        If not mail stays False
        """
        with open(direc, "rb") as f:
            text = f.readline()
            mail = False
    try:
        """
        Output depending on the mail value
        """
        decryptString = crypter.decrypt(text)
        message = (str(decryptString, "utf8"))
        
        if mail == True:
            print(" - The Pa$$w0rd and Mail are:")
            print(f"\t - Pa$$word: {message}\n"
                  f"\t - Mail: {text_mail}")
        else:
            print(" - The Pa$$w0rd is:")
            print(f"\t - Pa$$w0rd: {message}")
    except:
        pass