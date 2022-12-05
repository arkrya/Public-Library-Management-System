import mysql.connector
import datetime
from os import system, name
from datetime import date

# MySQL Initiation
def sqlConnect():
    mydb = mysql.connector.connect(    
        host = "Enter Your Host ID",    # Host ID
        user = "USER",                  # User_Name
        password = "Your Password",     # Password
        database = "Your Database"      # Current Selected Available Database
    )        
    
    mycursor = mydb.cursor()               # Defining Execution Cursor
    return mydb, mycursor



# *************** Functions Section ***************

# >>>>>> Function 1 <<<<<< 
'''
This function is used for increasing the primary key value by +1
'''
def Next_ID(column_name, table_name):
    mydb, mycursor = sqlConnect()
    sql = 'SELECT ' + column_name + ' FROM ' + table_name + ' ORDER BY ' + column_name + ' DESC LIMIT 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    for x in myresult:
        for y in x:
            z = y
    res = ''.join(filter(lambda i: i.isdigit(), z))
    new = int(res) + 1
    return (z[:3] + '0'*(len(z) - (len(str(new)) + 3)) + str(new))


# >>>>>> Function 2 <<<<<<
'''
This function is used for checking whether the table is null or not.
'''
def Null_ID(table_name):
    mydb, mycursor = sqlConnect()
    sql = 'SELECT * FROM ' + table_name + ' LIMIT 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    if myresult:
        return(True)       # Table Containing Data
    else:
        return(False)      # Null Table


# >>>>>> Function 3 <<<<<<
'''
This function is used to create date ID for primary key
'''
def Date_ID():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # Current Date Time
    did = ''
    for i in str(dt):
        if (i == '-' or i == ':' or i == ' '):
            pass
        else:
            did += i
    return(did) 


# >>>>>> Function 4 <<<<<<
'''
This function is used to clear the screen
'''
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



# >>>>>> Function 5 <<<<<<
'''
This function is used to update the value of a table
'''
def update_info(table_name, column_name, value, ID, ID_value):
    mydb, mycursor = sqlConnect()
    
    # Updating Data into particular tables...
    sql = "UPDATE " + table_name + " SET " + column_name + " = '" + value + "' WHERE (" + ID + " = '" + ID_value + "')"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
    

# >>>>>> Function 6 <<<<<<
'''
This function is used to search specific value in a table
'''    
def search_specifc(column_name, table_name, primary_ID, ID_value):
    mydb, mycursor = sqlConnect()
    sql = "SELECT " + column_name + " FROM " + table_name + " WHERE " + primary_ID + " = '" + ID_value + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    for x in myresult:
        for y in x:
            return(y)



# >>>>>> Function 7 <<<<<<
'''
This function is used to delete value from a table
''' 
def delete_info(table_name, column_name, value):
    mydb, mycursor = sqlConnect()
    sql = "DELETE FROM " + table_name + " WHERE ( " + column_name + " = '" + value + "' )"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()



# >>>>>> Function 8 <<<<<<
'''
This function is used to fetch the last primary key value 
'''
def last_ID(column_name, table_name):
    mydb, mycursor = sqlConnect()
    sql = 'SELECT ' + column_name + ' FROM ' + table_name + ' ORDER BY ' + column_name + ' DESC LIMIT 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    for x in myresult:
        for y in x:
            return (y)



# >>>>>> Function 9 <<<<<<
'''
This function is used to check and calulate the fine
'''  
def fine(due_date):
    mydb, mycursor = sqlConnect()
    return_date = date.today()
    sql = "SELECT DATEDIFF('" + str(return_date) + "', '" + str(due_date) + "')"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    for x in myresult:
        for y in x:
            if y < 1:
                return None
            else:
                return (y*2)             # *2 means 2 INR will be charged per day as fine



# >>>>>> Function 10 <<<<<<
'''
This function is used to retrive the book issue amount as per the category
'''
def issue_amt(Book_ID):
    cat_id = search_specifc('Book_Category_ID', 'Book_Details', 'Book_ID', Book_ID)
    cat_amt = search_specifc('Category_Issue_cost', 'Book_Category', 'Book_Category_ID', cat_id)
    return cat_amt    



# >>>>>> Function 11 <<<<<<
'''
This function is used to view the record as per the provided query
'''
def view(sql):
    from prettytable import PrettyTable
    mydb, mycursor = sqlConnect()
    my_table = PrettyTable()
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()     
    for x in myresult:
        my_table.add_row(x)
    print(my_table)
