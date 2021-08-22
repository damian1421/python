import getpass
import os

#Define 'clear' command
clear = lambda: os.system('clear')

#Asks for user / pass combination
clear()
print ("[Login] Verifying user for "+"PROGRAM NAME"+"...")
user = input("Username: ")
password = getpass.getpass("Password: ")

#Dictionary of users
users = {"l0gg3r":"password1","invitado":"password2"}
if user in users and password == users.get(user):
    clear()
    print("Welcome "+user+"!")
    #else: #Not working statement when user-pass is wrong, fix it!
    #    print("[NG] Alert intruder!  ",user)
