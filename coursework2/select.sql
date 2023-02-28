--���������� ��� ����, ���� ���� � �������� ��������--
select T.tour_name as 'Name',Tt.type_of_tour as 'Type',T.departure_date as 'Date', C.country_name as 'Country of destination',T.number_of_days as 'Days', T.price as 'Price'
from Tour T
JOIN Country as C ON C.id=T.country_id
JOIN Type_of_tour as Tt ON Tt.id=T.type_of_tour_id
where price between 2000 and 7000
GO
--���������� ��� ����, ����� ����������� ���� ���������� � ������� � ��������� �������--
select T.tour_name as 'Name',Tt.type_of_tour as 'Type',T.departure_date as 'Date', C.country_name as 'Country of destination',T.number_of_days as 'Days', T.price as 'Price'
from Tour T
JOIN Country as C ON C.id=T.country_id
JOIN Type_of_tour as Tt ON Tt.id=T.type_of_tour_id
where C.country_name IN ('Poland', 'Spain','Italy')
GO
--������ ������ ��������-����� �����(������� � �������) ������������ �� ���������.--
SELECT E.full_name, SUM((T.price-T.price*D.size/100)*S.number_of_sale) as 'Profit'
from Employee E
JOIN Sale_agreement as S ON E.id=S.employee_id
JOIN Tour as T ON S.tour_id=T.id
JOIN Discount as D ON T.discount_id=D.id
Group BY E.full_name
ORDER BY SUM((T.price-T.price*D.size/100)*S.number_of_sale) DESC
GO
--��������� ����� - �ᒺ������ ������, �� ��������� �볺���/�������� � �� ������. --
SELECT full_name, phone_number, '�볺��' AS '������' FROM Customer
UNION
SELECT full_name, phone_number, '��������' AS '������' FROM Employee
--5. ����������� ������� ��������� ���� � ������� ���� �� �볺����. --
SELECT C.full_name, COUNT(S.customer_id) as 'Count_of_agreement', SUM(S.number_of_sale) as 'Count_of_tour'
from Customer C, Sale_agreement S 
where C.id=S.customer_id 
GROUP BY  C.full_name
ORDER BY COUNT(S.customer_id) DESC, SUM(S.number_of_sale) DESC
GO
--6. ����������� ����.--
SELECT C.country_name AS '�����', SUM(S.number_of_sale) AS 'ʳ������ ��������' 
FROM Tour T
JOIN Sale_agreement as S ON T.id=S.tour_id
JOIN Country as C ON C.id=T.country_id
GROUP BY country_name
--7. ������ ������ ��� �� ������� � ���� ������� ������.--
SELECT T.id,T.tour_name,DATEDIFF(DAY, S.date_of_sale, T.departure_date) AS 'ʳ������ ��� �� �������� � ��������'
FROM Tour T,Sale_agreement S
WHERE S.tour_id=T.id
--8. �������� ���������� ����� ��� ������� ������ ��������������� ���� --
SELECT S.id as 'id �����',S.date_of_sale as '����', C.full_name as '��*� �볺���', E.full_name as '��*� ���������', T.tour_name as '����� ����'
FROM Sale_agreement S
INNER JOIN Tour as T ON T.id = S.tour_id 
INNER JOIN Customer as C ON C.id = S.customer_id 
INNER JOIN Employee E ON E.id =S.employee_id AND S.number_of_sale IN (SELECT MAX(number_of_sale) FROM Sale_agreement)
--9. �������� ���������� ��� ������� ����, �� ����� ������--
SELECT C.full_name, C.phone_number, S.date_of_sale, T.tour_name, D.size as 'Discount %' ,D.discount_name as 'Reason'
FROM  Customer C
INNER JOIN Sale_agreement as S ON C.id = S.customer_id
INNER JOIN Tour as T ON T.id = S.tour_id AND T.discount_id IN (SELECT discount_id FROM Tour WHERE discount_id IS NOT NULL)
INNER JOIN Discount as D ON D.id = T.discount_id
--10. ����� �񳺿 ������� ���������� ��� ���� ������ �볺���� � ����� �� ����. --
DECLARE @Customer_name varchar(250)
SET @Customer_name='Dewey Glass'
SELECT T.tour_name, T.price, T.departure_date, T.departure_city, T.operator, T.number_of_days, cn.country_name, H.hotel_name
FROM Tour T
JOIN Country as cn ON cn.id = T.country_id
JOIN Hotel as H ON H.id = T.hotel_id
WHERE T.id IN (SELECT S.tour_id FROM Sale_agreement S WHERE S.customer_id = (select C.id from Customer C where C.full_name=@Customer_name))
-- ���� ���� ����, �� �� ����� ������, ����� �������� �� ������������� ������. --
SELECT tour_name as 'Tour', country_name as 'Country', hotel_name+', '+hotel_class+', '+type_of_hotel AS 'Hotel'
FROM Hotel,Tour,Country 
WHERE hotel_id=Hotel.id AND country_id=Country.id AND discount_id is NULL
--12. �������� ����� �볺���, ���� �������� ����� ���� �����.--
SELECT C.full_name as 'Customer', COUNT(S.customer_id) as 'Count_of_sales'
FROM Sale_agreement S, Customer C
WHERE S.customer_id=C.id
GROUP BY C.full_name 
Having COUNT(S.customer_id)>1
--13. �������� ����� ���������, ���� �������� ����� ���� �����.--
SELECT ROW_NUMBER() OVER( ORDER BY COUNT(S.employee_id)) AS Position, C.full_name as 'Employee', COUNT(S.employee_id) as 'Count_of_sales'
FROM Sale_agreement S, Employee C
WHERE S.employee_id=C.id
GROUP BY C.full_name 
Having COUNT(S.employee_id)>1
--14. ������ ��� ��������� � ������� �������� �� �������� ����� ����� ������ �� ���� ���.--
SELECT C.full_name,SUM(S.number_of_sale) as 'Purchased tickets', SUM(R.number_of_sale) as 'Returned tickets'
from Employee C 
JOIN Return_agreement as R ON C.id=R.employee_id
JOIN Sale_agreement as S ON S.id=R.sale_id
Group BY C.full_name

