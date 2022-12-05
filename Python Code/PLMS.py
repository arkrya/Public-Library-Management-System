'''
Welcome to the main screen of Public Library Management System (PLMS)
'''

import Members_Section, Book_Section, Issue_Return_Section, Library_Functions


while True:
    print('*'*100)
    print('*' + ' '*36 + 'Welcome To Public Library' + ' '*37 + '*')
    print('*'*100)
    
    print('\n\n\n\n')
    print('Press (1)          MEMBERS')
    print('Press (2)          BOOKS')
    print('Press (3)          ISSUE BOOK')
    print('Press (4)          RETURN BOOK')
    print('\nPress (0)          QUIT')
    
    choice = int(input('\n\n          Enter Choice:  '))
    if choice == 1:
        Library_Functions.clear()
        while True:
            print('\nPress (1)          VIEW MEMBERS')
            print('Press (2)          ADD MEMBER')
            print('Press (3)          REMOVE MEMBER')
            print('Press (4)          UPDATE MEMBER')
            print('\nPress (0)          BACK')
            
            mem_choice = int(input('\n\n          Enter Choice:  '))
            if mem_choice == 1:
                Library_Functions.clear()
                Library_Functions.view('SELECT * FROM Members')
                
            elif mem_choice == 2:
                Library_Functions.clear()
                Members_Section.members_info()
            
            elif mem_choice == 3:
                Library_Functions.clear()
                M_ID = input('\n\nEnter Member ID:  ')
                Members_Section.delete_info(M_ID)
                print('\n\n')
            
            elif mem_choice == 4:
                Library_Functions.clear()
                Members_Section.update_member_info()
                print('\n\n')
                
            elif mem_choice == 0:
                Library_Functions.clear()
                break
            
            else:
                Library_Functions.clear()
                print('Invalid Choice!!!\n\n')
    
    elif choice == 2:
        Library_Functions.clear()
        while True:
            print('\nPress (1)          VIEW BOOKS')
            print('Press (2)          ADD BOOK')
            print('Press (3)          REMOVE BOOK')
            print('Press (4)          UPDATE BOOK')
            print('\nPress (0)          BACK')
            
            book_choice = int(input('\n\n          Enter Choice:  '))
            if book_choice == 1:
                Library_Functions.clear()
                while True:
                    print('\nPress (1)          VIEW ALL BOOKS')
                    print('Press (2)          CATEGORY WISE BOOKS')
                    print('Press (3)          AVAILABLE BOOK')
                    print('Press (4)          ISSUED BOOK')
                    print('Press (5)          DAMAGED BOOK')
                    print('\nPress (0)          BACK')
                    
                    view_book_choice = int(input('\n\n          Enter Choice:  '))
                    if view_book_choice == 1:
                        Library_Functions.clear()
                        Library_Functions.view("SELECT * FROM Book_Details")
                        
                    elif view_book_choice == 2:
                        Library_Functions.clear()
                        Library_Functions.view('''SELECT Book_Category.Book_Category_ID, Book_Category.Book_Category, Book_Details.Book_ID, Book_Details.Book_Name 
                                               from Book_Category 
                                               inner join Book_Details on 
                                               Book_Category.Book_Category_ID = Book_Details.Book_Category_ID''')
                    
                    elif view_book_choice == 3:
                        Library_Functions.clear()
                        Library_Functions.view("SELECT * from Book_Details where (Book_Status = 'New' or Book_Status = 'Available')")
                        
                    elif view_book_choice == 4:
                        Library_Functions.clear()
                        Library_Functions.view("SELECT * from Book_Details where Book_Status = 'Issued'")
                        
                    elif view_book_choice == 5:
                        Library_Functions.clear()
                        Library_Functions.view("SELECT * from Book_Details where Book_Condition = 'Damaged'")
                    
                    elif view_book_choice == 0:
                        break
                    
                    else:
                        Library_Functions.clear()
                        print('Invalid Choice!!!\n\n')
                    
            elif book_choice == 2:
                Library_Functions.clear()
                Book_Section.book_info()
                
            elif book_choice == 3:
                Library_Functions.clear()
                Book_Section.book_delete()
                
            elif book_choice == 4:
                Library_Functions.clear()
                Book_Section.update_book()
            
            elif book_choice == 0:
                Library_Functions.clear()
                break
            
            else:
                Library_Functions.clear()
                print('\nInvalid Choice!!!\n\n')
    
    
    elif choice == 3:
        Library_Functions.clear()
        while True:
            print('\nPress (1)          ISSUE BOOK')
            print('Press (2)          VIEW LAST ISSUE RECORD')
            print('Press (3)          DELETE LAST ISSUE RECORD')
            print('Press (4)          UPDATE LAST ISSUE RECORD')
            print('\nPress (0)          BACK')
            
            issue_choice = int(input('\n\n          Enter Choice:  '))
            if issue_choice == 1:
                Library_Functions.clear()
                Issue_Return_Section.book_issue()
            
            elif issue_choice == 2:
                Library_Functions.clear()
                ID = Library_Functions.last_ID('Issue_ID', 'Book_Issue')
                Library_Functions.view("SELECT * FROM Book_Issue WHERE Issue_ID = '"+ ID + "'")
            
            elif issue_choice == 3:
                Library_Functions.clear()
                Issue_Return_Section.delete_last_issue()
                
            elif issue_choice == 4:
                Library_Functions.clear()
                Issue_Return_Section.update_last_issue()
                
            elif issue_choice == 0:
                Library_Functions.clear()
                break
            
            else:
                Library_Functions.clear()
                print('\nInvalid Choice!!!\n\n')
                
    elif choice == 4:
        Library_Functions.clear()
        while True:
            print('\nPress (1)          RETURN BOOK')
            print('Press (2)          VIEW LAST RETURN RECORD')
            print('Press (3)          DELETE LAST RETURN RECORD')
            print('Press (4)          UPDATE LAST RETURN RECORD')
            print('\nPress (0)          BACK')
            
            return_choice = int(input('\n\n          Enter Choice:  '))
            if return_choice == 1:
                Library_Functions.clear()
                Issue_Return_Section.book_return()
            
            elif return_choice == 2:
                Library_Functions.clear()
                ID = Library_Functions.last_ID('Return_ID', 'Book_Return')
                Library_Functions.view("SELECT * FROM Book_Return WHERE Return_ID = '"+ ID + "'")
            
            elif return_choice == 3:
                Library_Functions.clear()
                Issue_Return_Section.delete_last_return()
                
            elif return_choice == 4:
                Library_Functions.clear()
                Issue_Return_Section.update_last_return()
                
            elif return_choice == 0:
                Library_Functions.clear()
                break
            
            else:
                Library_Functions.clear()
                print('\nInvalid Choice!!!\n\n')
    
    elif choice == 0:
        Library_Functions.clear()
        break
    
    else:
        Library_Functions.clear()
        print('Invalid Choice!!!\n\n')