import re
def change_address(cursor,cust_id):
	print ("****** 1. ADDRESS CHANGE ******")
	print (" Enter new address details")
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
	cursor.execute("UPDATE Customer SET AddressLine1='"+addr1+"',AddressLine2='"+addr2+"',City='"+city+"',State='"+state+"',Pincode="+str(pin)+" WHERE CustomerId="+str(cust_id)+"")
