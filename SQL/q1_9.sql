USE sakila;
SELECT SUM(C)
FROM (SELECT COUNT(*) AS C
FROM (SELECT DISTINCT first_name,last_name FROM actor) AS B
GROUP BY first_name
HAVING C>1) AS A;