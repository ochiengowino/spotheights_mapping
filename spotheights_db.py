import psycopg2
from psycopg2 import Error
import csv



try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "**********",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "assignment")

  #  cursor = connection.cursor()
    # Print PostgreSQL Connection properties
 #   print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
 #   cursor.execute("SELECT version();")
#    record = cursor.fetchone()
#    print("You are connected to - ", record,"\n")

#except (Exception, psycopg2.Error) as error :
#    print ("Error while connecting to PostgreSQL", error)
   
#

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE spotheights
          (gid SERIAL PRIMARY KEY,
          elevation           NUMERIC    NOT NULL,
          geom         GEOMETRY NOT NULL,
          CONSTRAINT uc_spotheights UNIQUE (elevation,geom)); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
#

with open('C:\Users\LYN\Desktop\BIG_BEN\Assignment\spotheights.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        cursor.execute(
        "INSERT INTO spotheights VALUES (%s, %s, %s)",
        row
        )
        connection.commit()

