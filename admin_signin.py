import getpass
from closed_accounts import print_history
from fd_report import *
from loan_report import *
from customer_report import *
def admin_sign_in(db,cursor):
	print ("*******\t ADMIN SIGN IN \t*******")
	flag = True
	count = 1
	while(flag and (count <= 3)):
		uname = input(" Enter Admin name : ")
		password = getpass.getpass(" Enter password : ")
		cursor.execute("Select AdminId,Password from AdminDetails where AdminId='"+uname+"' and Password = '"+password+"'")
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
		print (" 1. Print closed account history")
		print (" 2. FD Report of a Customer")
		print (" 3. FD Report of a Customer vis-a-vis another Customer")
		print (" 4. FD Report w.r.t a particular FD amount")
		print (" 5. Loan Report of a Customer")
		print (" 6. Loan Report of a Customer vis-a-vis another Customer")
		print (" 7. Loan Report w.r.t a particular loan amount")
		print (" 8. Loan - FD Report of Customers")
		print (" 9. Report of Customers who are yet to avail a loan")
		print (" 10. Report of Customers who are yet to open an FD account")
		print (" 11. Report of Customers who nether have a loan nor an FD account with the bank")
		print (" 0. Logout")
		option = int(input(" Enter the submenu : "))
		if(option == 0):
			correct_menu = False
			print (" Logout successful")
			return 0
		elif(option == 1):
			print_history(cursor)
			print ("***************************")
		elif(option == 2):
			res = print_fd_report(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available")
		elif(option == 3):
			res = print_fd_report_customer(cursor)
			if(res == 1):
				print ("***************************")
			elif(res == -2):
				print (" Not Available ")
			else:
				print (" NO FD account for customer")
		elif(option == 4):
			res = print_fd_report_amount(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		elif(option == 5):
			res = print_loan_report(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available")
		elif(option == 6):
			res = print_loan_report_customer(cursor)
			if(res == 1):
				print ("***************************")
			elif(res == -2):
				print (" Not Available ")
			else:
				print (" NO FD account for customer")
		elif(option == 7):
			res = print_loan_report_amount(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		elif(option == 8):
			res = print_loan_report_(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		elif(option == 9):
			res = print_customer_no_loan(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		elif(option == 10):
			res = print_customer_no_fd(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		elif(option == 11):
			res = print_customer_noloanfd(cursor)
			if(res == 1):
				print ("***************************")
			else:
				print (" Not Available ")
		else:
			print (" Enter valid option")
