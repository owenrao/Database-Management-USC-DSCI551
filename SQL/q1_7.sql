USE sakila;
SELECT actor.first_name,actor.last_name
FROM actor
WHERE actor.actor_id NOT IN (SELECT actor_id FROM film_actor WHERE film_id IN (SELECT film_id FROM film WHERE rating='R'));
