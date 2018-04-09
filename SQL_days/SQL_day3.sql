use sakila;

describe city;
describe address;

select *
from city
limit 10
;


select c.city_id, c.city, a.district
from city c
inner join address a 
	on c.city_id = a.city_id
where city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
;

select district
from address 
where city_id in (
	select city_id
    from city
    where city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
    )
;

select *
from customer
limit 10;

# film 
SELECT COUNT(*) as 'Number of Copies', title 
   FROM inventory join film WHERE film.film_id = inventory.film_id
   Group BY title;
   
   
# foreign keys
CREATE TABLE customer_email (
 id INTEGER(11) AUTO_INCREMENT NOT NULL,
 location VARCHAR(30) NOT NULL,
 animal_id INTEGER(10) NOT NULL,
 PRIMARY KEY (id),
 FOREIGN KEY (animal_id) REFERENCES customer(customer_id) 
);
   

# unions 
select count(*)
from city
union
select count(*)
from country;

select *
from customer
union
select * 
from customer_list;

select ID
from customer_list
where city like 'London';

# self joins
CREATE TABLE emps(
 employee_id int(8) NOT NULL,
 first_name varchar(125) NOT NULL,
 last_name varchar(125) NOT NULL,
 supervisor_id int(8),
 PRIMARY KEY(employee_id)
);

INSERT INTO emps VALUES (25, 'Sandy', 'Waxman', 100);
INSERT INTO emps VALUES (26, 'Yukio', 'Mishima', 100);
INSERT INTO emps VALUES (27, 'Serge', 'Gainsbourg', 100);
INSERT INTO emps VALUES (100, 'Sidney', 'Meiru', 100);

select *
from emps;

select A.employee_id, A.first_name, A.last_name, A.supervisor_id, B.first_name as supervisor_first_name, B.last_name as supervisor_last_name
from emps as A
join emps as B
	on A.supervisor_id = B.employee_id;






