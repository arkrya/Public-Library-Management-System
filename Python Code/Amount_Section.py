'''
This section will be used for storing all the transaction amount used in library.
These transaction will include:-
Book Purchase Amount
Fine Amount
Book Issue Amount
'''

import Library_Functions



def book_amount(Book_ID, Vendor_ID, Book_Category_ID, Date_Of_Purchase, Book_Cost):
    mydb,mycursor = Library_Functions.sqlConnect()
    
    # Entering data in Book Purchase Table
    x = Library_Functions.Null_ID('Book_Purchase')
    if x == False:
        Purchase_ID= 'PID0000001'
    elif x == True:
        Purchase_ID= Library_Functions.Next_ID('Purchase_ID', 'Book_Purchase')
        
    sql = "INSERT INTO Book_Purchase (Purchase_ID, Book_ID, Vendor_ID, Book_Category_ID, Date_Of_Purchase, P_Amount) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Purchase_ID, Book_ID, Vendor_ID, Book_Category_ID, Date_Of_Purchase, Book_Cost)
    mycursor.execute(sql, val)
    mydb.commit()
    
    mycursor.close()
    mydb.close()

def issue_amt(Book_ID, Return_Date, Return_ID):
    mydb,mycursor = Library_Functions.sqlConnect()
    # Entering Data On Fine Collection Table
    x = Library_Functions.Null_ID('Book_Issue_Amount')
    if x == False:
        BIA_ID= 'BIA0000001'
    elif x == True:
        BIA_ID= Library_Functions.Next_ID('BIA_ID', 'Book_Issue_Amount')
    
    sql = "SELECT Issue_ID FROM Book_Issue WHERE Book_ID = '" + Book_ID + "' ORDER BY Issue_Date DESC LIMIT 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        for y in x:
            Issue_ID = y
    
    due_date = Library_Functions.search_specifc('Due_Date', 'Book_Issue', 'Issue_ID', Issue_ID)
    Issue_Amount = Library_Functions.issue_amt(Book_ID)
    Fine = Library_Functions.fine(due_date)
    if Fine == None:
        Total_Amount = Issue_Amount
    else:
        Total_Amount = Issue_Amount + Fine
    sql2 = "INSERT INTO Book_Issue_Amount (BIA_ID, Issue_ID, Return_ID, Return_Date, Issue_Amount, Fine, Total_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val2 = (BIA_ID, Issue_ID, Return_ID, Return_Date, Issue_Amount, Fine, Total_Amount)
    mycursor.execute(sql2, val2)

    mydb.commit()
    print(f'Total Issue Amount = {Total_Amount}')

    mycursor.close()
    mydb.close()