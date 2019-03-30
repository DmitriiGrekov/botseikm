import sqlite3
questions={}

f = open('text.txt')
for line in f:
    arr=line.split("$$")
    questions[arr[0]]=arr[1]

print(questions)
 
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
 
# Создание таблицы
cursor.execute("""CREATE TABLE albums
                  (question text, answer text)
               """)
for j in questions.keys():
    cursor.execute("INSERT INTO albums VALUES (?,?)", [j, questions[j]])

conn.commit()
