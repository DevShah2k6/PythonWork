
use startersql2;
CREATE TABLE admin_users(
id int primary key,
name varchar(100),
email varchar(100),
gender enum('male','female','other'),
date_of_birth date,
salary int);

INSERT INTO admin_users 
(id, name, email, gender, date_of_birth, salary)
VALUES
(1, 'Amit Sharma', 'amit@gmail.com', 'male', '1998-05-14', 45000),
(2, 'Neha Patel', 'neha@gmail.com', 'female', '1999-08-22', 52000),
(3, 'Raj Verma', 'raj@gmail.com', 'male', '1997-12-10', 48000),
(4, 'Sara Khan', 'sara@gmail.com', 'female', '2000-03-18', 55000),
(5, 'Alex Roy', 'alex@gmail.com', 'other', '1996-07-30', 60000),
(6, 'John Doe', 'john@gmail.com', 'male', '1995-11-25', 60000);

TRUNCATE TABLE admin_users;