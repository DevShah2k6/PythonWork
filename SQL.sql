create database if not exists startersql2;

use startersql2;

create table users(
id int auto_increment primary key,
name varchar(100) not null,
email varchar(100) unique not null,
gender enum('Male','female','other'),
date_of_birth date,
salary decimal(10,2),
created_at timestamp default current_timestamp);


-- Insert sample data into users table

INSERT INTO users (name, email, gender, date_of_birth, salary)
VALUES
('John Doe', 'john@example.com', 'Male', '1995-06-15', 50000.00),
('Alice Smith', 'alice@example.com', 'female', '1998-02-20', 62000.50),
('Michael Johnson', 'michael@example.com', 'Male', '1992-11-10', 75000.00),
('Sophia Brown', 'sophia@example.com', 'female', '2000-08-05', 45000.75),
('Chris Lee', 'chris@example.com', 'other', '1997-04-12', 58000.00),
('xyz', 'xyz@example.com', 'male', '2005-01-12', 23450.00);
-- here below record can not bve iserted due to unique constraint
-- ('abc','xyz@exmaple.com','male','2007-01-12',22500.00);
-- here name is not null as done in table
-- (NULL,'xyz@exmaple.com','male','2007-01-12',22500.00); 
select * from users;


-- where clause
select name,gender from users where gender='male';


select email,gender from users where gender !='male';

select email,gender from users where date_of_birth<'1999-08-15';


select email,gender from users where id<=2;

-- checking null value are there or not 
select * from users where date_of_birth is null;

-- between

select name from users where date_of_birth between '1970-01-01' and '2000-12-31';


select * from users where gender in ('Male','female');

-- and condition
select * from users where gender ='male' and salary>30000;

select * from users where gender='female' or salary<20000;


-- order by ascending 
select * from users where gender='male' or salary>=15000 order by date_of_birth;

-- order by descending

select * from users where gender='male' or salary>=15000 order by date_of_birth desc;


select * from users;

-- updating data in table 
update users set salary = 45000,email='johnshah@gmail.com' where id=1;

select * from users;


update users set salary = salary+salary*0.20 where id =3;
select * from users;

SET SQL_SAFE_UPDATES = 0;
-- deleteing the data in table 
delete from users where salary<10000;

-- delete from users where id=3;
-- by drop table suers users table will be removed  
-- drop table users;


-- unique constrraint means all unique values are ther no same values are there
select * from users;
/*to see in chatgpt below one */
--  here email is been unique_email  to make filed unique
alter table users add constraint unique_email unique(email);


-- check constarint is used it is checking like condition as now i can not inserted values before 1990 
alter table users add constraint check_dob check (date_of_birth>'1990-01-01');

-- default constrint menas the default value will be there

-- aggreate fucntion
select count(*) from users;


select count(*) from users where gender ='male';
select * from users;
select min(salary) as min_salary,max(salary) as max_salary from users;

select sum(salary) as total from users;

select gender,AVG(SALARY) AS AVG_SALARY FROM USERS group by gender;

select name,length(name) as len_name from users;

select lower(name) as lower from users;

select *,concat(lower(name),"5677") as username,now() as time,month(date_of_birth) as month from users;

-- datediffrernce 
select name,datediff(curdate(),date_of_birth) as days from users;

set autocommit=0;
--   autocommit if off then data can be retrived also if delete by above command
-- here by rollback it goes to the last chnage or commit command  
rollback;
select * from users;

drop table if exists addresses;

create table addresses(
id int auto_increment primary key,
user_id int,
street varchar(255),
city varchar(100),
state varchar(100),
pincode varchar(10),
-- here below is benn done for the relation between two table 
-- on delete cascade means if some one delte the record in users table it will automatically dlete from this table 
-- fk_user is constraint name of foreign key 
constraint fk_user foreign key(user_id) references users(id)  on delete cascade
);
SELECT id, name FROM users;
INSERT INTO addresses (user_id, street, city, state, pincode)
VALUES
(1, '12 MG Road', 'Bangalore', 'Karnataka', '560001'),
(2, '45 Park Street', 'Kolkata', 'West Bengal', '700016'),
(4, '22 Anna Salai', 'Chennai', 'Tamil Nadu', '600002'),
(5, '10 Ring Road', 'Delhi', 'Delhi', '110001');

select * from addresses;

select * from users;

delete from users where id=5;

select * from addresses;

-- left join 
select * from users left join addresses on users.id = addresses.user_id;


select * from admin_users;

select * from users;

-- union :- to concantenate column wise
-- UNION: used to concatenate rows from two or more SELECT queries
-- also in union duplicate record will not be seen
select name from users
union
select name from admin_users;

select name,'user' as role from users
union
select name,'admin' as role from admin_users;

