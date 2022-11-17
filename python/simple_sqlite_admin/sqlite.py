import sqlite3
import os
db = 'admin.db'
'''

Change your login and password at 25 line

'''


def start():
    try:
        con=sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS admin(
                login STRING,
                password STRING
            );
            '''
        )
        con.commit()
        qwery = f'''
        INSERT INTO admin VALUES("admin","admin");
        '''#login with password
        cursor.execute(qwery)
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print('Error: ', error)
    finally:
        if(con):
            con.close()
            print('DB close')

def tryenter(login,password):
    con = sqlite3.connect(db)
    cursor = con.cursor()
    qwery = f'''
    SELECT login,password FROM admin;
    '''
    cursor.execute(qwery)
    res = cursor.fetchall()
    if login == res[0][0] and password == res[0][1]: #1 login 2 password
        return True
    else:
        return False
if not os.path.isfile('admin.db'):
    start()