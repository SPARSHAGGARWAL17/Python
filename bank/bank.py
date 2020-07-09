import random
import string 
import openpyxl as op
workbook = op.load_workbook('data.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')
_acc = 1
_name = 2
_pas = 3
_amount = 4
class bank:
    def create_account():
        row = sheet.max_row
        col = sheet.max_column
        account_list = []
        for i in range(1,row+1):
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
                sheet.cell(row+1,_acc).value = account_no
                break
        password = ''.join(random.choice(letters+numbers) for i in range(15))
        sheet.cell(row+1,_pas).value = password
        sheet.cell(row+1,_name).value = name
        sheet.cell(row+1,_amount).value = 0
        print('\nHello, ',name.upper())
        print('Use the following details to Login.')
        print('-----------------------------------')
        print('Account Number : ',account_no)
        print('Password : ',password)
        print('-----------------------------------')
        workbook.save('data.xlsx')
    def login():
        