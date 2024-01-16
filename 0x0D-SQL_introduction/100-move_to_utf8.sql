-- converts the database to utf-8
-- specify the database
USE hbtn_0c_0;
-- converting to utf8
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