--15. ������ ���� ������ ��������� ������� ����� ���������� ������/��� ������.--
SELECT E.full_name as 'Employee', SUM(T.price*R.number_of_sale) as 'Refunds'
from Customer E
INNER JOIN Return_agreement as R ON E.id=R.customer_id
INNER JOIN Tour as T ON R.tour_id=T.id
Group BY E.full_name
--16. ������ ��� ��� ���, ������ �� ����� ���� ������� � ������� ����.--
DECLARE @date_for_search date
SET @date_for_search=convert(date,'2023-01-10')
SELECT T.tour_name, C.country_name, T.price
FROM Tour T
JOIN Country as C ON C.id=T.country_id
WHERE T.id = (select S.tour_id from Sale_agreement S where S.date_of_sale=@date_for_search)
--17.  �������� ����� �볺��� � ������ ������ ������ ���� ����� � ����.--
SELECT C.full_name, S.number_of_sale, CN.country_name
FROM Sale_agreement S
INNER JOIN Customer C ON S.customer_id=C.id
INNER JOIN Tour T ON T.id=S.tour_id
INNER JOIN Country CN ON CN.id=T.country_id

--18. �� ����� ��� ������� ������ � �������� ���������� ��� �� ����������.--
SELECT Sale_agreement.*, Return_agreement.* 
FROM Sale_agreement 
LEFT  JOIN Return_agreement ON Sale_agreement.ID = Return_agreement.sale_id
UNION 
SELECT Sale_agreement.*, Return_agreement.* 
FROM Sale_agreement 
RIGHT  JOIN Return_agreement ON Sale_agreement.ID = Return_agreement.sale_id
--19. ����������� ���� �� ���� ������� �� ����, � ������� ��� ����� 10.--
SELECT T.tour_name, T.departure_date, C.country_name, T.number_of_days
FROM Tour T
JOIN Country C ON C.id=T.country_id
WHERE T.departure_city='Lviv' and T.number_of_days between 1 and 10

--20. ��� 3 ����������� ���� �� �����/�������� ������� �������, �� �� ALL INCLUSIVE--
SELECT TOP(3)
      T.tour_name, T.operator, T.number_of_days, T.departure_date,T.departure_city,T.price
FROM Tour T
JOIN Hotel H ON H.id=T.hotel_id
JOIN Type_of_food F ON F.id=T.food_id
WHERE H.type_of_hotel IN ('3 star','4 star') AND F.type_of_food='All inclusive'
ORDER BY price
