'''
Created on Jan 24, 2022

@author: gordie.campbell
'''

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:
        
        conn = sqlite3.connect(db_file)
        
        cur = conn.cursor()
        cur.execute('select * from login')
        count = 0
        
        for row in cur:
            
            converted_data = list(row)
            print(converted_data[0])
            
            print(list(row))
            count+=1
        cur.close()
        
    except Error as e:
        print(e)
    finally:
        
        if conn:
            conn.close()
            
if __name__ == '__main__':
    #create_connection()
    #create_connection(r"C:\sqlite\db\pythonsqlite.db")
    #create_connection(r"C:\sqlite\crap1.db")
    create_connection(r"C:\Users\gordie.campbell\Documents\sample.db")
    #create_connection(r"C:\sqlite\seattle.db")
    
    