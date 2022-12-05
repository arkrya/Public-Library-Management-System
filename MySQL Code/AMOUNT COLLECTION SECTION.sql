USE Public_Library;

CREATE TABLE Book_Purchase (
	Purchase_ID VARCHAR (20) NOT NULL PRIMARY KEY,
    Book_ID VARCHAR(10),
    Vendor_ID VARCHAR(10),
    Book_Category_ID VARCHAR(100) DEFAULT NULL,
    Date_Of_Purchase DATE,
    P_Amount INT  DEFAULT NULL
);

CREATE TABLE Book_Issue_Amount (
	BIA_ID VARCHAR (20)NOT NULL PRIMARY KEY,
    Issue_ID VARCHAR(20) NOT NULL,
    Return_ID VARCHAR (20) NOT NULL,
    Return_Date DATE,
    Issue_Amount INT,
    Fine INT,
	Total_Amount INT
);



ALTER TABLE Book_Issue_Amount 
	ADD FOREIGN KEY (Return_ID) REFERENCES Book_Return(Return_ID);

ALTER TABLE Book_Purchase 
	ADD FOREIGN KEY (Vendor_ID) REFERENCES Book_Vendors(Vendor_ID);

ALTER TABLE Book_Purchase 
	ADD FOREIGN KEY (Book_Category_ID) REFERENCES Book_Category(Book_Category_ID);    
    
ALTER TABLE Book_Issue_Amount
	ADD FOREIGN KEY (Issue_ID) REFERENCES Book_Issue(Issue_ID);