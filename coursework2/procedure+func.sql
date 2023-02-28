--1--
CREATE FUNCTION  select_tour(@DATE1 datetime, @DATE2 datetime)
RETURNS TABLE
AS
RETURN
(
    SELECT T.tour_name, T.departure_date, C.country_name
    FROM Tour T  
	JOIN Country AS C ON C.id = T.country_id
    WHERE T.departure_date BETWEEN @DATE1 and  @DATE2
);
GO
SELECT  * from select_tour (CONVERT(DATETIME,'2022-01-06 00:00:00.000'),CONVERT(DATETIME,'2023-03-08 00:00:00.000'));
--2--
CREATE FUNCTION  price_of_tour(@ID int)
RETURNS money
WITH EXECUTE AS CALLER
AS
BEGIN
     DECLARE @Price money;
     SELECT @Price = price FROM Tour WHERE id=@ID;
	 RETURN(@Price);
END;
GO
SELECT dbo.price_of_tour(1);

--3--
CREATE PROCEDURE tour_info AS
BEGIN
    SELECT  T.tour_name,T.departure_date ,O.type_of_tour, T.price, C.country_name, H.hotel_name
    FROM Tour T
	JOIN Country AS C ON C.id = T.country_id
	JOIN Hotel AS H ON H.id = T.hotel_id
	JOIN Type_of_tour AS O ON O.id = T.type_of_tour_id
END;

EXEC tour_info

--4--
CREATE PROCEDURE count_of_customers 
AS    
DECLARE @output NVARCHAR(150);      
DECLARE @totalCustomers INT;    
SET @totalCustomers=( SELECT Count(ID) FROM Customer);    
IF @totalCustomers > 400        
SET @output = 'More then 100 customers';    
ELSE        
SET @output = 'Less then 100 customers';    
SELECT @output; 
GO
EXEC count_of_customers
--5--

ALTER PROCEDURE price_increase  @percent INT 
AS   
UPDATE Tour   
SET price = price+(@percent/100*price)
GO
DECLARE @percent INT 
Set @percent=0.1 
EXEC price_increase   @percent

