'''
This section is for registering new users to the database with all the following informations.
A valid user should have:
    Name, Gender, DOB(YYYY-MM-DD), Address, Contact Number, E-Mail ID
There are some optional details too. e.g:
    Card Details , ID Card
'''
import Library_Functions


# Basic Info Section

def members_info():
    Name = input('Member Name: ')
    Gender = input('Gender    M/F: ')
    DOB = input('DOB >>> (YYYY-MM-DD): ')
    Address = input('Address: ')
    Contact_Num = int(input('Contact Number: '))
    E_mail = input('E-Mail Address: ')
    Library_Functions.clear()
    
    # Additional Info Section
    # For Card
    cflag = 0              # To make choice for entering data in Card Details Table
    Card_Choice = input('Do you have a card?   Y/N: ')
    if (Card_Choice == 'Y' or Card_Choice == 'y'):
        Card_Type = input('Card Type: ')
        Card_Bank = input('Bank Name:  ')
        Card_Number = int(input('Card Number: '))
        Card_Expiry = input('Card Expiry Year: ')
        cflag = 1
    else:
        Card_Type = None
        Card_Bank = None
        Card_Number = None
        Card_Expiry = None
    Library_Functions.clear()
        
    # For ID Card
    iflag = 0              # To make choice for entering data in Identity Details Table
    ID_Proof = input('Do you have an ID?   Y/N:  ')
    if ID_Proof == 'Y' or ID_Proof == 'y':
        ID_Type = input('ID Type: ')
        ID_Number = input('ID Number: ')
        iflag = 1
    else:
        ID_Type = None
        ID_Number = None
    Library_Functions.clear()
            
        
    try:
        # Entering Data To Database
        
        mydb, mycursor = Library_Functions.sqlConnect()
        
        x = Library_Functions.Null_ID('Members')
        if x == False:
            M_ID = 'MID0000001'
        elif x == True:
            M_ID = Library_Functions.Next_ID('M_ID', 'Members')
            
            
        # Entering Data Into Card_Details Table
        
        if cflag == 1:
            sql1 = "INSERT INTO Card_Details (Card_Number, Card_Type, Card_Bank, Card_Expiry) VALUES (%s, %s, %s, %s)"
            val1 = (Card_Number, Card_Type.upper(), Card_Bank.upper(), Card_Expiry)
            mycursor.execute(sql1, val1)
            
            mydb.commit()
        
        # Entering Data Into ID_Proof
        
        if iflag == 1:
            sql2 = "INSERT INTO M_Identity (ID_Number, ID_Type) VALUES (%s, %s)"
            val2 = (ID_Number, ID_Type)
            mycursor.execute(sql2, val2)
            
            mydb.commit()
        
        # Entering data into MEMBERS table.
        
        sql4 = "INSERT INTO Members (M_ID, M_Name, Gender, DOB, Address, Phone, E_MAIL, Card_Number, ID_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val4 = (M_ID, Name.capitalize(), Gender.upper(), DOB, Address.capitalize(), Contact_Num, E_mail, Card_Number, ID_Number)
        mycursor.execute(sql4, val4)
        
        mydb.commit()
        print(Name + ' is now a member!!\n\n')
    except:
        print("\nMember hasn't been added\n\n")
    mycursor.close()
    mydb.close()

# Deleting Info Of Member

def delete_info(M_ID):
    mydb, mycursor = Library_Functions.sqlConnect()
    
    try:
        # Temporary data retrival
        sql5 = "SELECT Card_Number, ID_Number FROM Members WHERE ( M_ID = '" + M_ID + "' )"  
        mycursor.execute(sql5)
        myresult = mycursor.fetchall()
        z = []
        for x in myresult:
            for y in x:
                z.append(y)
        # Deleting from Members Table
        Library_Functions.delete_info('Members', 'M_ID', M_ID)
        
        # Deleting from Card Details
        if z[0] is not None:
            Library_Functions.delete_info('Card_Details', 'Card_Number', z[0])
        
        # Deleting from M_Identity Table
        if z[1] is not None:
            Library_Functions.delete_info('M_Identity', 'ID_Number', z[1])
        
        print('Record Deleted Sucsessfully')
    except:
        print('Error in deleting...')
    mycursor.close()
    mydb.close()

# Updating Info Of Member

