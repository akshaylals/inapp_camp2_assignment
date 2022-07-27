CREATE DATABASE railway_db;
GO

USE railway_db;
GO

CREATE TABLE stops(
	id INT PRIMARY KEY NOT NULL,
	stop CHAR(3) NOT NULL
);
GO

CREATE TABLE trains(
	id INT IDENTITY PRIMARY KEY NOT NULL,
	code CHAR(7) NOT NULL,
	dest INT NOT NULL FOREIGN KEY REFERENCES stops(id),
	berth INT NOT NULL,
	waitlist INT NOT NULL
);
GO

CREATE TABLE passengers(
	id INT IDENTITY PRIMARY KEY NOT NULL,
	name VARCHAR(20) NOT NULL,
	age INT NOT NULL,
	dest INT NOT NULL FOREIGN KEY REFERENCES stops(id),
	train INT NOT NULL FOREIGN KEY REFERENCES trains(id),
);
GO


INSERT INTO stops VALUES
	(0, 'TVM'),
	(1, 'ALP'),
	(2, 'ERN'),
	(3, 'KZK');
GO

INSERT INTO trains VALUES
	('TVM_ALP', 1, 5, 0),
	('TVM_ERN', 2, 5, 0),
	('TVM_KZK', 3, 5, 0);
GO


SELECT * FROM trains;
SELECT * FROM stops;