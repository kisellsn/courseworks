CREATE VIEW success_of_emlpoyee
AS
SELECT TOP(5)
      E.full_name, COUNT(S.employee_id) as 'Count_of_sales'
from Employee E, Sale_agreement S 
where E.id=S.employee_id 
GROUP BY  E.full_name
ORDER BY COUNT(S.employee_id) DESC
GO

CREATE VIEW amount_of_emlpoyee_agreement
AS
SELECT E.full_name, SUM(T.price*S.number_of_sale) as 'Profit'
from Employee E
JOIN Sale_agreement as S ON E.id=S.employee_id
JOIN Tour as T ON S.tour_id=T.id
Group BY E.full_name
GO
SELECT * FROM amount_of_emlpoyee_agreement