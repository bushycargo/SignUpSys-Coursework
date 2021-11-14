#Josep Haines
#14/11/2021
#Coursework Login System

import csv
import ast
import hashlib as hal

def main():
    try:
        csvData = getData(input("Enter your username: "))
    except:
        print("Incorrect Username")
        exit()
    if passwordHashing(input("Enter your password: "), ast.literal_eval(csvData[1])) == ast.literal_eval(csvData[0]):
        print("Correct Password, Login Accepted")
    else:
        print("Incorrect Password, Login Denied")

def getData(username):
    intUserIndex = None
    csvUsernames = []
    csvSalts = []
    csvKeys = []
    with open("users.csv") as data:
        csvDictReader = csv.DictReader(data)
        for row in csvDictReader:
            csvUsernames.append(row['username'])
            csvSalts.append(row['salt'])
            csvKeys.append(row['key'])

        intUserIndex = csvUsernames.index(username)

        return csvKeys[intUserIndex], csvSalts[intUserIndex]

def passwordHashing(strPswd, pswdSalt): #Almost indentical from my sign up system except it doesnt generate the salt
	return hal.pbkdf2_hmac('sha256',strPswd.encode('utf-8'), pswdSalt, 100000)

main()
