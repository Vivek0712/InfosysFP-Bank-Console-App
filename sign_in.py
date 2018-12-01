import getpass
import re
from address_change import change_address
from money_deposit import deposit_money
from money_withdrawal import withdraw_money
from print_statement import print_statement
from account_closure import close_account
from money_transfer import transfer_money
from open_account import open_account
from loan_account import take_loan
def signin(db,cursor):
	print ("*******\t SIGN IN \t*******")
	flag = True
	count = 1
	while(flag and (count <= 3)):
		uname = int(input(" Enter Customer Id : "))
		password = getpass.getpass(" Enter password : ")
		cursor.execute("Select CustomerId,Password from Customer where CustomerId = '"+str(uname)+"' and Password = '"+password+"'")
		if(not(cursor.fetchone())):
			count += 1
			print (" Invalid customer id or password ")
		else:
			print (" Login successful")
			flag = False
	if(count > 3):
		print ("Too many unsuccessful logins")
		return -1
	correct_menu = True
	while(correct_menu):
		print ("********* MENU *********")
		print (" 1. Address Change")
		print (" 2. Open New Account")
		print (" 3. Money Deposit")
		print (" 4. Money Withdrawal")
		print (" 5. Print Statement")
		print (" 6. Transfer Money")
		print (" 7. Account Closure")
		print (" 8. Avail Loan")
		print (" 9. Logout")
		option = int(input("Enter the submenu : "))
		if(option == 9):
			correct_menu = False
			print (" Logout successful")
			return 0
		elif(option == 1):
			change_address(cursor,uname)
			print (" Address change successful")
			print ("***************************")
			db.commit()
		elif(option == 2):
			res = open_account(cursor,uname)
			if(res == 1):
				print (" Account created successfully")
				db.commit()
			else:
				print (" No account created")
		elif(option == 3):
			res = deposit_money(cursor,uname)
			if(res == 1):
				print (" Deposit Successful")
				db.commit()
			elif(res == -2):
				print (" Invalid Amount")
			else:
				print ("*************************")
				print (" Invalid Account Number")
			print ("***************************")
		elif(option == 4):
			res= withdraw_money(cursor,uname)
			if(res == 1):
				print (" Withdrawal successful")
				db.commit()
			elif(res == -2):
				print (" Withdrawals execeeded")
			elif(res == -3):
				print (" Invalid Account Type")
			else:
				print (" Insufficient balance")
		elif(option == 5):
			res = print_statement(cursor,uname)
			if(res == -1):
				print (" Invalid date")
			elif(res == -2):
				print (" Invalid Account Number")
			else:
				print ("*************************")
		elif(option == 6):
			res = transfer_money(cursor,uname)
			if(res == -1):
				print (" Insufficient Balance")
			elif(res == -2):
				print (" Invalid Account Number")
			else:
				print (" Transfer Successful")
				db.commit()
			print ("********************************")
		elif(option == 7):
			res = close_account(cursor,uname)
			if(res == 1):
				print (" Account closed successfully")
				db.commit()
			elif(res == -1):
				print (" Account closure terminated")
			else:
				print (" Invalid Account Number")
		elif(option == 8):
			res = take_loan(cursor,uname)
			if(res == 1):
				print (" Loan Granted")
				db.commit()
			elif(res == -1):
				print (" Not eligible for loan")
		else:
			print ("Enter valid option")