def update_member_info():
    x = True
    while x == True:
        ID_value = input('Enter Member ID: ')
        id_check = Library_Functions.search_specifc('M_ID', 'Members', 'M_ID', ID_value)
        if id_check is not None:
            Library_Functions.clear()
            flag = 0
            while True:
                print('Press (1)>>>>> General Info')
                print('Press (2)>>>>> Card Details')
                print('Press (3)>>>>> ID Card Details')
                print('Press (0)>>>>> QUIT')
                main_choice = int(input('>>>>> '))
                
                if main_choice == 1:
                    Library_Functions.clear()
                    while True:
                        print('Press (1)>>>>> Member Name')
                        print('Press (2)>>>>> Gender')
                        print('Press (3)>>>>> Date Of Birth')
                        print('Press (4)>>>>> Address')
                        print('Press (5)>>>>> Phone Number')
                        print('Press (6)>>>>> E-Mail ID')
                        print('Press (0)>>>>> BACK')
                        gen_info = int(input('>>>>> '))
                        data = ['*', 'M_Name', 'Gender', 'DOB', 'Address', 'Phone', 'E_MAIL']
                        if (gen_info < 0 or gen_info > 6):
                            Library_Functions.clear()
                            print('Invalid Choice!!!\n\n')
                            continue
                        elif gen_info == 0:
                            Library_Functions.clear()
                            break
                        else:
                            value = input('Input Value: ')
                            Library_Functions.update_info('Members', data[gen_info], value, 'M_ID', ID_value)
                            flag = 1
                            Library_Functions.clear()
                            print(data[gen_info] + ' Updated Successfully!!!\n\n')
                        
                            
                    
                elif main_choice == 2:
                    Library_Functions.clear()
                    while True:
                        ID_check = Library_Functions.search_specifc('Card_Number', 'Members', 'M_ID', ID_value)
                        if ID_check is not None:
                            print('Press (1)>>>>> Card Number')
                            print('Press (2)>>>>> Card Type')
                            print('Press (3)>>>>> Card Bank')
                            print('Press (4)>>>>> Card Expiry')
                            print('Press (0)>>>>> BACK')
                            crd_info = int(input('>>>>> '))
                            data = ['*', 'Card_Number', 'Card_Type', 'Card_Bank', 'Card_Expiry']
                            if (crd_info < 0 or crd_info > 4):
                                Library_Functions.clear()
                                print('Invalid Choice!!!\n\n')
                                continue
                            elif crd_info == 0:
                                Library_Functions.clear()
                                break
                            else:
                                value = input('Input Value: ')
                                Library_Functions.update_info('Card_Details', data[crd_info], value, 'Card_Number', ID_value)
                                flag = 1
                                Library_Functions.clear()
                                print(data[crd_info] + ' Updated Successfully!!!\n\n')
                        else:
                            Library_Functions.clear()
                            print('Card Details Unavailable!!!\n\n')
                            break
                    
                elif main_choice == 3:
                    Library_Functions.clear()
                    while True:
                        ID_check = Library_Functions.search_specifc('ID_Number', 'Members', 'M_ID', ID_value)
                        if ID_check is not None:
                            print('Press (1)>>>>> ID Number')
                            print('Press (2)>>>>> ID Type')
                            print('Press (0)>>>>> BACK')
                            idn_info = int(input('>>>>> '))
                            data = ['*', 'ID_Number', 'ID_Type']
                            if (idn_info < 0 or idn_info > 2):
                                Library_Functions.clear()
                                print('Invalid Choice!!!\n\n')
                                continue
                            elif idn_info == 0:
                                Library_Functions.clear()
                                break
                            else:
                                value = input('Input Value: ')
                                Library_Functions.update_info('M_Identity', data[idn_info], value, 'ID_Number', ID_value)
                                flag = 1
                                Library_Functions.clear()
                                print(data[idn_info] + ' Updated Successfully!!!\n\n')
                        
                        else:
                            Library_Functions.clear()
                            print('Identity Details Unavailable!!!\n\n')
                            break
                            
                    
                elif main_choice == 0:
                    Library_Functions.clear()
                    if flag == 0:
                        print('Info Update Cancelled!!!\n\n')
                        x = False
                        break
                    else:
                        print('Updation Complete!!!\n\n')
                        x = False
                        break
                
                else:
                    Library_Functions.clear()
                    print('Invalid Choice!!!\n\n')
        else:
            Library_Functions.clear()
            print('Member Not Found!!!\n\n')
            break
                