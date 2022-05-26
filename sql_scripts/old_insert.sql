insert into polls_tradepointtype(id, name) values
	(1,'Department Store'),
	(2,'Store'),
	(3,'Kiosk'),
	(4,'Tray');

    insert into TradePoint(Name, PointType, PointSize, RentPayment, UtilitiesPayment, PointCounterAmount) values
	('Sol', 1, 250, 5000, 500, 27),
    ('Luna', 1, 500, 10000, 250, 63),
    ('Mercurius', 2, 100, 3000, 200, 10),
    ('Venus', 2, 70, 1000, 100, 4),
    ('Terra', 2, 90, 1200, 120, 6),
    ('Mars', 3, 6, 600, 50, 1),
    ('Jupiter', 3, 5, 500, 70, 1),
    ('Saturnus', 3, 5, 500, 50, 1),
    ('Uranus', 4, null, null, null, null),
    ('Neptunus', 4, null, null, null, null),
    ('Pluto', 4, null, null, null, null);


insert into SomeStore(TradePointID) values
	(1),
    (2),
    (3),
    (4),
	(5);

insert into DepartmentStore(TradePointID) values
	(1),
    (2);

insert into Store(TradePointID) values
	(3),
    (4),
    (5);

insert into Product(Name, Description) values
    ('salmon', ''),
    ('trout', ''),
    ('cod', ''),
    ('tuna', ''),
    ('sole', ''),
    ('fish steak', ''),
    ('fish fillet', ''),
    ('smoked fish', ''),
    ('caviar', ''),
    ('white bread', ''),
    ('whole-wheat bread', ''),
    ('rye bread', ''),
    ('shrimp', ''),
    ('crab', ''),
    ('oysters', ''),
    ('apple', ''),
    ('pear', ''),
    ('apricot', ''),
    ('peach', ''),
    ('nectarine', ''),
    ('plum', ''),
    ('grapes', ''),
    ('cherry', ''),
    ('sweet cherry', ''),
    ('lemon', ''),
    ('orange', ''),
    ('tangerine', ''),
    ('grapefruit', ''),
    ('banana', ''),
    ('kiwi', ''),
    ('pineapple melon', ''),
    ('watermelon', ''),
    ('tomato', ''),
    ('cucumber', ''),
    ('onion', ''),
    ('garlic', ''),
    ('sweet pepper', ''),
    ('cabbage', ''),
    ('cauliflower', ''),
    ('lettuce', ''),
    ('spinach', ''),
    ('carrots', ''),
    ('beets', ''),
    ('potatoes', ''),
    ('mushrooms', ''),
    ('sweets', ''),
    ('caramels', ''),
    ('chocolate candies', ''),
    ('chocolate', ''),
    ('tea', ''),
    ('coffee', ''),
    ('milk', ''),
    ('cocoa', ''),
    ('hot chocolate', ''),
    ('mineral water', ''),
    ('soft drinks', ''),
    ('Swiss cheese', ''),
    ('Parmesan', ''),
    ('Cheddar', ''),
    ('Mozzarella', ''),
    ('Roquefort', ''),
    ('blue cheese', ''),
    ('beef', ''),
    ('pork', ''),
    ('veal', ''),
    ('lamb', ''),
    ('beefsteak', ''),
    ('roast beef', ''),
    ('ground beef', ''),
    ('hamburgers', ''),
    ('pork chops', ''),
    ('lamb chops', ''),
    ('ham', ''),
    ('bacon', ''),
    ('sausage', ''),
    ('hot dogs', ''),
    ('whole chicken', ''),
    ('chicken leg', ''),
    ('drumstick', ''),
    ('chicken breast', ''),
    ('turkey breast eggs', ''),
    ('dill', ''),
    ('parsley', ''),
    ('mint', ''),
    ('pepper', ''),
    ('salt', ''),
    ('mustard', ''),
    ('garlic', ''),
    ('olive oil', ''),
    ('corn oil', ''),
    ('sunflower seed oil', '');


