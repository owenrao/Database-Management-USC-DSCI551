USE sakila;
SELECT COUNT(*)
FROM film
WHERE rating='PG-13' AND length>=100 AND length<=200;