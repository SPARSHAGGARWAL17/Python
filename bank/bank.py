import random
import string
from sys import setprofile 
import openpyxl as op
# file name goes here
file = 'data.xlsx'
workbook = op.load_workbook(file)
sheet = workbook['Sheet1']
_acc = 1
_name = 2
_pas = 3
_amount = 4
row = sheet.max_row+1
col = sheet.max_column

def create_account():
    account_list = []
    for i in range(1,row):
        cell = sheet.cell(i,1)
        account_list.append(cell)
    print(row,col)
    print('~ Create Account in Bank. ~')
    name = input('Enter your name : ')
    letters = string.ascii_letters
    numbers = string.digits
    while True:
        account_no = random.randint(100000000,999999999)
        if account_no in account_list:
            continue
        else:
            sheet.cell(row,_acc).value = account_no
            break
    password = ''.join(random.choice(letters+numbers) for i in range(15))
    sheet.cell(row,_pas).value = password
    sheet.cell(row,_name).value = name
    sheet.cell(row,_amount).value = 0
    print('\nHello, ',name.upper())
    print('Use the following details to Login.')
    print('-----------------------------------')
    print('Account Number : ',account_no)
    print('Password : ',password)
    print('-----------------------------------')
    workbook.save(file)
def login():
    print('~ Enter details to login ~')
    while True:
        login = (False,)
        account_no = input('Enter your Account number : ')
        password = input('Enter Password : ')
        for i in range(1,row):
            acc = sheet.cell(i,_acc).value
            pas = sheet.cell(i,_pas).value
            if account_no == str(acc):
                if password == pas:
                    login = (True,i)
                    break
        if login[0]:
            print('Login Successful!')
            name = sheet.cell(login[1],_name).value
            print('Hello, ',name.upper())
            while True:
                choice = input('Enter your choice: \n 1. Transactions \n 2. Transfer \n 3. Logout : ')
                if choice == '1':
                    transact(login)
                    continue
                elif choice =='2':
                    transfer(login)
                    continue
                elif choice =='3':
                    break
                else:
                    print('Invalid Choice')
                    continue
        else:
            print('Invalid User')
        break
def transact(login):
    amount = sheet.cell(login[1],_amount).value
    print('-----------------------------------')
    print("Amount Available : ",amount)
    while True:
        choice = input('\nSelect Choice: \n 1. Deposit \n 2. Withdraw : ')
        if choice =='1':
            while True:
                try:
                    deposit = int(input('Enter amount to Deposit : '))
                    sheet.cell(login[1],_amount).value = amount+deposit
                    print('Deposited Successfully.')
                    print("Amount Available : ",amount+deposit)
                    workbook.save(file)
                    break
                except:
                    print('Invalid Value!')
                    continue
            break
        elif choice == '2':
            while True:
                try:
                    withdraw = int(input("Enter amount to Withdraw : ")) 
                    if 0 <= withdraw < amount :
                        sheet.cell(login[1],_amount).value = amount-withdraw
                        print('Withdraw Successful!')
                        print('Available Amount : ',amount-withdraw)
                        workbook.save(file)
                        break
                    else:
                        print('Invalid Amount!')
                        continue
                except:
                    print('Invalid Amount!')
            break
def transfer(login):
    print('-----------------------------------')
    while True:
        amount = sheet.cell(login[1],_amount).value
        print('Available Amount : ',amount)
        user = (False,0)
        try:
            account_no = int(input('Enter account number to Transfer : '))
            for i in range(1,row):
                acc = sheet.cell(i,_acc).value
                if str(account_no) == str(acc):
                    print("BANK USER FOUND!")
                    user = (True,i)
            if user[0]:
                while True:
                    amount_user = int(input('Enter amount to Transfer: '))
                    if amount_user >= amount:
                        print('Invalid Amount')
                        continue
                    else:
                        break
                sheet.cell(login[1],_amount).value = amount-amount_user
                sheet.cell(user[1],_amount).value+=amount_user
                print('Transfer Successful!')
                print('Available Amount : ',amount-amount_user)
                workbook.save(file)
                break
            else:
                print('Invalid User!')
                continue
        except:
            print('Invalid acc.')
print('===========================')
print('  ~ WELCOME TO THE BANK ~  ')
print('===========================')
while True:
    try:
        ch = int(input("Enter your choice: \n 1. Create Account \n 2. Login \n 3. Exit : "))
        if ch ==1:
            create_account()
            continue
        elif ch == 2:
            login()
            continue
        elif ch ==3:
            break
        else:
            print('Invalid Choice!')
            continue
    except:
        print('Invalid Choice!')
        continue