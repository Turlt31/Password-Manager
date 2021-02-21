import time
import os
import colorama
from colorama import Fore, Style
import sys

colorama.init(autoreset=True)

class password:

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

	def addAcc():
		f = open("passwords.txt", "a")
		n = input("Enter website Name: ")
		e = input("Enter Email/Username: ")
		p = input("Enter Password: ")
		print()
		if n == "cancel" or e == "cancel" or p == "cancel":
			password.osCLS()
			password.options()

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
		password.osCLS()
		password.options()

	def showAcc():
		f = open("passwords.txt", "r")
		count = 0
		print(f"{Fore.MAGENTA}====================")
		print()
		for line in f:
			entityList = line.split(',')
			password.decrypt1(entityList[0], entityList[1], entityList[2])
			count += 1
			
		f.close()
		print()
		print(f"{Fore.MAGENTA}====================")
		print()
		print(f"There are {count} Acccounts")
		print()
		input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
		password.osCLS()
		password.options()
			
	def findAcc():
		global count
		n = input("Enter Name: ")
		f = open("passwords.txt", "r")

		print(f"{Fore.MAGENTA}====================")
		print()

		for line in f:
			entityList = line.split(',')
			password.decrypt2(entityList[0], entityList[1], entityList[2], n)
			time.sleep(0.2)

		if count == 0:
			print(f"No Acccounts were found with the Name: {n}")
		else:
			print()
			print(f"{Fore.MAGENTA}====================")
			print()
			print(f"Found {count} Acccounts")

		f.close()
		print()
		input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
		password.osCLS()
		password.options()

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
			password.osCLS()
			password.options()
		else:
			print()
			print("Okay")
			time.sleep(1.5)
			password.osCLS()
			password.options()

	def logOut():
		password.osCLS()
		Main.main()

	def options():
		print('''
 1. Add Acccount 	5. Go Back
 2. Show Accounts	6. Log Out
 3. Find Acccount	9. Exit
 4. Clear Accounts
			''')
		choice = input(f"Enter option: {Fore.RED}")
		if choice == "1":
			print()
			password.addAcc()
		elif choice == "2":
			print()
			password.showAcc()
		elif choice == "3":
			print()
			password.findAcc()
		elif choice == "4":
			print()
			password.clear()
		elif choice == "5":
			print()
			password.osCLS()
			Main.options()
		elif choice == "6":
			print()
			password.logOut()
		elif choice == "9":
			password.osCLS()
			exit()
		else:
			print()
			print(f"{Fore.RED}Incorect Option")
			time.sleep(1.5)
			password.osCLS()
			password.options()

	def osCLS():
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

class creditcard:

	def osCLS():
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

	def options():
		print('''
 1. Add Card 	 4. Log Out	
 2. Show Cards	 5. Go Back
 3. Clear Cards  9. Exit   
			''')
		choice = input(f"Enter option: {Fore.RED}")
		if choice == "1":
			print()
			creditcard.addCard()
		elif choice == "2":
			print()
			creditcard.showCards()
		elif choice == "3":
			print()
			creditcard.clear()
		elif choice == "4":
			print()
			creditcard.logOut()
		elif choice == "5":
			print()
			creditcard.osCLS()
			Main.options()
		elif choice == "9":
			creditcard.osCLS()
			exit()
		else:
			print()
			print(f"{Fore.RED}Incorect Option")
			time.sleep(1.5)
			creditcard.osCLS()
			creditcard.options()

	def addCard():
		f = open("card.txt", "a")
		n = input("Enter the Name on Card: ")
		N = input("Enter the Card Number: ")
		print("Use this format: mm/yyyy")
		d = input("Enter the expiration date: ")
		csv = input("Enter the csv: ")

		if n == "cancel" or N == "cancel" or d == "cancel" or csv == "cancel":
			password.osCLS()
			password.options()

		encryptedN = ""
		encryptedNN = ""
		encryptedD = ""
		encryptedcsv = ""

		for letter in n:
			if letter == ' ':
				encryptedN += ' '
			else:
				encryptedN += chr(ord(letter) + 5)

		for letter in N:
			if letter == ' ':
				encryptedNN += ' '
			else:
				encryptedNN += chr(ord(letter) + 5)

		for letter in d:
			if letter == ' ':
				encryptedD += ' '
			else:
				encryptedD += chr(ord(letter) + 5)

		for letter in csv:
			if letter == ' ':
				encryptedcsv += ' '
			else:
				encryptedcsv += chr(ord(letter) + 5)

		f.write(encryptedN + ',' + encryptedNN + ',' + encryptedD + ',' + encryptedcsv + ', \n')
		print(f"{Fore.MAGENTA}Added Name: {n}, Date: {d}, csv: {csv}, number: {N}")
		f.close()
		print()
		input("press ENTER to continue")
		creditcard.osCLS()
		creditcard.options()

	def decrypt1(name, number, date, csv):
		dencryptedN = ""
		dencryptedNN = ""
		dencryptedD = ""
		dencryptedcsv = ""

		for letter in name:
			if letter == ' ':
				dencryptedN += ' '
			else:
				dencryptedN += chr(ord(letter) - 5)

		for letter in number:
			if letter == ' ':
				dencryptedNN += ' '
			else:
				dencryptedNN += chr(ord(letter) - 5)

		for letter in date:
			if letter == ' ':
				dencryptedD += ' '
			else:
				dencryptedD += chr(ord(letter) - 5)

		for letter in csv:
			if letter == ' ':
				dencryptedcsv += ' '
			else:
				dencryptedcsv += chr(ord(letter) - 5)

		print(f"{Fore.RED}Name: {dencryptedN}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Card Number: {dencryptedNN}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	Date: {dencryptedD}")
		time.sleep(0.2)
		print(f"{Fore.GREEN}	csv: {dencryptedcsv}")

	def showCards():
		f = open("card.txt", "r")
		count = 0
		print(f"{Fore.MAGENTA}====================")
		print()
		for line in f:
			entityList = line.split(',')
			creditcard.decrypt1(entityList[0], entityList[1], entityList[2], entityList[3])
			count += 1
			
		f.close()
		print()
		print(f"{Fore.MAGENTA}====================")
		print()
		print(f"There are {count} Cards")
		print()
		input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
		creditcard.osCLS()
		creditcard.options()

	def clear():
		sure = input("Are you sure? ")
		if sure == "yes" or sure == "Yes" or sure == "Y" or sure == "y":
			f = open("card.txt", "w")
			f.close()
			print()
			print("Cleared all Cards")
			print()
			print(f"{Fore.MAGENTA}====================")
			print()
			input(f"press {Style.BRIGHT}ENTER{Style.NORMAL} to continue")
			creditcard.osCLS()
			creditcard.options()
		else:
			print()
			print("Okay")
			time.sleep(1.5)
			creditcard.osCLS()
			creditcard.options()

	def logOut():
		creditcard.osCLS()
		Main.main()

