USE sakila;
SELECT title,length
FROM film
WHERE film.length=(SELECT MAX(length) FROM film);