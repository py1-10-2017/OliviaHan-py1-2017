SELECT customer.first_name, customer.last_name, customer.email, city.city, address.address, address.postal_code
FROM customer
JOIN address
ON customer.address_id = address.address_id 
JOIN city
ON city.city_id = address.city_id
WHERE city.city_id = 312;

SELECT film.title, film.description,film.release_year, film.rating, film.special_features, category.name as genre
FROM film
JOIN film_category 
on film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';

SELECT actor.first_name, actor.last_name,actor.actor_id, film.title, film.description, film.release_year
FROM actor 
JOIN film_actor
ON actor.actor_id = film_actor.actor_id
JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, city.city, address.address, address.postal_code, store.store_id,city.city_id
FROM customer
JOIN address
ON customer.address_id = address.address_id 
JOIN city
ON city.city_id = address.city_id
JOIN store
ON store.store_id = customer.store_id
WHERE city.city_id in (1, 42, 312, 459) and store.store_id = 1;