insert into Customer(Name, Info) values
	('Vladimir Pixix', ''),
    ('Matvey Kulakov', null),
    ('Adolpho Mendoza', ''),
    ('Felice Labone', ''),
    ('Abbott Endecott', ''),
    ('Malva Mackleden', ''),
    ('Mitchael Krelle', ''),
    ('Jennette Coxhead', ''),
    ('Alisander Wemyss', ''),
    ('Tabatha Tasker', ''),
    ('Tam Dobell', ''),
    ('Tracee Phillippo', ''),
    ('Orel Heavy', ''),
    ('Matty Steketee', ''),
    ('Shaine Cockaday', ''),
    ('Guillema Lantry', ''),
    ('Camella Lytlle', ''),
    ('Yuri Lemarie', ''),
    ('Cassandre Burel', ''),
    ('Elisabet Bidewel', ''),
    ('Aretha Scanlan', ''),
    ('Nisse Handforth', ''),
    ('Caye Cuckoo', ''),
    ('Wendye Gallelli', ''),
    ('Anne-corinne Terrey', ''),
    ('Channa Iddins', ''),
    ('Sancho Heffernan', ''),
    ('Cassandra McDonagh', ''),
    ('Hayden Soutter', ''),
    ('Ezri Christou', ''),
    ('Winona Pond-Jones', ''),
    ('Karol Grigsby', ''),
    ('Farica Wheatcroft', ''),
    ('Berry Cottis', ''),
    ('Carmen Razzell', ''),
    ('Issy Kobel', ''),
    ('Bessie Barrand', ''),
    ('Dan Crownshaw', ''),
    ('Mose Dericut', ''),
    ('Alana Piser', ''),
    ('Helge Proud', ''),
    ('Nita Joincey', '');


insert into Employee(ID ,Name, WorkingPoint, Salary) values
(1,'Vova Rubick',11,2606),
(2,'Cristine Walbrun',5,2270),
(3,'Shelby Klisch',6,2592),
(4,'Rriocard Cicutto',4,2522),
(5,'Nikkie Corson',10,2680),
(6,'Tybalt Renac',1,1636),
(7,'Rianon Halton',4,2403),
(8,'Seana Lissett',7,2038),
(9,'Eudora Tudge',6,3033),
(10,'Valentine Hubbuck',1,1948),
(11,'Euell Tabner',9,2894),
(12,'Ximenes Pickrell',3,1432),
(13,'Garrick Side',5,1668),
(14,'Kim Durward',8,2161),
(15,'Derry Becraft',7,1826),
(16,'Stacia Biskupski',6,2595),
(17,'Luca Pedden',6,2551),
(18,'Vinita De la Yglesia',11,2505),
(19,'Latashia Lawie',2,3007),
(20,'Garner Boulton',8,3155);

