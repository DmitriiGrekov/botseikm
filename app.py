import sqlite3
questions={}

f = open('eikm_testy.txt','r')
for line in f:
    
    arr=line.split("$$")
    
    questions[arr[0]]=arr[-1]
    

print(questions)
 
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
 
# Создание таблицы
for j in questions.keys():
    cursor.execute("INSERT INTO albums VALUES (?,?)", [j, questions[j]])
print("Добавлено")
conn.commit()
