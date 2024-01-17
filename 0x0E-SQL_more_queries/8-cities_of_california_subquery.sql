-- lists all cities of california
SELECT * 
FROM states, cities
WHERE states.id IN
	(SELECT id 
		FROM states
		WHERE name = 'California')
ORDER BY states.id;
