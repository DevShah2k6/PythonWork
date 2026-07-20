-- creating database
create database if not exists school;
use school;
-- creating table
create table Student(
id int auto_increment primary key,
student_name varchar(100) not null,
class_id int not null,
age int,
course_name varchar(100),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
city varchar(100)
);

-- dropping the whole table
drop table Student;
-- inserting data into student
insert into Student values(1,'xyz',14,1,'SQL');

-- seeing the whole data  using select statement
select * from Student;

insert into Student(id,student_name,age,class_id,course_name,created_at,city) values
(1,'xyz',14,1,'SQL',now(),'jaipur'),
(2,'abc',15,2,'Java',now(),'ahmedabad'),
(3,'pqr',17,1,'Python',now(),'lucknow'),
(4,'qwe',18,3,'ML',now(),'ahmedabad'),
(5,'asd',20,2,'AI',now(),'mumbai'),
(6,'opq',21,4,'AI',now(),'bengaluru');



-- seeing the specific column
select student_name,course_name from Student;

-- adding column named city in stduent table
alter table Student add column city varchar(100);

-- Disable MySQL safe update mode temporarily
-- This allows UPDATE or DELETE queries without using a KEY column in WHERE clause

SET SQL_SAFE_UPDATES = 0;
-- deleteing the record in which city is jaipur
delete from Student where city='jaipur';

insert into Student values(7,'zaw',23,5,'MERN Stack',now(),'baroda');

select * from Student;

-- renaming Student->Student_Details
rename table Student to Student_Details;

rename table Student_Details to Student;

insert into Student values(8,'ert',4,6,'Mean Stack',now(),'ranchi');

select * from Student;

insert into Student values(9,'bnm',4,6,null,now(),'jaipur');


-- where clause
select * from Student where age>17;

select * from Student where student_name='opq';


select * from Student where student_name is null;

select * from Student where course_name is null;

-- between
select * from Student where age between 18 and 24;

-- updating the table
update Student set course_name = 'AI-ML' where student_name='zaw';


select * from Student;

update Student set course_name='MERN Stack' where course_name is null;

-- ascending order
select * from Student order by age;

-- descending order
select * from Student order by age desc;

select * from Student where student_name='zaw' and course_name='AI-ML';


select * from Student where age is null and course_name='mean stack';

select * from Student where age>20 or course_name='AI';

-- not equal operator
select * from Student where course_name !='AI';

-- aggreate fucntion
select min(age) as min_age from Student;

select max(age) as max_age from Student;

select count(*) as total_students from Student;

-- string fucntion
select upper(student_name) as capital from Student;

select concat(upper(student_name),"5677") as username from Student;


drop table if exists Class;
CREATE TABLE Class (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(20),
    teacher_name VARCHAR(50),
    subject_marks int not null,
    room_id int,
    foreign key(room_id) references Room(room_id)
);
CREATE TABLE Room (
    room_id INT PRIMARY KEY,
    room_number VARCHAR(10)
);
drop table Class;
INSERT INTO Class VALUES
(1, '10A', 'Mr. Sharma',45,101),
(2, '10B', 'Mrs. Patel',67,102),
(3, '9A', 'Mr. Mehta',34,102),
(4,'8A','MR. Shah',78,null);
INSERT INTO Room VALUES (101, 'A101');
INSERT INTO Room VALUES (102, 'B202');
select * from Class;
select * from Student;
select * from Room;
-- inner join
select * from Student s join Class c on s.class_id = c.class_id;

select * from Class c join Room r on c.room_id = r.room_id;

-- left join
select * from Student s left join Class c on s.class_id = c.class_id where student_name='opq';

select * from Class c left join Room r on c.room_id = r.room_id;


-- right join
select * from Student s right join Class c on s.class_id = c.class_id where student_name='asd';

select * from Class c right join Room r on c.room_id = r.room_id;

-- union (remove duplicates)
select * from Student
union
select * from Student;

-- union all(include duplicate)
select * from Class
union all
select * from Class;

alter table Student add column sid int;


update Student set sid = 1 where id in (7,8);
update Student set sid=2 where student_name = 'asd';
update Student set sid=3 where city = 'Ahmedabad';
select * from Student;

-- self join

select * from Student s1  join Student s2 on s1.sid = s2.id;

-- view (virtual table)
create view age_18 as select * from Student where age>18;

