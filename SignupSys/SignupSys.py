#Josep Haines
#10-11-2021 - 11-11-2021
#Coursework Sign Up System

import os
import csv
import hashlib as hal

def main():
    #Declairing Variables
    strSalt = None
    strUsername = None
    strPassword = None

    print("Sign up system")
    strUsername = input("Enter username: ") #Takes in username
    while strPassword == None: #While there is no password stored loop
       strPassword = enterPassword()
    strPassword = passwordHashing(strPassword) #Hashes the password and returns the key and salt
    strSalt = str(strPassword[0]) #Extracts the salt from the previous output
    strPassword = str(strPassword[1]) #Extracts the key from previous output
    writeFile(strUsername, strPassword, strSalt) #Writes to CSV file

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
    return pswdSalt, key #Returns salt and key

def writeFile(username, key, salt):
    if not os.path.isfile('users.csv'):#If the file doesn't exist run
        csvUsers = open('users.csv', 'w') #Creates the file
        csvWriter = csv.DictWriter(csvUsers, fieldnames=['username','key','salt']) #Creates a csv writer
        csvWriter.writeheader() #Writes the headers: username, key and salt
        csvUsers.close() #Closes the file

    csvUsers = open('users.csv', 'a') #Opens the file with append
    csvWriter = csv.DictWriter(csvUsers, fieldnames=['username','key','salt']) #Recreates the writer
    csvWriter.writerow({'username': username, 'key': key, 'salt': salt}) #Appends the data
    csvUsers.close() #Closes the file :)

main()
