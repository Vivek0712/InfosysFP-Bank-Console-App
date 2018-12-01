import sign_up
import mysql.connector
from sign_in import signin
from admin_signin import admin_sign_in
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="mysql")
c=db.cursor()
correct_menu = True
while(correct_menu):
    print (" ******** MENU ********")
    print ("1. Sign Up(New Customer)")
    print ("2. Sign In(Existing Customer)")
    print ("3. Admin Sign In")
    print ("4. Quit")
    menu_option = int(input("Enter the menu : "));
    if(menu_option == 4):
        correct_menu=False
        print ("****EXIT****")
        exit()
    elif(menu_option == 1):
        res = sign_up.signup(c)
        if(res == -1):
            print(" Account creation failed: Insufficient inital deposit(<5000)")
        else:
            print(" Account creation successful")
            db.commit()
    elif(menu_option == 2):
        signin(db,c)
    elif(menu_option == 3):
        admin_sign_in(db,c)
    else:
        print ("Enter valid menu")
c.close()