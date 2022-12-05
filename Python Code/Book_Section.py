'''
This section will be used to add or update the book information section.
NOTE:- this section will not contain the issue and return data of a book.

'''
import Library_Functions
from datetime import date
import Amount_Section

def book_info():
    mydb, mycursor = Library_Functions.sqlConnect()
    try:
         
        # Entering Data Into Book Vendors Table
        add_choice = int(input('Press (1)>>>>> Add Vendor\nPress (2)>>>>> Add Book Category\nPress (3)>>>>> Add Book\n>>>>> '))
        
        if add_choice == 1:
            Library_Functions.clear()
            Vendor_Name = input('Vendor Name: ')
            Vendor_Address = input('Vendor Address: ')
            Vendor_Phone = int(input('Vendor Phone Number: '))
            Vendor_EMAIL = input('Vendor E-Mail: ')
            y = Library_Functions.Null_ID('Book_Vendors')
            if y == False:
                Vendor_ID = 'VID0000001'
            elif y == True:
                Vendor_ID = Library_Functions.Next_ID('Vendor_ID', 'Book_Vendors')
            
            sql1 = "INSERT INTO Book_Vendors (Vendor_ID, Vendor_Name, Vendor_Address, Vendor_Phone, Vendor_EMAIL) VALUES (%s, %s, %s, %s, %s)"
            val1 = (Vendor_ID, Vendor_Name, Vendor_Address, Vendor_Phone, Vendor_EMAIL)
            mycursor.execute(sql1, val1)
            
            mydb.commit()
            print('Vendor Has Been Added!!!\n\n')
        # Entering Data into Book Category Table
        
        elif add_choice == 2:
            Library_Functions.clear()
            Book_Category = input('Book Category: ')
            Category_Issue_Cost = int(input('Category Issue Cost: '))
            z = Library_Functions.Null_ID('Book_Category')
            if z == False:
                Book_Category_ID = 'BCD0000001'
            elif z == True:
                Book_Category_ID = Library_Functions.Next_ID('Book_Category_ID', 'Book_Category')
            
            sql1 = "INSERT INTO Book_Category (Book_Category_ID, Book_Category, Category_Issue_Cost) VALUES (%s, %s, %s)"
            val1 = (Book_Category_ID, Book_Category, Category_Issue_Cost)
            mycursor.execute(sql1, val1)
            
            mydb.commit()
            print('Book Category Has Been Added!!!\n\n')
        
        
        # Entering Data into Book Detail Table
        elif add_choice == 3:
            Library_Functions.clear()
            Book_Name = input('Book Name: ')
            Book_Publication = input('Book Publication: ')
            Book_Author = input('Book Author: ')
            Date_Of_Purchase = date.today()
            Book_Status = 'New'
            Book_Condition = 'New'
            Book_Cost = int(input('Book Cost: '))
            Book_Category_ID = input('Book Category ID: ')
            Vendor_ID = input('Vendor ID: ')
            x = Library_Functions.Null_ID('Book_Details')
            if x == False:
                Book_ID = 'BID0000001'
            elif x == True:
                Book_ID = Library_Functions.Next_ID('Book_ID', 'Book_Details')
                
            sql1 = "INSERT INTO Book_Details (Book_ID, Book_Name, Book_Publication, Book_Author, Date_Of_Purchase, Book_Status, Book_Condition, Book_Cost, Book_category_ID, Vendor_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val1 = (Book_ID, Book_Name, Book_Publication, Book_Author, Date_Of_Purchase, Book_Status, Book_Condition, Book_Cost, Book_Category_ID, Vendor_ID)
            mycursor.execute(sql1, val1)
            mydb.commit()
            
            # Entering Data Into Book Purchase Table
            Amount_Section.book_amount(Book_ID, Vendor_ID, Book_Category_ID, Date_Of_Purchase, Book_Cost)
            print('Book Has Been Added!!!\n\n')
        
        else:
            print('Invalid Choice!!!\n\n')
    except:
        print("Book Hasn't Added!!!\n\n ")
    mycursor.close()
    mydb.close()
        

# Deleting Book Details
def book_delete():
    Book_ID = input('Enter Book ID: ')
    Library_Functions.delete_info('Book_Details', 'Book_ID', Book_ID)
    

