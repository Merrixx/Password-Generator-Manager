from encrypt import get_encrypt
import os

def savethis(purpose, to_save, email=""):
    """
    Saves Passwords as a File:
    """
    if email:
        direcmail = os.path.join("./purposes/Mail",f"{purpose}.bin")
        with open(direcmail, "w") as f:
            f.write(email)
            f.close()
        print(f"\n\t-Email saved!")

    crypter = get_encrypt()
    save_it = to_save.encode("utf-8")
    crypto_save = crypter.encrypt(save_it)
    direc = os.path.join("./purposes/Passwords",f"{purpose}.bin")

    with open(direc, "wb") as f:
        f.write(crypto_save)
        f.close()
    print(f"\t-Pa$$w0rd saved!")