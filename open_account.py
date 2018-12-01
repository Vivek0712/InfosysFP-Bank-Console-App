import datetime
import random
import re
class Savings():
    __date = ""
    __amt = 0.0
    __accnum = 0
    __withdrawals = 0
    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        flag = True
        while(flag):
            self.__amt = int(input(" Enter amount to be deposited : "))
            if(self.__amt > 0):
                flag = False
            else:
                print (" Enter valid amount")
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("INSERT INTO Savings VALUES(%s,%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date,self. __withdrawals))
        self.display_details()
    def display_details(self):
        print (" Account Number : ",self.__accnum)
        print (" Balance : ",self.__amt)
        print (" Date Created : ",self.__date)
        print (" No of Withdrawal done : ",self.__withdrawals)

class CurrentAccount():
    __date = ""
    __amt = 0.0
    __accnum = 0
    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        flag = True
        while(flag):
            self.__amt = float(input(" Enter amount to be deposited : "))
            if(self.__amt > 5000):
                flag = False
            else:
                print (" Enter valid amount(Min 5000)")
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("INSERT INTO CurrentAccount VALUES(%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date))
        self.display_details()
    def display_details(self):
        print (" Account Number : ",self.__accnum)
        print (" Balance : ",self.__amt)
        print (" Date Created : ",self.__date)

class FixedDeposit():
    __date = ""
    __amt = 0.0
    __accnum = 0
    __deposit_term = 0
    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        flag = True
        while(flag):
            self.__amt = int(input(" Enter amount to be deposited : "))
            if(self.__amt > 0):
                if(self.__amt%1000==0):
                    flag = False
                else:
                    print (" Deposit should be in terms of 1000")
            else:
                print (" Enter valid amount")
        flag = True
        while(flag):
            self.__deposit_term = int(input(" Enter term to be deposited : "))
            if(self.__deposit_term > 0):
                flag = False
            else:
                print (" Invalid term")
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("INSERT INTO FixedDeposit VALUES(%s,%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date,self.__deposit_term))
        self.display_details(cursor,cust_id)
    def display_details(self,cursor,cust_id):
        cursor.execute("SELECT * FROM FixedDeposit WHERE CustomerId='"+str(cust_id)+"'")
        res =  cursor.fetchall()
        print (" {0:15s} \t{1:8s}\t{2:20s}\t{3:15s}".format("Account Number","Amount","Date Created","Deposit Term"))
        for result in res:
            print (" {0:14d} \t{1:8f}\t{2}\t{3:12d}".format(result[0],result[2],result[3],result[4]))

def open_account(cursor,cust_id):
    print (" ********* NEW ACCOUNT ********")
    flag = True
    flag_acc = False
    result = 0
    while(flag):
        print (" Press 0 to go back....")
        option = int(input(" Enter the type of account (1.Savings Account, 2.Current Account, 3.Fixed Deposit Account) : "))
        if (option == 0):
            if(flag_acc == False):
                return -1
            else:
                return 1
        elif (option == 1):
            print (" ******* SAVINGS ACCOUNT *******")
            savings_acc = Savings()
            savings_acc.set_accnum(generate_accnum(cursor))
            savings_acc.writeDetails(cursor,cust_id)
            flag_acc = True
        elif (option == 2):
            print (" ******* CURRENT ACCOUNT *******")
            current_acc = CurrentAccount()
            current_acc.set_accnum(generate_accnum(cursor))
            current_acc.writeDetails(cursor,cust_id)
            flag_acc = True
        elif (option == 3):
            print (" ******* FIXED DEPOSIT ACCOUNT *******")
            fd_acc = FixedDeposit()
            fd_acc.set_accnum(generate_accnum(cursor))
            fd_acc.writeDetails(cursor,cust_id)
            flag_acc = True
        else:
            print (" Enter valid option")
def generate_accnum(cursor):
    flag = True
    while(flag):
    	random_num = random.randint(10000,99999)
    	cursor.execute("SELECT s.AccountNumber FROM Savings s INNER JOIN CurrentAccount ca INNER JOIN FixedDeposit fd INNER JOIN LoanAccount la ON s.AccountNumber = ca.AccountNumber AND s.AccountNumber = fd.AccountNumber AND s.AccountNumber = la.AccountNumber WHERE s.AccountNumber = %d"%random_num)
    	if(not(cursor.fetchone())):
    		account_num = random_num
    		flag = False
    return account_num
