-- asa
USE hbtn_0d_tvshows;

SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_shows_genres tg ON s.id = tg.tv_show_id
LEFT JOIN genres g ON tg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
