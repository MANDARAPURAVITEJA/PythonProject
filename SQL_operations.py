import pymysql
from flask import jsonify

def Create_Table(): #Execute only one time to create the table.
    # localhost,username,password,database name
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server

    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    #Query for creating database and table structure.
    db_query= """create database if not exists User;"""
    db_query_use = """use User"""
    table_createquery="""
    create table user_details(
    user_id int not null auto_increment primary key,
    first_name varchar(30),
    last_name varchar(30),
    emailid varchar(50),
    password varchar(20),
    security_question varchar(30)
    );"""
    
    query=cursor_obj.execute(db_query);print(query) # to execute the sql query
    query=cursor_obj.execute(db_query_use);print(query)
    query=cursor_obj.execute(table_createquery);print(query)
    db_obj.commit() # for savings the changes to database
    db_obj.close()  # to close the database connection


def database_exists(database_name, connection):
    cursor = connection.cursor()
    
    # Use the information_schema to check if the database exists
    cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s", (database_name,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the cursor
    cursor.close()
    
    # If the result is not None, the database exists
    return result is not None


def Insert_Data(first_name,last_name,emailid,password,security_question):
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server
    print(db_obj)
    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    # Check if the database exists
    database_name="User"
    if database_exists(database_name, db_obj):
        print(f"The database '{database_name}' exists.")
    else:
        print(f"The database '{database_name}' does not exist.")
        Create_Table()

    db_query_use = """use User"""
    insert_query= """insert into user_details(first_name,last_name,emailid,password,security_question)
    values('"""+str(first_name)+"','"+str(last_name)+"','"+str(emailid)+"','"+str(password)+"','"+str(security_question)+"""');"""

    query=cursor_obj.execute(db_query_use);print(query)
    query=cursor_obj.execute(insert_query);print(query)
    db_obj.commit() # for savings the changes to database
    db_obj.close()  # to close the database connection


def retrieve_data(username,password):
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server
    print(db_obj)
    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    db_query_use = """use User"""
    retrieve_query= """select emailid,password from user_details
    where emailid='"""+str(username)+"' and password='"+str(password)+"';"
    
    query=cursor_obj.execute(db_query_use)
    query=cursor_obj.execute(retrieve_query);print(query)

    result = cursor_obj.fetchone();print(result)
    
    # Close the cursor
    cursor_obj.close()
    
    # If the result is not None, the database exists
    return result is not None

def homepage_data():
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server
    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    db_query_use = """use User"""
    retrieve_query= """select * from employee;"""

    
    
    query=cursor_obj.execute(db_query_use)
    cursor_obj.execute(retrieve_query)

    result =[column for column in cursor_obj.fetchall()];print(result)
    
    # Close the cursor
    cursor_obj.close()
    return result




