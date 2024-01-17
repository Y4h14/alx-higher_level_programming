-- lists all cities of california
SELECT id, name 
FROM cities
WHERE id IN
	(SELECT id 
		FROM states
		WHERE name = "California")
ORDER BY id;
