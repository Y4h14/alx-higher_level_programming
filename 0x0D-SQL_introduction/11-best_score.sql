-- lists all records with a score >= 10 in second_table
-- specify the database
USE hbtn_0c_0
-- the query
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
