from encrypt import get_encrypt
import os

def readit(ifile):
    """
    Read the Password of a file
    """
    crypter = get_encrypt()
    path2 = "./purposes/Mail"
    dir_files2 = os.listdir(path2)
    direc = os.path.join("./purposes/Passwords",f"{ifile}.bin")
    direc2 = os.path.join("./purposes/Mail",f"{ifile}.bin")
    mail = False
    
    if (f"{ifile}.bin" in dir_files2):
        with open(direc2, "r") as f:
            text_mail = f.readline()
        with open(direc, "rb") as f:
            text = f.readline()
            mail = True
    else:
        with open(direc, "rb") as f:
            text = f.readline()
            mail = False
    try:
        decryptString = crypter.decrypt(text)
        message = (str(decryptString, "utf8"))
        if mail == True:
            print("The Pa$$w0rd and Mail are:")
            print(f"Pa$$word: {message} \t||\t Mail: {text_mail}")
        else:
            print("The Pa$$w0rd is:")
            print(f"\t{message}")
    except:
        pass