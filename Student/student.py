from typing import ValuesView
import psycopg2

# FILE FOR USERNAME AND PASSWORD
import sec
global tname;
tname=[]
global tno;

def columnname():
    while True:
        name = input(f'Enter name for column : ')
        try:
            datatype = int(
                input('Enter datatype for column [1. int/ 2. char/ 3. float]: '))
            if datatype not in range(1,4) and datatype!='':
                continue
            return (name, datatype)
        except Exception as e:
            print(f'Invalid! \n{e}')



def createtable(list1, list2, name,cur ,conn):
    cur.execute(f'CREATE TABLE {name}();')
    conn.commit()
    print('Table created!')
    for i in range(len(list1)):
        cur.execute(f'''ALTER TABLE {name} \
                            ADD {list1[i]} {list2[i]};''')
        conn.commit()

def switchdt(a):
    switch = {
        1: 'int',
        2: 'varchar(255)',
        3: 'float'
    }
    return switch[a]



def table(cur ,conn):
    colname = []
    datatype = []
    name = input('Enter name for table: ')
    tname.append(name)
    colno = int(input('Enter number of Columns: '))
    for i in range(colno):
        coname, dt = columnname()
        print(coname)
        if coname == '':
            break
        colname.append(coname)
        datatype.append(switchdt(dt))
    createtable(colname, datatype, name, cur, conn)
    print('Table and Columns Created.')

def displaytable(row,cur,conn):
    print('==================================================================')
    for i in range(len(row)):
        print(row[i][3].ljust(20, ' '), end=' |')
    print('\n==================================================================')
    cur.execute(''' SELECT * FROM student;''')
    conn.commit()
    data = cur.fetchall()
    for i in data:
        for j in i:
            print(str(j).ljust(20, ' '), end=' |')
        print('\n')
    print('==================================================================')

def display(cur,conn):
    try:
        cur.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'student';''')
        conn.commit()
        row = cur.fetchall()
        name = input('Enter name of the table: ')
        displaytable(row,cur,conn)
    except Exception as e:
        print('NO database. \n ')

def getdata(cur,conn):
    try:
        name = input('Enter name of table: ')
        cur.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_NAME = '{name}';''')
        conn.commit()
        row = cur.fetchall()
        col = []
        data = []
        for i in range(len(row)):
            col.append(row[i][3])
            data.append(row[i][7])
        return(col,data)
    except:
        print('Invalid input!')
        return (None,None)

def insert(cur,conn):
    while True:
        try:
            col,data = getdata(cur,conn)
            if col == None:
                continue
            inputs=[]
            for i in range(len(col)):
                in1 = input(f'Enter value for {col[i]}: ')
                if data[i]=='integer':
                    inputs.append(f"{in1}")
                else:
                    inputs.append(f"\'{in1}\'")
            record = ','.join(col)
            values = ','.join(inputs)
            cur.execute(f'''INSERT INTO student ({record})
                            VALUES ({values})''')
            conn.commit()
            print(values)
            break
        except:
            print('Invalid table name!')
def operation(string,conn,cur):
    name = input('Enter table name: ')


print("----------------------------------------")
print('~ WELCOME TO STUDENT MANAGEMENT SYSTEM ~')
print("----------------------------------------")
conn = psycopg2.connect(database = 'student',user = sec.username, password = sec.password)
cur = conn.cursor()
print('Connection Ready!')
while True:
    try:
        choice = int(input('Select option. \n 1. Create Table \n 2. Display Table \n 3. Insert \n 4. Search \n 5. Delete \n 6. Exit   : '))
        break
    except:
        print('Invalid number!')
if choice ==1:
    table(cur,conn)
elif(choice==2):
    display(cur,conn)
elif(choice==3):
    insert(cur,conn)
elif(choice==4):
    pass
elif(choice==5):
    pass
elif(choice==6):
    exit
