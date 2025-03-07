--asd
USE hbtn_0d_tvshows;

SELECT s.title
FROM tv_shows s
JOIN tv_shows_genres tg ON s.id = tg.tv_show_id
JOIN genres g ON tg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
