USE Public_Library;

CREATE TABLE Book_Vendors (
	Vendor_ID VARCHAR(20) NOT NULL PRIMARY KEY,
    Vendor_Name VARCHAR(50) NOT NULL,
    Vendor_Address VARCHAR(50) DEFAULT NULL,
    Vendor_Phone BIGINT DEFAULT NULL,
    Vendor_EMAIL VARCHAR(50) DEFAULT NULL
);

CREATE TABLE Book_Details (
	Book_ID VARCHAR(20) NOT NULL PRIMARY KEY,
    Book_Name VARCHAR(255) NOT NULL,
    Book_Publication VARCHAR(255) DEFAULT NULL,
    Book_Author VARCHAR(255) DEFAULT NULL,
    Date_Of_Purchase DATE DEFAULT NULL,
    Book_Status VARCHAR(50) DEFAULT NULL,
    Book_Condition VARCHAR(50) DEFAULT NULL,
    Book_Cost INT DEFAULT NULL,
    Book_Category_ID VARCHAR(20) NOT NULL,
    Vendor_ID VARCHAR(20) NOT NULL
);

CREATE TABLE Book_Category (
	Book_Category_ID VARCHAR(20) NOT NULL PRIMARY KEY,
    Book_Category VARCHAR (255),
    Category_Issue_Cost INT
);

ALTER TABLE Book_Details ADD FOREIGN KEY (Book_Category_ID) REFERENCES Book_Category(Book_Category_ID) ON UPDATE CASCADE;
ALTER TABLE Book_Details ADD FOREIGN KEY (Vendor_ID) REFERENCES Book_Vendors(Vendor_ID) ON UPDATE CASCADE;