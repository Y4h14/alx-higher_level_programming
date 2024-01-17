--  creates the database hbtn_0d_usa and the table cities
-- create the database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- creating the table
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
	PRIMARY KEY(id),
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)	
);
