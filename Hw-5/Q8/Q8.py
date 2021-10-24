import subprocess
import sys
import psycopg2

#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5433", 
                        user="postgres", 
                        password="123456", 
                        database="postgres"
                       )

sql ='''CREATE TABLE employee(
   id serial,
   fname varchar(10),
   lname varchar(10)
   )'''


cur = conn.cursor()
cur.execute(sql)
sql2 = '''insert into employee(id, fname, lname) VALUES 
(generate_series(1, 500), 
substr(MD5(random()::text), 0, 10), 
substr(MD5(random()::text), 0,10)) '''
cur.execute(sql2)
cur.execute("SELECT * FROM employee limit 10")

myresult = cur.fetchall()

for x in myresult:
  print(x)
conn.commit()
cur.close()
conn.close()