
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
    try:
        cur.execute(f'CREATE TABLE {name}();')
        conn.commit()
        for i in range(len(list1)):
            cur.execute(f'''ALTER TABLE {name} \
                                ADD {list1[i]} {list2[i]};''')
            conn.commit()
        print('Table created!')
    except:
        print('Table already exist!')
        cur.execute('ROLLBACK')
        conn.commit()
        return

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
        if coname == '':
            break
        colname.append(coname)
        datatype.append(switchdt(dt))
    createtable(colname, datatype, name, cur, conn)

def displaytable(row,data,cur,conn):
    print('==================================================================')
    for i in range(len(row)):
        print(row[i].ljust(20, ' '), end=' |')
    print('\n==================================================================')
    
    for i in data:
        for j in i:
            print(str(j).ljust(20, ' '), end=' |')
        print('\n')
    print('==================================================================')

def display(cur,conn):
    try:
        col,data,name = getdata(cur,conn)
        cur.execute(f''' SELECT * FROM {name};''')
        conn.commit()
        data1 = cur.fetchall()
        displaytable(col,data1,cur,conn)
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
        return(col,data,name)
    except:
        print('Invalid input!')
        return (None,None,None)

def insert(cur,conn):
    while True:
        try:
            col,data,name  = getdata(cur,conn)
            if col == None:
                continue
            inputs=[]
            print(f'Enter data for table {name}')
            for i in range(len(col)):
                in1 = input(f'Enter value for {col[i]}: ')
                if data[i]=='integer':
                    inputs.append(f"{in1}")
                else:
                    inputs.append(f"\'{in1}\'")
            record = ','.join(col)
            values = ','.join(inputs)
            cur.execute(f'''INSERT INTO {name} ({record})
                            VALUES ({values})''')
            conn.commit()
            print(values)
            break
        except:
            print('Invalid table name!')
def operation(string,cur,conn):
    col,data,name = getdata(cur,conn)
    if string == 'search':
        while True:
            try:
                for i in range(len(col)):
                    print(f'{i+1}. {string} by {col[i]}')
                op = int(input('Enter your operation'))
                val = input('Enter value: ')
                if data[op-1]!='integer':
                    val = f"\'{val}\'"
                print(val)
                cur.execute(f'SELECT * FROM {name} WHERE {col[op-1]} = {val}')
                conn.commit()
                data1 = cur.fetchall()
                displaytable(col,data1,cur,conn)
                break
            except:
                print('Error!')
    elif string == 'delete':
        while True:
            try:
                for i in range(len(col)):
                    print(f'{i+1}. {string} by {col[i]}')
                op = int(input('Enter your operation: '))
                val = input('Enter value: ')
                if data[op-1] != 'integer':
                    val = f"\'{val}\'"
                cur.execute(f'DELETE FROM {name} WHERE {col[op-1]} = {val}')
                conn.commit()
                display(cur,conn)
                break
            except:
                print('Error!')

print("----------------------------------------")
print('~ WELCOME TO STUDENT MANAGEMENT SYSTEM ~')
print("----------------------------------------")
conn = psycopg2.connect(database = 'student',user = sec.username, password = sec.password)
cur = conn.cursor()
print('Connection Ready!')
while True:
    try:
        choice = int(input('Select option. \n 1. Create Table \n 2. Display Table \n 3. Insert \n 4. Search \n 5. Delete \n 6. Exit   : '))
        if choice == 1:
            table(cur, conn)
        elif(choice == 2):
            display(cur, conn)
        elif(choice == 3):
            insert(cur, conn)
        elif(choice == 4):
            operation('search', cur, conn)
        elif(choice == 5):
            operation('delete', cur, conn)
        elif(choice == 6):
            break
    except:
        print('Invalid number!')