# Deleting Vendor Details
def vendor_delete():
    Vendor_ID = input('Enter Vendor ID: ')
    Library_Functions.delete_info('Book_Vendors', 'Vendor_ID', Vendor_ID)
    

# Deleting Book Category
def book_category_delete():
    Book_Category_ID = input('Enter Book Category ID: ')
    Library_Functions.delete_info('Book_Category', 'Book_Category_ID', Book_Category_ID)
    

# Updating Book Details
def update_book():
    Book_ID = input('Enter Book ID: ')
    flag = 0
    while True:
        print('Press (1)>>>>> Book Name')
        print('Press (2)>>>>> Book Publication')
        print('Press (3)>>>>> Book Author')
        print('Press (4)>>>>> Date Of Purchase')
        print('Press (5)>>>>> Book Status')
        print('Press (6)>>>>> Book Condition')
        print('Press (7)>>>>> Book Cost')
        print('Press (0)>>>>> BACK\n')
        book_info = int(input('>>>>> '))
        x = ['*', 'Book_Name', 'Book_Publication', 'Book_Author', 'Date_Of_Purchase', 'Book_Status', 'Book_Condition', 'Book_Cost']
        if (book_info < 0 or book_info > 7):
            Library_Functions.clear()
            print('Invalid Choice!!!\n\n')
            continue
        elif book_info == 0:
            if flag == 0:
                Library_Functions.clear()
                print('Book Update Cancelled!!!\n\n')
                break
            else:
                Library_Functions.clear()
                print('Updation Complete!!!\n\n')
                break
        else:
            value = input('Input Value: ')
            Library_Functions.update_info('Book_Details', x[book_info], value, 'Book_ID', Book_ID)
            flag = 1
            Library_Functions.clear()
            print(x[book_info] + ' Updated Successfully!!!\n\n')
            
            
# Updating Vendor Details
def update_vendor():
    Vendor_ID = input('Enter Vendor ID: ')
    flag = 0
    while True:
        print('Press (1)>>>>> Vendor Name')
        print('Press (2)>>>>> Vendor Address')
        print('Press (3)>>>>> Vendor Phone')
        print('Press (4)>>>>> Vendor E-MAIL')
        print('Press (0)>>>>> BACK')
        Vendor_info = int(input('>>>>> '))
        x = ['*', 'Vendor_Name', 'Vendor_Address', 'Vendor_Phone', 'Vendor_EMAIL']
        if (Vendor_info < 0 or Vendor_info > 4):
            Library_Functions.clear()
            print('Invalid Choice!!!\n\n')
            continue
        elif Vendor_info == 0:
            if flag == 0:
                Library_Functions.clear()
                print('Vendor Update Cancelled!!!\n\n')
                break
            else:
                Library_Functions.clear()
                print('Updation Complete!!!\n\n')
                break
        else:
            value = input('Input Value: ')
            Library_Functions.update_info('Book_Vendors', x[Vendor_info], value, 'Vendor_ID', Vendor_ID)
            flag = 1
            Library_Functions.clear()
            print(x[Vendor_info] + ' Updated Successfully!!!\n\n')
            
            
            
# Updating Book Category Details
def update_book_category():
    Book_Category_ID = input('Enter Book Category ID: ')
    flag = 0
    while True:
        print('Press (1)>>>>> Book Category')
        print('Press (2)>>>>> Category Issue Cost')
        print('Press (0)>>>>> BACK')
        cat_info = int(input('>>>>> '))
        x = ['*', 'Book_Category', 'Category_Issue_Cost']
        if (cat_info < 0 or cat_info > 2):
            Library_Functions.clear()
            print('Invalid Choice!!!\n\n')
            continue
        elif cat_info == 0:
            if flag == 0:
                Library_Functions.clear()
                print('Book Category Update Cancelled!!!\n\n')
                break
            else:
                Library_Functions.clear()
                print('Updation Complete!!!\n\n')
                break
        else:
            value = input('Input Value: ')
            Library_Functions.update_info('Book_Category', x[cat_info], value, 'Book_Category_ID', Book_Category_ID)
            flag = 1
            Library_Functions.clear()
            print(x[cat_info] + ' Updated Successfully!!!\n\n')