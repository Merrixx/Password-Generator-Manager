from cryptography.fernet import Fernet
import subprocess 
import os

def get_encrypt():
    """
    Creates or returns the key
    """
    try:
        direc = os.path.join("./methode","methode.bin")
        with open(direc, "rb") as f:
            key = f.readline()
            f.close()
        crypter = Fernet(key)
        return crypter
    except:
        key = get_key()
        direc = os.path.join("./methode","methode.bin")
        with open(direc, "wb") as f:
            f.write(key)
            f.close()
        print(f"\n-Key has been generated!-")


def get_key():
    """
    Function for creating the key
    """
    key = Fernet.generate_key()
    return key