insert into Receipt(ID,TradePointID,CustomerID,Date,EmployeeID) values
(1,5,9,'2021-04-10',5),
(2,6,10,'2021-11-28',9),
(3,5,40,'2021-08-17',4),
(4,7,5,'2021-12-15',20),
(5,10,13,'2021-02-23',11),
(6,6,39,'2021-04-14',10),
(7,9,39,'2021-11-13',14),
(8,4,33,'2021-03-08',11),
(9,2,9,'2021-11-07',2),
(10,9,12,'2021-04-10',5),
(11,7,42,'2021-01-22',15),
(12,1,17,'2021-10-24',8),
(13,7,19,'2021-03-17',3),
(14,11,30,'2021-03-07',18),
(15,5,5,'2021-02-27',17),
(16,7,36,'2021-10-22',15),
(17,3,4,'2021-08-20',14),
(18,11,6,'2021-04-08',11),
(19,1,40,'2021-01-20',8),
(20,3,33,'2021-12-18',19),
(21,11,19,'2021-02-17',4),
(22,11,30,'2021-01-10',14),
(23,1,39,'2021-02-23',20),
(24,2,8,'2021-08-07',19),
(25,6,34,'2021-11-20',5),
(26,8,20,'2021-07-20',9),
(27,5,31,'2021-01-19',12),
(28,3,29,'2021-09-10',16),
(29,1,27,'2021-07-09',11),
(30,3,15,'2021-04-01',18),
(31,2,20,'2021-07-24',2),
(32,3,39,'2021-10-26',19),
(33,4,3,'2021-02-02',1),
(34,3,10,'2021-06-01',19),
(35,8,11,'2021-04-09',8),
(36,6,18,'2021-07-06',11),
(37,10,15,'2021-08-28',18),
(38,6,36,'2021-03-12',3),
(39,7,17,'2021-04-26',4),
(40,9,24,'2021-04-18',9),
(41,8,17,'2021-07-23',5),
(42,8,28,'2021-10-26',18),
(43,6,37,'2021-03-13',16),
(44,11,9,'2021-01-06',4),
(45,10,1,'2021-06-22',15),
(46,6,35,'2021-07-02',1),
(47,9,3,'2021-06-16',17),
(48,1,2,'2021-09-28',10),
(49,8,28,'2021-04-26',6),
(50,4,23,'2021-04-21',8),
(51,9,13,'2021-02-12',11),
(52,6,30,'2021-11-23',8),
(53,1,5,'2021-03-25',16),
(54,9,18,'2021-05-03',8),
(55,4,9,'2021-05-03',14),
(56,5,5,'2021-08-28',11),
(57,8,12,'2021-12-27',12),
(58,5,24,'2021-07-04',10),
(59,1,1,'2021-02-20',20),
(60,8,27,'2021-12-20',1),
(61,9,4,'2021-01-10',7),
(62,6,37,'2021-11-16',9),
(63,11,22,'2021-11-06',8),
(64,6,4,'2021-10-30',4),
(65,4,31,'2021-09-17',12),
(66,9,40,'2021-12-17',3),
(67,4,25,'2021-07-25',3),
(68,2,17,'2021-05-23',15),
(69,9,8,'2021-08-23',11),
(70,6,21,'2021-03-22',20),
(71,6,27,'2021-11-12',3),
(72,5,37,'2021-09-18',16),
(73,7,28,'2021-07-11',2),
(74,2,13,'2021-12-23',1),
(75,5,36,'2021-12-31',19),
(76,7,15,'2021-10-22',10),
(77,5,32,'2021-10-13',12),
(78,5,2,'2021-12-11',15),
(79,7,12,'2021-07-20',8),
(80,2,18,'2021-08-19',4),
(81,4,12,'2021-05-02',17),
(82,1,29,'2021-04-16',14),
(83,6,13,'2021-08-24',13),
(84,4,35,'2021-06-06',15),
(85,7,39,'2021-09-16',7),
(86,6,16,'2021-05-04',18),
(87,9,26,'2021-03-01',11),
(88,9,28,'2021-03-09',1),
(89,5,41,'2021-11-07',9),
(90,2,30,'2021-10-19',8),
(91,10,33,'2021-07-13',2),
(92,8,5,'2021-04-30',5),
(93,9,6,'2021-12-20',2),
(94,8,13,'2021-07-02',19),
(95,1,16,'2021-12-14',10),
(96,3,5,'2021-07-01',16),
(97,6,2,'2021-02-17',9),
(98,6,22,'2021-10-21',11),
(99,2,40,'2021-02-03',13),
(100,6,41,'2021-02-15',13),
(101,7,36,'2021-01-04',19),
(102,3,10,'2021-12-23',5),
(103,5,8,'2021-03-09',10),
(104,8,3,'2021-06-20',9),
(105,8,28,'2021-04-08',6),
(106,10,39,'2021-11-10',4),
(107,4,31,'2021-11-04',10),
(108,9,11,'2021-05-14',12),
(109,1,23,'2021-07-01',7),
(110,2,15,'2021-09-20',16),
(111,4,39,'2021-05-08',1),
(112,11,13,'2021-09-08',2),
(113,4,33,'2021-06-26',14),
(114,4,24,'2021-01-06',8),
(115,2,26,'2021-01-15',2),
(116,2,17,'2021-07-19',7),
(117,2,1,'2021-08-02',18),
(118,11,18,'2021-05-29',3),
(119,8,39,'2021-12-07',19),
(120,1,34,'2021-02-02',11),
(121,6,4,'2021-02-25',16),
(122,7,20,'2021-12-10',5),
(123,11,34,'2021-11-04',4),
(124,4,14,'2021-07-10',19),
(125,3,10,'2021-08-31',20),
(126,10,38,'2021-01-16',8),
(127,8,31,'2021-05-14',8),
(128,3,31,'2021-06-18',1),
(129,9,15,'2021-08-23',11),
(130,7,28,'2021-05-18',9),
(131,4,26,'2021-12-17',18),
(132,4,12,'2021-09-14',12),
(133,10,14,'2021-06-27',16),
(134,1,34,'2021-11-07',13),
(135,5,41,'2021-12-30',4),
(136,7,26,'2021-10-22',16),
(137,6,28,'2021-10-14',14),
(138,10,5,'2021-06-20',3),
(139,2,30,'2021-02-21',8),
(140,5,11,'2021-09-24',2),
(141,4,10,'2021-11-29',17),
(142,10,4,'2021-06-12',19),
(143,3,33,'2021-01-17',5),
(144,10,26,'2021-05-21',5),
(145,11,39,'2021-09-14',18),
(146,11,41,'2021-02-18',8),
(147,1,5,'2021-08-20',14),
(148,1,35,'2021-12-20',20),
(149,9,38,'2021-07-22',7),
(150,7,23,'2021-12-08',7);


insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (74, 90, 5, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (70, 80, 1, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (6, 53, 3, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (59, 16, 4, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (98, 37, 4, 5);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (31, 1, 2, 37);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (21, 73, 1, 17);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (92, 36, 5, 7);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (8, 8, 5, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (134, 52, 5, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (82, 26, 1, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (67, 63, 1, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (11, 81, 4, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (19, 81, 4, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (111, 62, 1, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (82, 72, 5, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (62, 55, 3, 28);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (134, 84, 3, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (109, 87, 3, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (20, 81, 5, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (50, 30, 3, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (15, 46, 5, 17);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (32, 30, 4, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (28, 48, 2, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (1, 26, 2, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (63, 71, 2, 37);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (34, 57, 4, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (69, 66, 3, 29);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (29, 52, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (64, 33, 1, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (144, 9, 5, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (150, 22, 5, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (31, 25, 1, 28);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (98, 10, 1, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (70, 22, 1, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (92, 84, 3, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (101, 47, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (72, 7, 3, 20);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (81, 35, 2, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (39, 44, 5, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (40, 85, 3, 32);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (34, 11, 3, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (40, 70, 4, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (46, 53, 4, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (61, 42, 2, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (138, 11, 4, 7);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (1, 83, 4, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (111, 42, 5, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (100, 7, 1, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (58, 44, 5, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (149, 77, 3, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (7, 29, 1, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (58, 65, 5, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (138, 84, 1, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (24, 91, 1, 17);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (52, 25, 2, 32);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (144, 79, 5, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (142, 33, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (17, 48, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (104, 25, 4, 11);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (93, 68, 3, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (29, 22, 4, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (103, 87, 4, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (57, 3, 5, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (113, 83, 2, 5);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (7, 20, 2, 15);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (3, 13, 2, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (23, 2, 1, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (5, 54, 1, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (119, 52, 1, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (138, 5, 4, 38);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (120, 3, 3, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (37, 2, 2, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (120, 42, 1, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (69, 76, 5, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (55, 39, 1, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (37, 47, 2, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (119, 63, 2, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (54, 11, 4, 38);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (61, 43, 2, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (137, 44, 5, 15);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (117, 63, 4, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (130, 31, 3, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (148, 60, 1, 32);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (149, 52, 5, 11);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (119, 74, 3, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (146, 34, 1, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (111, 87, 5, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (76, 45, 4, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (87, 21, 1, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (44, 86, 3, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (136, 7, 4, 15);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (132, 68, 1, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (93, 47, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (50, 72, 3, 17);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (74, 66, 5, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (91, 68, 3, 10);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (69, 89, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (111, 25, 3, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (76, 9, 3, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (70, 43, 2, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (60, 30, 4, 7);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (128, 43, 4, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (82, 22, 2, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (34, 39, 3, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (69, 88, 2, 39);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (15, 52, 3, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (36, 8, 3, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (130, 24, 5, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (13, 76, 5, 5);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (15, 1, 1, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (142, 2, 3, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (119, 47, 5, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (98, 31, 3, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (83, 9, 4, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (51, 65, 3, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (57, 53, 1, 28);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (18, 59, 3, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (131, 29, 1, 37);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (89, 2, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (121, 91, 2, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (121, 69, 2, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (42, 27, 3, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (95, 80, 5, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (44, 54, 3, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (123, 40, 4, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (150, 73, 5, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (88, 30, 1, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (54, 73, 4, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (90, 78, 2, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (126, 72, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (148, 7, 1, 11);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (8, 12, 2, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (9, 39, 2, 5);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (80, 3, 5, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (116, 76, 3, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (33, 85, 3, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (135, 66, 4, 11);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (123, 36, 2, 32);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (101, 48, 2, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (19, 36, 3, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (149, 69, 5, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (75, 19, 5, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (135, 36, 4, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (47, 42, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (46, 91, 1, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (46, 83, 1, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (78, 8, 2, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (114, 26, 1, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (51, 8, 2, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (120, 20, 4, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (35, 45, 3, 39);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (61, 52, 3, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (92, 80, 5, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (143, 2, 4, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (125, 85, 4, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (6, 91, 2, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (127, 64, 5, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (68, 50, 5, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (136, 67, 2, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (130, 43, 5, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (103, 14, 4, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (125, 73, 1, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (67, 60, 1, 38);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (133, 81, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (79, 17, 5, 37);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (109, 77, 2, 7);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (102, 50, 1, 38);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (101, 25, 3, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (77, 7, 1, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (50, 55, 4, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (92, 5, 1, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (7, 79, 5, 39);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (116, 34, 3, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (137, 56, 3, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (100, 42, 5, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (90, 14, 2, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (57, 59, 5, 10);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (101, 85, 5, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (22, 3, 4, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (145, 79, 5, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (146, 15, 1, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (110, 13, 2, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (119, 36, 4, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (23, 52, 4, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (140, 48, 4, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (9, 29, 1, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (96, 50, 4, 6);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (15, 23, 5, 17);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (143, 21, 3, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (139, 36, 3, 37);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (5, 25, 3, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (52, 20, 1, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (6, 36, 4, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (24, 36, 4, 7);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (105, 55, 5, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (3, 20, 3, 29);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (19, 89, 3, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (135, 20, 4, 34);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (79, 79, 5, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (121, 43, 2, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (60, 71, 1, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (53, 4, 1, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (49, 27, 5, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (65, 42, 5, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (93, 6, 5, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (21, 28, 5, 26);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (135, 25, 1, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (98, 25, 1, 8);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (85, 63, 3, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (52, 29, 3, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (115, 14, 3, 24);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (145, 58, 2, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (105, 88, 1, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (80, 27, 2, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (46, 42, 2, 19);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (24, 27, 3, 14);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (65, 55, 3, 16);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (134, 74, 1, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (54, 68, 5, 38);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (41, 13, 4, 36);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (28, 40, 3, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (114, 18, 1, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (86, 74, 2, 31);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (100, 72, 1, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (1, 81, 4, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (29, 4, 5, 23);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (130, 66, 4, 9);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (130, 5, 3, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (27, 57, 5, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (81, 90, 3, 25);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (63, 68, 4, 20);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (31, 47, 2, 22);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (32, 63, 1, 27);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (82, 12, 4, 28);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (47, 89, 3, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (140, 34, 1, 18);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (56, 17, 4, 33);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (39, 61, 3, 13);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (137, 90, 4, 35);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (6, 67, 1, 15);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (4, 51, 1, 40);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (102, 45, 3, 10);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (110, 84, 2, 12);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (118, 39, 3, 30);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (73, 9, 5, 21);
insert into ReceiptItem (ReceiptID, ProductID, Amount, Price) values (4, 57, 1, 29);

insert into Section (ID, TradePointID, SectionManagerID, SectionNumber, Floor) values (1, 1, 6, 1, 4);
insert into Section (ID, TradePointID, SectionManagerID, SectionNumber, Floor) values (2, 1, 6, 2, 2);
insert into Section (ID, TradePointID, SectionManagerID, SectionNumber, Floor) values (3, 2, 19, 2, 5);
insert into Section (ID, TradePointID, SectionManagerID, SectionNumber, Floor) values (4, 2, 19, 1, 2);

insert into Hall(ID, HallNumber, TradePointID, EmployeesNumber, Floor) values (1, 1, 4, 3, 5);
insert into Hall(ID, HallNumber, TradePointID, EmployeesNumber, Floor) values (2, 1, 1, 2, 5);
insert into Hall(ID, HallNumber, TradePointID, EmployeesNumber, Floor) values (3, 1, 3, 3, 5);
insert into Hall(ID, HallNumber, TradePointID, EmployeesNumber, Floor) values (4, 2, 4, 1, 3);

insert into Request (ID, TradePointID, Date) values (1, 2, '2021-09-19');
insert into Request (ID, TradePointID, Date) values (2, 7, '2021-11-22');
insert into Request (ID, TradePointID, Date) values (3, 10, '2021-03-03');
insert into Request (ID, TradePointID, Date) values (4, 7, '2021-05-24');
insert into Request (ID, TradePointID, Date) values (5, 3, '2021-09-22');
insert into Request (ID, TradePointID, Date) values (6, 5, '2021-03-05');
insert into Request (ID, TradePointID, Date) values (7, 11, '2021-08-09');
insert into Request (ID, TradePointID, Date) values (8, 7, '2021-10-18');
insert into Request (ID, TradePointID, Date) values (9, 2, '2021-03-02');
insert into Request (ID, TradePointID, Date) values (10, 3, '2021-09-29');
insert into Request (ID, TradePointID, Date) values (11, 4, '2021-02-26');
insert into Request (ID, TradePointID, Date) values (12, 11, '2021-08-17');
insert into Request (ID, TradePointID, Date) values (13, 9, '2021-05-20');
insert into Request (ID, TradePointID, Date) values (14, 4, '2021-08-10');
insert into Request (ID, TradePointID, Date) values (15, 3, '2021-08-11');
insert into Request (ID, TradePointID, Date) values (16, 1, '2021-10-28');
insert into Request (ID, TradePointID, Date) values (17, 9, '2021-01-29');
insert into Request (ID, TradePointID, Date) values (18, 5, '2021-12-15');
insert into Request (ID, TradePointID, Date) values (19, 5, '2021-09-10');
insert into Request (ID, TradePointID, Date) values (20, 9, '2021-10-28');
insert into Request (ID, TradePointID, Date) values (21, 5, '2021-12-22');
insert into Request (ID, TradePointID, Date) values (22, 8, '2021-03-27');
insert into Request (ID, TradePointID, Date) values (23, 11, '2021-03-31');
insert into Request (ID, TradePointID, Date) values (24, 7, '2021-08-21');
insert into Request (ID, TradePointID, Date) values (25, 7, '2021-11-05');
insert into Request (ID, TradePointID, Date) values (26, 7, '2021-09-08');
insert into Request (ID, TradePointID, Date) values (27, 2, '2021-10-08');
insert into Request (ID, TradePointID, Date) values (28, 4, '2021-06-27');
insert into Request (ID, TradePointID, Date) values (29, 8, '2021-01-29');
insert into Request (ID, TradePointID, Date) values (30, 2, '2021-11-04');
insert into Request (ID, TradePointID, Date) values (31, 9, '2021-12-28');
insert into Request (ID, TradePointID, Date) values (32, 2, '2021-07-20');
insert into Request (ID, TradePointID, Date) values (33, 10, '2021-09-23');
insert into Request (ID, TradePointID, Date) values (34, 6, '2021-01-05');
insert into Request (ID, TradePointID, Date) values (35, 5, '2021-12-13');
insert into Request (ID, TradePointID, Date) values (36, 8, '2021-01-30');
insert into Request (ID, TradePointID, Date) values (37, 10, '2021-02-08');
insert into Request (ID, TradePointID, Date) values (38, 5, '2021-09-19');
insert into Request (ID, TradePointID, Date) values (39, 3, '2021-07-17');
insert into Request (ID, TradePointID, Date) values (40, 10, '2021-03-24');

insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (70, 5, 1, 28);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (61, 6, 4, 85);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (76, 6, 3, 97);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (66, 11, 9, 88);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (6, 1, 1, 87);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (44, 7, 5, 67);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (35, 4, 5, 73);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (9, 5, 5, 23);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (45, 2, 4, 47);
insert into Distribution (ProductID, TradePointID, OrderID, Amount) values (25, 9, 2, 73);

insert into ProductsOrder (ID, Date) values (1, '2021-10-21');
insert into ProductsOrder (ID, Date) values (2, '2021-09-20');
insert into ProductsOrder (ID, Date) values (3, '2021-09-23');
insert into ProductsOrder (ID, Date) values (4, '2021-05-18');
insert into ProductsOrder (ID, Date) values (5, '2021-03-07');
insert into ProductsOrder (ID, Date) values (6, '2021-03-09');
insert into ProductsOrder (ID, Date) values (7, '2021-03-12');
insert into ProductsOrder (ID, Date) values (8, '2021-02-22');
insert into ProductsOrder (ID, Date) values (9, '2021-08-23');
insert into ProductsOrder (ID, Date) values (10, '2021-12-12');

insert into RequestOrder (RequestID, OrderID) values (2, 1);
insert into RequestOrder (RequestID, OrderID) values (17, 1);
insert into RequestOrder (RequestID, OrderID) values (36, 6);
insert into RequestOrder (RequestID, OrderID) values (21, 6);
insert into RequestOrder (RequestID, OrderID) values (38, 9);
insert into RequestOrder (RequestID, OrderID) values (23, 3);
insert into RequestOrder (RequestID, OrderID) values (9, 8);
insert into RequestOrder (RequestID, OrderID) values (28, 3);
insert into RequestOrder (RequestID, OrderID) values (38, 1);
insert into RequestOrder (RequestID, OrderID) values (19, 5);

insert into RequestItem (ProductID, RequestID, Amount) values (10, 16, 200);
insert into RequestItem (ProductID, RequestID, Amount) values (71, 3, 166);
insert into RequestItem (ProductID, RequestID, Amount) values (32, 18, 80);
insert into RequestItem (ProductID, RequestID, Amount) values (40, 8, 36);
insert into RequestItem (ProductID, RequestID, Amount) values (65, 16, 85);
insert into RequestItem (ProductID, RequestID, Amount) values (68, 9, 183);
insert into RequestItem (ProductID, RequestID, Amount) values (8, 8, 21);
insert into RequestItem (ProductID, RequestID, Amount) values (26, 9, 96);
insert into RequestItem (ProductID, RequestID, Amount) values (69, 25, 95);
insert into RequestItem (ProductID, RequestID, Amount) values (74, 25, 88);

insert into Distributor (ID, Contact, Rating) values (1, null, 31);
insert into Distributor (ID, Contact, Rating) values (2, null, 34);
insert into Distributor (ID, Contact, Rating) values (3, null, 70);
insert into Distributor (ID, Contact, Rating) values (4, null, 82);
insert into Distributor (ID, Contact, Rating) values (5, null, 93);
insert into Distributor (ID, Contact, Rating) values (6, null, 4);
insert into Distributor (ID, Contact, Rating) values (7, null, 6);
insert into Distributor (ID, Contact, Rating) values (8, null, 97);
insert into Distributor (ID, Contact, Rating) values (9, null, 1);
insert into Distributor (ID, Contact, Rating) values (10, null, 94);

insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (1, 3, 77, 73, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (2, 6, 49, 58, false);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (3, 9, 55, 97, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (4, 3, 25, 77, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (5, 6, 30, 11, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (6, 3, 83, 27, false);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (7, 6, 84, 34, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (8, 10, 10, 34, true);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (9, 9, 15, 41, false);
insert into DistributorProduct (ID, DistributorID, ProductID, Price, OfferIsActiveNow) values (10, 8, 44, 86, false);

