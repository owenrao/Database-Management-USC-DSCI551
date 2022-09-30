USE sakila;
SELECT customer.first_name, customer.last_name
FROM customer JOIN payment ON customer.customer_id=payment.customer_id
GROUP BY customer.customer_id
HAVING SUM(payment.amount)>200;