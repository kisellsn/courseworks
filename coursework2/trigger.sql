--1--

CREATE TRIGGER reminder1  
ON Customer  
AFTER UPDATE, DELETE    
AS RAISERROR ('Notify Customer Relations', 16, 10);  
GO 

--2--
ALTER TRIGGER INSTEADOF_UPDATE_Tour 
ON Tour
INSTEAD OF UPDATE 
AS
IF(UPDATE(price))
    UPDATE Tour SET price = inserted.price
    FROM INSERTED
    INNER JOIN Tour
    ON Tour.id = INSERTED.id
RETURN;
RAISERROR (N'You can not edit tour info, Transaction has been failed', 16, 10)
ROLLBACK;

CREATE TRIGGER INSTEADOF_UPDATE_Return_agreement
ON Return_agreement
INSTEAD OF UPDATE 
AS
   RAISERROR (N'You can not edit an agreement that has already been concluded Transaction has been failed', 16, 1)
   ROLLBACK;
GO

CREATE TRIGGER INSTEADOF_UPDATE_Sale_agreement
ON Sale_agreement
INSTEAD OF UPDATE
AS
   RAISERROR (N'You can not edit an agreement that has already been concluded Transaction has been failed', 16, 1)
   ROLLBACK;
GO

--3--
ALTER TABLE Customer ADD CHECK (phone_number LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
GO 
ALTER TABLE Employee ADD CHECK (phone_number LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
GO 
ALTER TABLE Customer ADD CHECK (passport LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
GO 

ALTER TABLE Sale_agreement ADD CHECK (number_of_sale BETWEEN 1 and 10)
GO 
ALTER TABLE Return_agreement ADD CHECK (number_of_sale BETWEEN 1 and 10)
GO 
ALTER TABLE Tour ADD CHECK (price >= 100)
GO 

ALTER TABLE Sale_agreement ADD CHECK (date_of_sale >= convert(datetime,'2000-01-01 00:00:00.000'))
GO 
ALTER TABLE Return_agreement ADD CHECK (date_of_sale >= convert(datetime,'2000-01-01 00:00:00.000'))
GO 
ALTER TABLE Tour ADD CHECK (departure_date >= convert(datetime,'2000-01-01 00:00:00.000'))
GO 
