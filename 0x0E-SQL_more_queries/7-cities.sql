--  creates the database hbtn_0d_usa and the table cities
-- create the database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- creating the table
CREATE TABLE IF NOT EXISTS `cities`(
	id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFRENCES states(id)
	);
