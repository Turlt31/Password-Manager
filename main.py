import time
import os
import colorama
from colorama import Fore, Style
import sys

colorama.init(autoreset=True)

def main():
	global tries
	f = open("backupPasswords.txt", "r")
	masterPassword = input(f"{Fore.GREEN}Master Password: ")
	if masterPassword == decrypt3(f.readline()):
		osCLS()
		drawLogo()
		print(f"{Fore.GREEN}Please wait Loading...")
		time.sleep(2)
		osCLS()
		options()
	else:
		os.system("cls")
		print(f"{Fore.RED}Incorect Password, tries left: {tries}")
		if tries == 0:
			time.sleep(1)
			osCLS()
			exit()
		tries -= 1
		main()
	f.close()

def decrypt1(name, email, password):
	dencryptedN = ""
	dencryptedE = ""
	dencryptedP = ""

	for letter in name:
		if letter == ' ':
			dencryptedN += ' '
		else:
			dencryptedN += chr(ord(letter) - 5)

	for letter in email:
		if letter == ' ':
			dencryptedE += ' '
		else:
			dencryptedE += chr(ord(letter) - 5)

	for letter in password:
		if letter == ' ':
			dencryptedP += ' '
		else:
			dencryptedP += chr(ord(letter) - 5)

	if any(c in "@" for c in dencryptedE): 
		print(f"{Fore.RED}Name: {dencryptedN}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Email: {dencryptedE}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Password: {dencryptedP}")
		time.sleep(0.2)
	else:
		print(f"{Fore.RED}Name: {dencryptedN}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Username: {dencryptedE}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Password: {dencryptedP}")
		time.sleep(0.2)

def decrypt2(name, email, password, findName):
	global count
	dencryptedN = ""
	dencryptedE = ""
	dencryptedP = ""
	
	for letter in name:
		if letter == ' ':
			dencryptedN += ' '
		else:
			dencryptedN += chr(ord(letter) - 5)

	for letter in email:
		if letter == ' ':
			dencryptedE += ' '
		else:
			dencryptedE += chr(ord(letter) - 5)

	for letter in password:
		if letter == ' ':
			dencryptedP += ' '
		else:
			dencryptedP += chr(ord(letter) - 5)

	if findName == dencryptedN:
		print(f"{Fore.GREEN}Email: {dencryptedE}, Password: {dencryptedP}")
		count += 1

def decrypt3(password):
	dencryptedP = ""

	for letter in password:
		if letter == ' ':
			dencryptedP += ' '
		else:
			dencryptedP += chr(ord(letter) - 5)

	return dencryptedP

def addAcc():
	f = open("passwords.txt", "a")
	n = input("Enter website Name: ")
	e = input("Enter Email/Username: ")
	p = input("Enter Password: ")
	print()

	encryptedN = ""
	encryptedE = ""
	encryptedP = ""
	for letter in n:
		if letter == ' ':
			encryptedN += ' '
		else:
			encryptedN += chr(ord(letter) + 5)

	for letter in e:
		if letter == ' ':
			encryptedE += ' '
		else:
			encryptedE += chr(ord(letter) + 5)

	for letter in p:
		if letter == ' ':
			encryptedP += ' '
		else:
			encryptedP += chr(ord(letter) + 5)

	f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
	if any(c in "@" for c in e): 
		print(f"{Fore.MAGENTA}Added Name: {n}, Email: {e}, Password: {p}")
	else:
		print(f"{Fore.MAGENTA}Added Name: {n}, Username: {e}, Password: {p}")
	f.close()
	print()
	input("press ENTER to continue")
	osCLS()
	options()

def showAcc():
	f = open("passwords.txt", "r")
	count = 0
	print(f"{Fore.MAGENTA}====================")
	print()
	for line in f:
		entityList = line.split(',')
		decrypt1(entityList[0], entityList[1], entityList[2])
		count += 1
		
	print()
	print(f"{Fore.MAGENTA}====================")
	print()
	print(f"There are {count} Acccounts")
	print()
	input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
	osCLS()
	options()
		
def findAcc():
	global count
	n = input("Enter Name: ")
	f = open("passwords.txt", "r")

	print(f"{Fore.MAGENTA}====================")
	print()

	for line in f:
		entityList = line.split(',')
		decrypt2(entityList[0], entityList[1], entityList[2], n)
		time.sleep(0.2)

	if count != 0:
		print()
		print(f"{Fore.MAGENTA}====================")
		print()
		print(f"Found {count} Acccounts")
		print()
	else:
		print(f"No Acccounts were found with the Name: {n}")
		print()

	input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
	osCLS()
	options()

def clear():
	sure = input("Are you sure? ")
	if sure == "yes" or sure == "Yes" or sure == "Y" or sure == "y":
		f = open("passwords.txt", "w")
		f.close()
		print()
		print("Cleared all Account")
		print()
		print(f"{Fore.MAGENTA}====================")
		print()
		input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
		osCLS()
		options()
	else:
		print()
		print("Okay")
		time.sleep(1.5)
		osCLS()
		options()

def changePassword():
	f = open("backupPasswords.txt", "w")
	p = input(f"Enter new Password: ")

	encryptedP = ""

	for letter in p:
		if letter == ' ':
			encryptedP += ' '
		else:
			encryptedP += chr(ord(letter) + 5)

	f.write(encryptedP)
	print(f"Changed your Master Password to: {p}")
	f.close()
	print()
	input("press ENTER to continue")
	osCLS()
	options()

def logOut():
	osCLS()
	main()

def options():
	print('''
 1. Add Acccount 	6. Change Master Password
 2. Show Accounts	7. Log Out
 3. Find Acccount	9. Exit
 4. Clear Accounts
 5. Clear Screen
		''')
	choice = input(f"Enter option: {Fore.RED}")
	if choice == "1":
		print()
		addAcc()
	elif choice == "2":
		print()
		showAcc()
	elif choice == "3":
		print()
		findAcc()
	elif choice == "4":
		print()
		clear()
	elif choice == "5":
		time = int(input("How Long would you like to clear the screen: "))
		osCLS()
		time.sleep(int(time))
		options()
	elif choice == "6":
		print()
		changePassword()
	elif choice == "7":
		print()
		logOut()
	elif choice == "9":
		osCLS()
		exit()
	else:
		print()
		print(f"{Fore.RED}Incorect Option")
		time.sleep(1.5)
		osCLS()
		options()

def drawLogo():
	logo = '''
									+-----------------------+
									+	 Welcome        +
									+         Erikas        +
									+      Root Granted     +
									+-----------------------+
			'''
	print(f"{Fore.GREEN}{logo}")

def osCLS():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

tries = 5
count = 0
osCLS()
main()
