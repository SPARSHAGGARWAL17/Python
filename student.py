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


def menu(v):
    print(v)
    switch = {
        1: table(cur,conn),
        2: display(cur,conn),
        3: '',
        4: '',
        5: '',
        6: exit
    }
    
    switch[v]

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


def display(cur,conn):
    try:
        cur.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = student;''')
        conn.commit()
        row = cur.fetchall()
        col = []
        print('==================================================================')
        for i in range(len(row)):
            print(row[i][3].ljust(20,' '),end=' |')
        print('\n==================================================================')
        cur.execute(''' SELECT * FROM students;''')
        conn.commit()
        data = cur.fetchall()
        for i in data:
            
            for j in i:
                print(str(j).ljust(20, ' '), end=' |')
        print('\n==================================================================')
    except Exception as e:
        print('NO database. \n ')


def insert(cur,conn):
    name = input('Enter name of the table to insert:  ')
    while True:
        if name in tname:
            pass


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
    pass
elif(choice==4):
    pass
elif(choice==5):
    pass
elif(choice==6):
    exit