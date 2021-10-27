# Quick Instructions into this Password-Generator/Manager
This was a small project to see and test what i am able to do with my current python knowledge.
It is not a high end lvl of security. Be aware that if you stream or show people your key and then your encrypted Passwords, they will easily be able to rebuild this
Password-Generator/Manager and decrypt those passwords.


# Installation:
## Installation - Methode 1
First Installation Methode is by simple Installing the Release Packages.
Dont forget to install python and pip so you can even install and use the terminal program.

## Installation - Methode 2
Second Installation Methode is by copying the https link going into a folder. Then opening the Cmd and typing:
>git clone https://github.com/Merrixx/Password-Generator-Manager.git


### Installing the needed Packages for the program.
After you have the Program installed you have to open the directory in a Cmd and type the following Command:

- Installing the required Libaries
>pip install -r requirements.txt

- From now on you can execute the program in the Cmd by typing following Command.
>python main.py



# Now about the functionality
- Option 1:                                                                                                                           
You can generate random Passwords in any amount you want. Those will not be saved since they are just randomly generated and just for the sake of copy pasting.

- Option 2:                                                                                                                             
It Generates you a Password and then prompts for you to enter a Purpose, which is suppose to be the reason for you to save the Password. You can also choose if you want to input an email which will be saved aswell and shown on prompt. After you do so it will create a .bin file in the purpose directory and will call it the "purpose" given earlier.
Dont worry those Passwords will be shown in ecrypted version.

- Option_3:
Before you are able to get the Password from the program it will ask you for a purpose to input. If it finds a Password associating to that purpose it will return your Password. If an Email was give that one will be output aswell.

- Option 4:                                             
By Choosing Option 3 the program will return your currently saved Passwords. If an Email is given along with a Password the Program will tell you that aswell.



# Small Reminder
This wont be one of my biggest projects ever but i will change things from time to time. Please create a backup of your "methode.bin" since that file saves your key.
The program calls a function every startup, so if your methode.bin is not allready existing it will create a NEW one.