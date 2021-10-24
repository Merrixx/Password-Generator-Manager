# Quick Instructions into this Password-Generator/Manager
This was a small project to see and test what i am able to do with my current python knowledge.
It is not a high end lvl of security. Be aware that if you stream or show people your key and then your encrypted Passwords, they will easily be able to rebuild this
Password-Generator/Manager and decrypt those passwords.


# Usability
## After installing you need to go into the Directory and open a Terminal
Right after that you need to type following Command into your Terminal. Which will install the needed Libaries for this Programm.
>pip install -r requirements.txt

Execute the Programm in the Terminal with following Command.
>python main.py


# Now about the functionality
- Option 1:                                                                                                                           
	You can generate random Passwords in any amount you want. Those will not be saved since they are just randomly generated and just for the purpose of copy pasting.

- Option 2:                                                                                                                             
	It Generates you a Password and then prompts for you to enter a Purpose aka (What to save it for). After you do so it will create a .bin file in the purpose directory and will call it the "purpose" given earlier.
	Dont worry those Passwords will be shown in ecrypted version. Just remember dont stream those.

- Option_3:                                                                                                                           
	Choosing Option 3 you will be able to recieve your previous saved Passwords. Only works if existing.

- Option 4:                                                                                                                           
	Just prints you all the currently purposes you saved the Passwords for.



# Small Reminder
This wont be one of my biggest projects ever but i will change things from time to time. Please create a backup of your "methode.bin" since that file saves your key.
The programm calls a function every bootup, so if your methode.bin is not allready existing it will create a NEW one.