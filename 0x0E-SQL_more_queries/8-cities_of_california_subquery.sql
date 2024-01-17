-- lists all cities of california
SELECT * 
FROM states, cities
WHERE states.id = cities.states_id
AND states.name = 'California'
ORDER BY states.id;
