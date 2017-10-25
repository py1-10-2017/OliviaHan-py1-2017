
select countries.name, languages.language, languages.percentage 
from countries 
join languages 
on countries.id = languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;

select countries.name, count(cities.id) as city_number
from countries
join cities 
on countries.id = cities.country_id 
group by countries.id 
order by city_number desc;

select countries.name as country, cities.name as city, cities.population
from cities 
join countries
on countries.id = cities.country_id
where countries.id = 136
having cities. population > 500000
order by cities.population desc;

select distinct countries.name as country, languages.language, languages.percentage
from countries
join languages
on countries.id = languages.country_id 
join cities 
on countries.id = cities.country_id
having percentage > 89
order by languages.percentage desc;

select name,surface_area,population from countries 
where surface_area < 501 and population >100000;

select name, government_form,capital,life_expectancy from countries
where government_form = 'Constitutional Monarchy'
having capital > 200 and life_expectancy > 75;

select countries.name as country, cities.name as city, cities.district, cities.population
from countries
join cities 
on countries.id = cities.country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires'
having population > 500000;

select count(countries.id) as country_number, region
from countries 
group by countries.region
order by country_number desc;












