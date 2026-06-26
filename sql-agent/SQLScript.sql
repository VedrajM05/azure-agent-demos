CREATE DATABASE SalesAnalyticsDB;
GO

CREATE TABLE Products
(
    ProductId INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2)
);

CREATE TABLE Customers
(
    CustomerId INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

CREATE TABLE Orders
(
    OrderId INT PRIMARY KEY,
    CustomerId INT,
    ProductId INT,
    Quantity INT,

    FOREIGN KEY (CustomerId)
        REFERENCES Customers(CustomerId),

    FOREIGN KEY (ProductId)
        REFERENCES Products(ProductId)
);

INSERT INTO Products VALUES
(1,'Laptop',800),
(2,'Keyboard',50),
(3,'Mouse',25),
(4,'Monitor',300),
(5,'Headphones',100);

INSERT INTO Customers VALUES
(1,'John'),
(2,'Sarah'),
(3,'Mike'),
(4,'Emma');

INSERT INTO Orders VALUES
(1,1,1,2),
(2,1,2,5),
(3,2,4,1),
(4,3,1,1),
(5,4,5,3),
(6,2,3,10),
(7,4,2,4);

SELECT * FROM Products;
SELECT * FROM Customers;
SELECT * FROM Orders;


SELECT @@SERVERNAME;

