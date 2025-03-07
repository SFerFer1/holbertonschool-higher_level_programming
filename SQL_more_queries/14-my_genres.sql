-- asas
USE hbtn_0d_tvshows;

SELECT g.name AS tv_genres
FROM genres g
JOIN tv_shows_genres tg ON g.id = tg.genre_id
JOIN tv_shows s ON tg.tv_show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
