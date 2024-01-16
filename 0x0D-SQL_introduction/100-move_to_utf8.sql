-- converts the database to utf-8
-- specify database
USE hbtn_0c_0
-- the DDL
ALTER TABLE `first_table`
CONVERT TO CHARACTAR SET utf8mb4 COLLATE utf8mb4_unicode_ci;
