-- QUERY IS NOTHING BUT THE COMMAND JUST LIKE WE WRITE THE COMMAND IN CMD

create DATABASE startersql;

-- to use the databse we write this
use startersql;
use startersql2;

-- creating a table

CREATE TABLE users(
id INT auto_increment PRIMARY KEY,
names varchar(100) NOT NULL,
email VARCHAR(100) unique not null,
gender enum('male','female','other') ,
date_of_birth DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from users;


-- to delete the all things from a database 
-- it will remoove all things 
-- drop database startersql;

-- datatypes
/*
-int
-varchar
-enum
date
-timestamp

*/

-- constraints

/*
-auto_increment - it increments automaticallay by one
- primary key - make the column the primary key
-not null - it makes that data should not be empty in an column 
-unique-it makes the unique vLue like roll no which is unique like aadhar number
-default-set a default value if not value is selected 
*/

select * from users;

-- to select specific columm
select id,email from users;


-- to rename the table
rename table users to programmers;

select * from programmers;

-- programmers to users
rename table programmers to users;

-- to altering the table using this
alter table users add is_active boolean default  true;

select * from users;


-- to drop the column
alter table users drop column is_active;


select * from users;


-- to modify column
alter table users modify column names varchar(150);

-- to do email after id using this 
 alter table users modify column email varchar(100) after id; 

-- column of date of birth is in first column
alter table users modify column date_of_birth DATETIME first;


-- inserting the data 

-- insert into users values('2013-2-12',1,'harry@codewithharry.com','alice','Male',default);

-- inserting data using specific column
-- insert into users(names,email,gender,date_of_birth) values('harry','harry2@codewithharry.com','Male',default);
insert into users(names,email,gender,date_of_birth) values('harry12','harry12@codewithharry.com','Female','2025-1-12'),
('harry3','haary3@copdewithharry.com','male','2025-2-12'),
('harry4','harry4@codewithharry.com','male','2025-3-12');

select * from users;

select * from addresses;

-- inner join 
select users.name ,addresses.city,users.gender,addresses.id as addresses_id from users inner join addresses on users.id = addresses.user_id;



