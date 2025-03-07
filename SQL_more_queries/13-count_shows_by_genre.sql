-- aqaa
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
JOIN tv_shows_genres tg ON g.id = tg.genre_id
JOIN tv_shows s ON tg.tv_show_id = s.id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
