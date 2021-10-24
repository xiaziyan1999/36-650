import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("psycopg2")

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
conn.commit()
print(cur.rowcount, "record inserted.")


conn.commit()
cur.close()
conn.close()
