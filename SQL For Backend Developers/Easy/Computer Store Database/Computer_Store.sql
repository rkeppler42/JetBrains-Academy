-- Create the Product table
CREATE TABLE Product (
    maker VARCHAR(50) NOT NULL,
    model INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY (model)
);

-- Create the PC table
CREATE TABLE PC (
    code INT NOT NULL,
    model INT NOT NULL,
    speed INT NOT NULL,
    ram INT NOT NULL,
    hd INT NOT NULL,
    cd VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (code),
    FOREIGN KEY (model) REFERENCES Product(model)
);

-- Create the Laptop table
CREATE TABLE Laptop (
    code INT NOT NULL,
    model INT NOT NULL,
    speed INT NOT NULL,
    ram INT NOT NULL,
    hd INT NOT NULL,
    screen INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (code),
    FOREIGN KEY (model) REFERENCES Product(model)
);

-- Create the Printer table
CREATE TABLE Printer (
    code INT NOT NULL,
    model INT NOT NULL,
    color CHAR(1) NOT NULL,
    type VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (code),
    FOREIGN KEY (model) REFERENCES Product(model)
);

/* Task 1: 

Objectives:
    - Identify printers in your inventory that are priced over $200;
    - Find the model number, type, and price of the Printer. The order of the columns matters.*/

SELECT 
    model,
    type,
    price
FROM
    Printer
WHERE
    price > 200
;