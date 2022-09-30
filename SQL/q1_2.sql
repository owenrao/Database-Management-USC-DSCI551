USE sakila;
SELECT first_name,last_name
FROM actor
WHERE SUBSTRING(last_name,-2,1)='i';