class Main:

	def main():
		global tries
		f = open("backupPasswords.txt", "r")
		masterPassword = input(f"{Fore.GREEN}Master Password: ")
		if masterPassword == Main.decrypt3(f.readline()):
			Main.osCLS()
			Main.drawLogo()
			print(f"{Fore.GREEN}Please wait Loading...")
			time.sleep(2)
			Main.osCLS()
			Main.options()
		else:
			Main.osCLS()
			print(f"{Fore.RED}Incorect Password, tries left: {tries}")
			if tries == 0:
				time.sleep(1)
				Main.osCLS()
				exit()
			tries -= 1
			Main.main()
		f.close()

	def decrypt3(password):
		dencryptedP = ""

		for letter in password:
			if letter == ' ':
				dencryptedP += ' '
			else:
				dencryptedP += chr(ord(letter) - 5)

		return dencryptedP

	def osCLS():
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

	def drawLogo():
		logo = '''
									+-----------------------+
									+	 Welcome        +
									+         Erikas        +
									+      Root Granted     +
									+-----------------------+
				'''
		print(f"{Fore.GREEN}{logo}")

	def changePassword():
		f = open("backupPasswords.txt", "r")
		op = input("Enter old password: ")
		

		if op == Main.decrypt3(f.readline()):
			np = input(f"Enter new Password: ")
			f = open("backupPasswords.txt", "w")
			encryptedP = ""

			for letter in np:
				if letter == ' ':
					encryptedP += ' '
				else:
					encryptedP += chr(ord(letter) + 5)

			f.write(encryptedP)
			print(f"Changed your Master Password to: {np}")
			f.close()
			print()
			input("press ENTER to continue")
			Main.osCLS()
			Main.options()
		else:
			print()
			print(f"{Fore.RED}Incorect old Password")
			print()
			input("press ENTER to continue")
			Main.osCLS()
			Main.options()

	def options():
		print('''
 1. Password Manager	 	 4. Log out
 2. Credit Card Manager		 9. Exit
 3. Change Master Password
			''')
		choice = input(f"Enter option: {Fore.RED}")
		if choice == '1':
			print()
			Main.osCLS()
			password.options()
		elif choice == '2':
			print()
			Main.osCLS()
			creditcard.options()
		elif choice == '3':
			print()
			Main.changePassword()
		elif choice == '4':
			Main.osCLS()
			Main.main()
		elif choice == '9':
			Main.osCLS()
			exit()
		else:
			print()
			print(f"{Fore.RED}Incorect Option")
			time.sleep(1.5)
			Main.osCLS()
			Main.options()

tries = 5
count = 0
password.osCLS()
Main.main()
