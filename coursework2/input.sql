INSERT INTO Country
VALUES
('Spain'),
('Italy'),
('France'),
('Poland');

INSERT INTO Discount
VALUES
('Large family', 15),
('Invalidity', 20),
('On a Ukrainian passport', 10);


INSERT INTO Hotel
VALUES
('Qubus Hotel Gdansk', '4 star', 'motel'),
('Hanza Hotel','2 star', 'youth hotel'),
('Old Town','3 star', 'pension'),
('Novotel Gdansk Centrum', '3 star', 'beach houses'),
('IBIS','5 star', 'apartments');


INSERT INTO Type_of_food
VALUES
('BB(1)'),
('HB(2)'),
('FB(3)'),
('All inclusive');


INSERT INTO Type_of_tour
VALUES
('sightseeing'),
('of wedding'),
('eco'),
('extreme');

INSERT INTO Customer
VALUES
('Halima Pitts', '4670655974', '467065597'),
('Taya Saunders','3049264639', '304926463'),
('Keane Nunez','8065315344', '806531534'),
('Marjorie Nguyen', '2340424936', '234042493'),
('Dewey Glass','9354652593', '935465259');

INSERT INTO Employee
VALUES
('Haaris Todd', '6291355931'),
('Daniyal Macdonald', '3440655565'),
('Tanya Lara', '0861774809');

INSERT INTO Tour
VALUES
('T1',2023-01-14,4,'op2','Lviv',4,3, 4,4, 1, 4000),
('T2',2022-03-01,4,'op3','Gdansk',4,15, 4,1,NULL, 92233),
('T3',2020-10-22,4,'op4','Kherson',1,10, 1,1,NULL, 20368),
('T4',2020-05-06,4,'op5','Odesa',4,14, 4,2, 2,2500);

INSERT INTO Sale_agreement
VALUES
(2023-01-14,4,11,2,1),
(2022-03-01,1,12,3,2),
(2020-10-22,3,13,1,3),
(2020-10-22,2,14,1,4),
(2020-05-06,4,15,1,1);

INSERT INTO Return_agreement
VALUES
(2023-01-14,1,'for family reason',11,2,1),
(2022-03-01,1,'for family reason',12,3,2),
(2020-10-22,3,'for family reason',13,1,3),
(2020-10-22,2,'for family reason',14,1,4),
(2020-05-06,2,'for family reason',15,1,1);

select * from Tour;
select * from Customer;
select * from Employee;
select * from Sale_agreement;
