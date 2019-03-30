import sqlite3
def get_anser(tex):
        
        conn = sqlite3.connect("mydatabase.db")
        #conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
 
        sql = "SELECT * FROM albums WHERE question=?"
        for row in cursor.execute(sql,([tex])):
                return row[-1]
print(get_anser("Как меня зовут?"))
