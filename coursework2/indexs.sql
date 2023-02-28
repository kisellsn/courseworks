SET STATISTICS TIME ON;
GO
SELECT E.full_name AS '��������', C.full_name AS '�볺��',  C.phone_number AS '����� �������� �볺���'
FROM Customer C,Employee E,Sale_agreement S
WHERE S.employee_id=E.id AND S.customer_id=C.id AND S.id = 10

CREATE INDEX IX_1 ON Employee(id, full_name, phone_number)
CREATE INDEX IX_2 ON Customer(id, full_name, phone_number, passport)

DROP INDEX IX_2  ON Customer;  
DROP INDEX IX_1  ON Employee;  