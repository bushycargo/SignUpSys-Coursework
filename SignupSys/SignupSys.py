#Josep Haines
#10-11-2021
#Coursework Sign Up System

import os
import json
import hashlib as hal

def main():
    #Declairing Variables
    strSalt = None
    strUsername = None
    strPassword = None
    jsonUsers = {}
    jsonUsers['users'] = []

    print("Sign up system")
    strUsername = input("Enter username: ") #Takes in username
    while strPassword == None: #While there is no password stored loop
       strPassword = enterPassword()
    strPassword = passwordHashing(strPassword)
    strSalt = str(strPassword[0])
    strPassword = str(strPassword[1])
    jsonUsers['users'].append({
        'username': strUsername,
        'salt': strSalt,
        'password': strPassword
    })
    with open ('users.json', 'w') as output:
        json.dump(jsonUsers, output, indent=4)

def enterPassword():
    strPswd = input("Enter password: ") #Enter a password and store to temp var
    if strPswd == input("Confirm password: "): #Check temp var against new inport
        return strPswd #If both match return it
    else: #Else return no password
        print("Passwords do not match")
        return None

def passwordHashing(strPswd):
    pswdSalt = os.urandom(16) #Generate 16 char salt
    key = hal.pbkdf2_hmac('sha256',strPswd.encode('utf-8'), pswdSalt, 100000) #Hashing password
    return pswdSalt, key #Combining password and salt for output, when verifying seperate first 16 chars for the salt

main()
