-- kkkkkdd

USE hbtn_0d_usa

SELECT cities.id, cities.state_id, cities.name  FROM cities
WHERE state_id = (SELECT state_id FROM states WHERE NAME = California)
ORDER BY cities.id ASC;