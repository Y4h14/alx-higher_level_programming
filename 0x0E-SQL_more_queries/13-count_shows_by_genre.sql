-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.id_genre AS genre, COUNT(*) AS number_of_shows
FROM tv_gneres AS g
	INNER JOIN tv_show_genres AS x
	ON g.id = x.genre_id
	GROUP BY g.name
ORDER BY number_of_shows DESC;
