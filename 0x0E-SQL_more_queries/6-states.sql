-- creates the database hbtn_0d_usa and the table states
-- creating the table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- creating the states table
CREATE TABLE IF NOT EXISTS `states`(
	id INT PRIMARY KEY UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL);