select * from age_18;
update age_18 set course_name='Android' where id=5;
-- dropping view
drop view age_18;


create index idx_student_name on Student(student_name);

show indexes from Student;

create index idx_teacher_name on Class(teacher_name);

show indexes from Class;
drop index idx_student_name on Student;
drop index idx_teacher_name on Class;
-- logical operator
select * from Student where student_name='asd' and course_name='mearn stack';

select * from Student where student_name='abc' or course_name='AI';

-- aggreate fucntion

select avg(subject_marks) from Class;

select min(subject_marks) as min_marks from Class;
select max(subject_marks) as max_marks from Class;

-- subquery
select * from Student s join Class c on s.class_id = c.class_id where subject_marks>(select avg(subject_marks) from Class);
select * from Student s join Class c on s.class_id = c.class_id where sid in (select id from Student where subject_marks>(select avg(subject_marks) from Class));
-- group by
select course_name from Student group by course_name;
select class_id from Student group by class_id;

select class_id,count(*) from Student group by class_id having count(*)>1;

-- rollup
select room_id,avg(subject_marks) from Class c group by room_id with rollup having avg(subject_marks)>30;


--  stored procedures
-- changing delimiter 
delimiter $$

-- creating procedure
-- create procedure show_data()
-- begin
-- 	select * from Student s join Class c on s.class_id = c.class_id;
-- end $$

-- call show_data()
-- delimiter ;
-- delimiter $$
-- create procedure insert_student(
-- in p_id int,
-- in p_student_name varchar(100),
-- in p_class_id int,
-- in p_age int,
-- in p_course_name varchar(100)
-- begin
-- 	insert into Student(id,student_name,class_id,age,course_name) values(p_id,p_student_name,p_class_id,p_age,p_course_name);
-- 	select * from Student;
-- end $$
-- delimiter ;


DELIMITER $$

CREATE PROCEDURE insert_student(
    IN p_id INT,
    IN p_student_name VARCHAR(100),
    IN p_class_id INT,
    IN p_age INT,
    IN p_course_name VARCHAR(100)
)
BEGIN
    INSERT INTO Student(id, student_name, class_id, age, course_name)
    VALUES (p_id, p_student_name, p_class_id, p_age, p_course_name);

    SELECT * FROM Student;
END $$
desc Student;
CALL insert_student(1, 'Amit', 1, 15, 'Science');
DELIMITER ;

drop procedure if exists insert_student;

 show procedure status where db='school';
 
 -- trigerrs
 
 create table player(
 id int auto_increment primary key,
 player_name varchar(100),
 player_team varchar(100),
 date_of_birth date,
 salary int);
 
 create table player_log(
 id int auto_increment primary key,
 player_id int,
 names varchar(100),
 created_on timestamp default current_timestamp
 );
 
 
 delimiter $$
 
 create trigger insert_player
 after insert on player
 for each row
 begin
	insert into player_log(id,names)
    values(new.id,new.player_name);
 end $$
 delimiter ;
 
 
 insert into player(player_name,player_team,date_of_birth, salary)
 values("virat","RCB",'1973-11-5',12345);
  insert into player(player_name,player_team,date_of_birth, salary)
 values("dhoni","CSK",'1973-7-7',2345);
 
 select * from player_log;
 select * from player;
 desc player_log;
 show triggers;
 
 -- distinct ,like etc
 
 select * from Student where student_name like 'a_%';
 
 select * from Student where student_name like '_p_';


select distinct course_name from Student; 

-- case statement

 select *,case when age>=18 then "adult" else "minor"
 end as category from Student;
 
 -- cte expression
 
 with join_table as (
 select c.room_id from Class c join Room r on c.room_id = r.room_id
 )
 
 select * from join_table;
 
 
 
 -- window function
 
 -- rank fucntion
 select *,rank() over(order by age) as age_rank from Student;
 
 -- dense_rank
 select *,dense_rank() over(order by age desc) from Student;
 
 -- in this final total is benn shown in every row
 select *,sum(subject_marks) over() as running_total_marks from Class;
 
 
 -- running total
 select *,sum(subject_marks) over(order by class_id) as running_total_marks from Class;
 
 
 
 -- total avg 
 select *,avg(subject_marks) over() as total_avg from Class;
 
 -- running avgrage
 select *,avg(subject_marks) over(order by class_id) from Class;
 
 -- rank fucntion
 select rank() over(order by subject_marks) from Class;
 
 
 
 
 