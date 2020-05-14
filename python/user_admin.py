import psycopg2

connection = None

def readPassword():
    f = open('/home/ec2-user/sql-passwd','r')
    line = f.readline()
    f.close()
    print("/"+line[:-1]+"/")
    return line[:-1]

def connect():
    return psycopg2.connect(user='image_gallery', password=readPassword(), dbname='image_gallery', host='demo-database-1.c923ckbw7nvl.us-east-2.rds.amazonaws.com')

def execute(query, other=None):
    cursor = connection.cursor()
    if other:
        cursor.execute(query, other)
    else:
        cursor.execute(query)
    return cursor
    
def listUsers():
    for r in execute('select username,password,full_name from users'):
        print(r[0]+' '+r[1]+' '+r[2])    

def addUser():
    username = input('Username> ')
    password = input('Password> ')
    fullName = input('Full name> ')
    execute("insert into users (username,password,full_name) values (%s,%s,%s)", (username,password,fullName))

def menu():
    print('1) List users')
    print('2) Add user')
    print('3) Modify user')
    print('4) Delete user')
    print('5) Quit')
    opt = int(input('Select option> '))
    if (opt == 1):
        listUsers()
    elif (opt == 2):
        addUser()
    return opt != 5
    
def main():
    global connection
    connection = connect()
    while(menu()):
        pass
   
        
if __name__ == '__main__':
    main()