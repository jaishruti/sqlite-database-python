import sqlite3
conn = sqlite3.connect("student.db")
# conn.execute('''
#     Create table studentDetails(
#              reg_no INT PRIMARY KEY,
#              name VARCHAR(20),
#              age INT,
#              grade INT
#     )
# ''')

#inserting data into out table
# insertion = '''
#     insert into studentDetails (reg_no, name, age, grade) VALUES 
#     (124, 'Aanya', 18, 12)
# '''
result=conn.execute('''
select * from studentDetails''')

for i in result:
    print("regno-",i[0]," name-",i[1])
# conn.commit()
conn.close()