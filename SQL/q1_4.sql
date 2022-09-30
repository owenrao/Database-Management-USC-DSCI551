USE sakila;
SELECT category.name, COUNT(*)
FROM category JOIN film_category ON category.category_id=film_category.category_id
GROUP BY category.category_id;