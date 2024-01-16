-- lists the number of records with the same score
-- specify databae 
USE hbtn_0c_0
-- query
SELECT score, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`;

