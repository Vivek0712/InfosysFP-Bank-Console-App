import mysql.connector
import random
import re
import getpass
def signup(cursor):
	flag = True
	while(flag):
		random_num = random.randint(10000,99999)
		cursor.execute("SELECT CustomerId FROM Customer WHERE CustomerId = %d"%random_num)
		if(not(cursor.fetchone())):
			customer_id = random_num
			flag = False
	print (" ********\tSIGN UP\t********")
	print (" Enter details")
	first_name = input(" First Name: ")
	last_name = input(" Last Name: ")
	addr1 = input(" Address Line 1: ")
	addr2 = input(" Address Line 2: ")
	city = input(" City: ")
	state = input(" State: ")
	flag = True
	while(flag):
		pin = input(" Pin: ")
		if(re.match(r'^[0-9]{6}$',pin,0)):
			flag = False
		else:
			print (" Invalid pin( Valid pin: 6 digits)")
	flag = True
	while(flag):
		password1 = getpass.getpass(" \n Enter New Password: ")
		if(re.search(r'\w{8,}',password1,0)):
			password2 = getpass.getpass(" \n Confirm Password: ")
			if(password1 == password2):
				flag = False
			else:
				print(" Password mismatch")
		else:
			print (" Invalid password (Minimum 8 letters)")

	cursor.execute("INSERT INTO Customer VALUES("+str(customer_id)+",'"+first_name+"','"+last_name+"','"+addr1+"','"+addr2+"','"+city+"','"+state+"',"+str(pin)+",'"+password1+"')")
	return 1
