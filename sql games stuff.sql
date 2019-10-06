--DELETE DATABASE games_db

--DROP TABLE [Game Listings]

--CREATE TABLE [Game Listings]
--(
--[Listing ID] int NOT NULL,
--Game VARCHAR (50),
--Console VARCHAR (10),
--Phone CHAR (11),
--Price DECIMAL (5,2),
--Location VARCHAR (10),
--Latitude DECIMAL (8,5),
--Longitude DECIMAL (8,5)
--)

--INSERT INTO [Game Listings] ([Listing ID], Game, Console, Phone, Price) 
--VALUES 
--(1, 'The Simpsons: Hit & Run', 'PS2', '07123456789', '10.00'),
--(2, 'Crash Team Racing', 'PS1', '07987654321', '4.99'),
--(3, 'Sheep, Dog n Wolf', 'PS1', '07987123456', '4.99'),
--(4, 'Need for Speed: Underground', 'PS2', '07123987654', '8.99'),
--(5, 'Batman: Arkham Asylum', 'XBOX 360', '07321987456', '10.99')

SELECT * FROM [Game Listings]