select name,'user' as role,date_of_birth from users
union
select name,'admin' as role,date_of_birth from admin_users
order by date_of_birth;

-- union all
-- in this duplicates are allowed
select name from users
union all
select name from admin_users;



alter table users add column referred_by_id int;

update users set referred_by_id = 1 where id in (2,3);
update users set referred_by_id = 2 where id=4 ;

select * from users;

-- self join is been done
select a.id,a.name as user_name,
b.name as referred_by_name 
from users a 
left join users b on a.referred_by_id  = b.id;

select * from users;
-- creating a view like virtual table 

create view users_list as select * from users where salary<50000;
--  to delete the view
drop view users_list;

select * from users_list;

update users set salary = salary+4700 where id=1;

-- view is like snapshot based on result of select query 
-- it is used when to write long select query
select * from users_list;

drop view users_list;


-- index help to spped the data retriveal
-- below command is to show indexes
show indexes from users;

-- id and email have indexes 

-- idx_email is index name made on gender
create index idx_email on users (gender);

-- index consumes extra space and slow down crud operation as index have to update

-- multi column index
create index idx_gender_salary on users(gender,salary);


select * from users where gender='female' and salary>10000;



select * from users where salary>50000;
-- dropping the indexes
-- drop index index name on table name
drop index idx_gender_salary on users;


-- subqueries
select avg(salary) from users;

-- inner query return the value and then comparsion is done
-- this is a scalar query in which one value is returning
select id,name,salary from users where salary > (select avg(salary) from users);

select id,name,salary from users where salary < (select avg(salary) from users);

-- users which are referreb which are earning grtaer than avg salary
select id,name,referred_by_id from users where  referred_by_id in (select id from users where salary>(select avg(salary) from users));


select name,salary,(select avg(salary) from users) as avg_salary from users;


-- group by and having

-- grouping by gender and showing the average salary
select gender,avg(salary) as 'Average_Salary' from users group by gender;

select gender,avg(salary) as 'Average_Salary',count(*) as count from users group by gender;

-- having is used after grouping
-- filtering is done wioth having
select gender,avg(salary) as 'Average_Salary',count(*) as count from users group by gender having avg(salary)<70000 and count(*)<20;


select referred_by_id,count(*) as total_referred from users where referred_by_id is not null group by referred_by_id having count(*)>0;

-- rollup is used for finding grand total or subtotals to find it
-- it gives weighted average 
-- 1*salary+ 2*salary/3 then weighted average will be found
select gender,avg(salary) as 'Average_Salary',count(*) as count from users group by gender with rollup having avg(salary)<60000;



-- stored proceudre (like fucntion)

-- without chnaging delimiter

delimiter $$
/*create procedure select_users()
begin
-- here ; is not delimiter
	select * from users;
end $$
-- delimiter is now semicolon ;
delimiter ;
-- (call procedure name) syntax
call select_users()

*/
delimiter $$
-- create procedure AddUser(
-- 	in p_name varchar(100),
-- 	in p_email varchar(100),
-- 	in p_gender enum('Male','female','other'),
-- 	in p_dob date,
-- 	in p_salary int
-- )
-- begin
-- 	insert into users (name,email,gender,date_of_birth,salary) values (p_name,p_email,p_gender,p_dob,p_salary);
--     select * from users;
--  end $$
 
 -- call AddUser('John','john@harry.com','other','1990-07-12',74000)
 -- call AddUser('alice','alice@harry.com','male','1995-07-12',56000)
 
 -- to show that how many procedure are ther in that database
 show procedure status where db='startersql2';
 
 
 drop procedure if exists AddUser;
 
 
 -- triggers:-invoke particluar action menas chnages are reflected 
 -- trigeers arw automatially exceuted 
 use startersql2;


create table users (
    id int auto_increment primary key,
    name varchar(100),
    email varchar(100),
    gender varchar(10),
    date_of_birth date,
    salary int
);

create table user_log(
    id int auto_increment primary key,
    user_id int,
    name varchar(100),
    created_on timestamp default current_timestamp
);
delimiter $$

create trigger after_user_insert
after insert on users
for each row
begin
    insert into user_log(user_id, name)
    values (NEW.id, NEW.name);
end $$

delimiter ;

insert into users (name, email, gender, date_of_birth, salary)
values ('rohan','rohan@rohan.com','male','2007-04-04',56000);
insert into users (name, email, gender, date_of_birth, salary)
values ('priya', 'priya@gmail.com', 'female', '2005-09-12', 62000);
select * from user_log;
use startersql;


select * from users where name like '_a%';

select * from users where name like '_a_h%';

-- limit offset
select * from users order by id limit 1 offset 2;

-- distict
select distinct gender from users;

-- truncate

truncate table addresses;

select * from addresses;

-- delete removes the record one by one 
