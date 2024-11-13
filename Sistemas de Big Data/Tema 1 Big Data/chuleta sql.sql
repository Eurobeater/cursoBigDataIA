show databases;

use granciudad

show tables;

desc city;

truncate granciudad;

INSERT INTO granciudad SET id= 0, nombre = 'Cartagena', origen = 'Carthago', fecha = '600-12-31';

INSERT INTO granciudad SET id= 0, nombre = 'Mérida', origen = 'Caesar Augusta',
fecha = '200-12-31';

DELETE FROM granciudad WHERE id = 4;

DELETE FROM granciudad ORDER BY nombre ASC LIMIT 2;

DELETE FROM granciudad WHERE fecha > '1000-01-01';

SELECT INTO actor SET actor_id = 0, first_name = 'ALFREDO', last_name = 'LANDA', last_update = 0;

SELECT * FROM actor WHERE last_name = 'JOHANSSON';

SELECT * FROM actor WHERE last_name LIKE '__O%';

SELECT * FROM actor WHERE last_name LIKE '%JOH%';

SELECT * FROM actor WHERE first_name LIKE 'J%' AND last_name LIKE '%a%';

SELECT COUNT(*) FROM actor WHERE first_name LIKE 'J%' AND last_name LIKE '%a%';

SELECT * from city WHERE city LIKE '% %';

SELECT * from city WHERE country_id = 61;

SELECT city FROM city WHERE country_id = (SELECT country_id FROM country WHERE country = 'Spain');

SELECT title FROM film WHERE length >= 80 AND length <= 120;

SELECT title FROM film WHERE length(title) >= 12 ;

SELECT title FROM film WHERE title LIKE '____________%';

SELECT title FROM film WHERE rating != 'NC-17';

SELECT title FROM film WHERE length = (SELECT MAX(length) FROM film);

SELECT title, first_name, last_name FROM film LEFT JOIN film_actor ON film.film_id = film_actor.film_id LEFT JOIN actor ON film_actor.actor_id = actor.actor_id;