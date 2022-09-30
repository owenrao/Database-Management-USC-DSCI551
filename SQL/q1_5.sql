USE sakila;
SELECT customer_id
FROM rental
GROUP BY customer_id
HAVING COUNT(*)>=40;