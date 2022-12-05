'''
This Section is issuing and returning the books.
'''

import Library_Functions
from datetime import date
import Amount_Section


# Entering Data On Issue Table
def book_issue():
    mydb, mycursor = Library_Functions.sqlConnect()
    try:
        Issue_ID = 'IID' + Library_Functions.Date_ID()
        M_ID = input('Enter M_ID: ')
        Book_ID = input('Enter Book_ID: ')
        Issue_Date = date.today()
        Due_Date = input('Due Date (YYYY-MM-DD): ')
        
        
        sql = "INSERT INTO Book_Issue (Issue_ID, M_ID, Book_ID, Issue_Date, Due_Date) VALUES (%s, %s, %s, %s, %s)"
        val = (Issue_ID, M_ID, Book_ID, Issue_Date, Due_Date)
        mycursor.execute(sql, val)
        
        mydb.commit()
        print('Book Issued Successfully!!!\n\n')
    except:
        print('Book Issue Failed!!!\n\n')
        
    mycursor.close()
    mydb.close()

# Entering Data On Return Table

def book_return():
    mydb, mycursor = Library_Functions.sqlConnect()

    try:
        Return_ID = 'RID' + Library_Functions.Date_ID()
        M_ID = input('Enter M_ID: ')
        Book_ID = input('Enter Book_ID: ')
        Return_Date = date.today()
        
        sql = "INSERT INTO Book_Return (Return_ID, M_ID, Book_ID, Return_Date) VALUES (%s, %s, %s, %s)"
        val = (Return_ID, M_ID, Book_ID, Return_Date)
        mycursor.execute(sql, val)
        mydb.commit()
        Amount_Section.issue_amt(Book_ID, Return_Date, Return_ID)
        
        
        print('Book Returned Successfully!!!\n\n')
    except:
        print('Book Return Failed!!!\n\n')
    
    mycursor.close()
    mydb.close()


# Deleting Last Issue Record
def delete_last_issue():
    try:
        value = Library_Functions.last_ID('Issue_ID', 'Book_Issue')        # Fetch Last Issue ID
        Library_Functions.delete_info('Book_Issue', 'Issue_ID', value)     # Delete Last Issue Record
        print('Record Deleted Successfully!!!\n\n')
    except:
        print('Record Not Deleted!!!\n\n')

# Deleting Last Return Record
def delete_last_return():
    try:
        value = Library_Functions.last_ID('Return_ID', 'Book_Return')        # Fetch Last Return ID
        Library_Functions.delete_info('Book_Return', 'Return_ID', value)     # Delete Last Return Record
        print('Record Deleted Successfully!!!\n\n')
    except:
        print('Record Not Deleted!!!\n\n')

# Updating Last Issue Record
def update_last_issue():
    flag = 0
    while True:
        print('Press (1)>>>>> Member ID')
        print('Press (2)>>>>> Book ID')
        print('Press (3)>>>>> Issue Date')
        print('Press (4)>>>>> Due Date')
        print('Press (0)>>>>> BACK')
        issue_info = int(input('>>>>> '))
        x = ['*', 'M_ID', 'Book_ID', 'Issue_Date', 'Due_Date']
        if (issue_info < 0 or issue_info > 4):
            Library_Functions.clear()
            print('Invalid Choice!!!\n\n')
            continue
        elif issue_info == 0:
            if flag == 0:
                Library_Functions.clear()
                print('Book Issue Update Cancelled!!!\n\n')
                break
            else:
                Library_Functions.clear()
                print('Updation Complete!!!\n\n')
                break
        else:
            ID_value = Library_Functions.last_ID('Issue_ID', 'Book_Issue')
            value = input('Input Value: ')
            Library_Functions.update_info('Book_Issue', x[issue_info], value, 'Issue_ID', ID_value)
            flag = 1
            Library_Functions.clear()
            print(x[issue_info] + ' Updated Successfully!!!\n\n')
            
            
# Updating Last Return Record
def update_last_return():
    flag = 0
    while True:
        print('Press (1)>>>>> Member ID')
        print('Press (2)>>>>> Book ID')
        print('Press (3)>>>>> Return Date')
        print('Press (0)>>>>> BACK')
        ret_info = int(input('>>>>> '))
        x = ['*', 'M_ID', 'Book_ID', 'Return_Date']
        if (ret_info < 0 or ret_info > 3):
            Library_Functions.clear()
            print('Invalid Choice!!!\n\n')
            continue
        elif ret_info == 0:
            if flag == 0:
                Library_Functions.clear()
                print('Book Return Update Cancelled!!!\n\n')
                break
            else:
                Library_Functions.clear()
                print('Updation Complete!!!\n\n')
                break
        else:
            ID_value = Library_Functions.last_ID('Return_ID', 'Book_Return')
            value = input('Input Value: ')
            Library_Functions.update_info('Book_Return', x[ret_info], value, 'Return_ID', ID_value)
            flag = 1
            Library_Functions.clear()
            print(x[ret_info] + ' Updated Successfully!!!\n\n')