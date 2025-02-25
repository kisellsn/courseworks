--1--
CREATE LOGIN employee1 WITH PASSWORD='EMPLOYEE1';
CREATE USER employee_1 FOR LOGIN employee1;
CREATE ROLE EMPLOYEE;
GRANT SELECT,INSERT ON Tour TO EMPLOYEE;
GRANT SELECT,INSERT ON Customer TO EMPLOYEE;
GRANT SELECT,INSERT ON Sale_agreement TO EMPLOYEE;
GRANT SELECT,INSERT ON Return_agreement TO EMPLOYEE;
GRANT SELECT ON Country TO EMPLOYEE;
GRANT SELECT ON Type_of_tour TO EMPLOYEE;
GRANT SELECT ON Type_of_food TO EMPLOYEE;
GRANT SELECT ON Hotel TO EMPLOYEE;
GRANT SELECT ON Discount TO EMPLOYEE;
ALTER ROLE EMPLOYEE ADD MEMBER employee_1;	

--2--
CREATE LOGIN employer1 WITH PASSWORD='EMPLOYER1';
CREATE USER employer_1 FOR LOGIN employer1;
CREATE ROLE EMPLOYER;
GRANT SELECT ON Sale_agreement TO EMPLOYER;
GRANT SELECT ON Return_agreement TO EMPLOYER;
GRANT SELECT ON success_of_emlpoyee TO EMPLOYER
GRANT SELECT,UPDATE,INSERT,DELETE ON Employee to EMPLOYER;
ALTER ROLE EMPLOYER ADD MEMBER employer_1;

CREATE VIEW success_of_emlpoyee
AS
select TOP(5)
      E.full_name, COUNT(S.employee_id) as 'Count_of_sales'
from Employee E, Sale_agreement S 
where E.id=S.employee_id 
GROUP BY  E.full_name
ORDER BY COUNT(S.employee_id) DESC
GO
SELECT * FROM success_of_emlpoyee