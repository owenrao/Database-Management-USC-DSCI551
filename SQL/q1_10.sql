USE sakila;
SELECT C_A.first_name,C_A.last_name,A_CT.city
FROM
(SELECT first_name,last_name, address_id
FROM customer
WHERE first_name='Jessie' OR first_name='Jamie' OR first_name='Leslie') AS C_A
INNER JOIN
(SELECT address.address_id,city.city
FROM address JOIN city ON address.city_id=city.city_id) AS A_CT
ON C_A.address_id=A_CT.address_id
ORDER BY C_A.first_name DESC;

