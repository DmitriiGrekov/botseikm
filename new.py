import sqlite3 as lite
import sys
 
con = lite.connect('mydatabase.db')
app=[]
f=open('new.txt','w')
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM albums")
    rows = cur.fetchall()
    
 
    for row in rows:
        
        
        
        
        ques=str(row[0]).lower().strip()
        f.write(ques+"$$"+row[1]+'\n')


f.close()
        
        
