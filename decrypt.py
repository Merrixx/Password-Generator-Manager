from encrypt import get_encrypt
import os

def readit(ifile):
    """
    Read the Password of a file
    """
    crypter = get_encrypt()
    direc = os.path.join("./purposes/Passwords",f"{ifile}.bin")
    direc2 = os.path.join("./purposes/Mail",f"{ifile}.bin")
    print(direc2)
    # if (f"{ifile}" in direc2):
    #     print("It is included")
    #     with open(direc2, "r") as f:
    #         text2 = f.readline()
    print("Without 2nd file")
    with open(direc, "rb") as f:
        text = f.readline()
    try:
        decryptString = crypter.decrypt(text)
        message = (str(decryptString, "utf8"))
        # if text2:
        #     print("The Pa$$w0rd and Mail are:")
        #     print(f"Pa$$word: {message} \t||\t Mail: {text2}")
        #else:
        print("The Pa$$w0rd is:")
        print(f"\t{message}")
    except:
        pass