-- Create the tables

-- First version
CREATE TABLE employees (
       name VARCHAR(30),
       age INT,
       occupation VARCHAR(50)
);

-- Second version
CREATE TABLE employees (
       name VARCHAR(30) unique,
       age INT,
       occupation VARCHAR(50)
);

-- Third version (with primary key)
CREATE TABLE employees (
       id INTEGER PRIMARY KEY,
       name VARCHAR(30),
       age INT,
       occupation VARCHAR(50)
);

-- Dependents table (first version)
CREATE TABLE dependents(
       id INTEGER PRIMARY KEY,
       name VARCHAR(30),
       relationship VARCHAR(30),
       employee_id INTEGER
);

-- Dependents table (final version - with foreign key)
-- requires PRAGMA in next line to work
-- PRAGMA foreign_keys = ON;

CREATE TABLE dependents(
       id INTEGER PRIMARY KEY,
       name VARCHAR(30),
       relationship VARCHAR(30),
       employee_id INTEGER,
       FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Insert some data

INSERT INTO employees(name, age, occupation) VALUES('John', 40, 'Carpenter');
INSERT INTO employees(name, age, occupation) VALUES('Jack', 35, 'Driver');
INSERT INTO employees(name, age, occupation) VALUES('Bill', 50, 'Salesman');
INSERT INTO employees(name, age, occupation) VALUES('John', 25, 'Bellboy');

INSERT INTO employees(age, name, occupation) VALUES 
       (30, 'James', 'Waiter'), 
       (25, 'Fredrick', 'Bartender');   

-- Insert a dependent
INSERT INTO dependents(name, relationship, employee_id) VALUES ("Molly", "daughter", 2);   



-- Querying data

-- SELECT columns FROM table WHERE conditions; 

SELECT * from employees; -- All columns of all rows
SELECT name, age from employees; -- Only name and age (control the columns)
SELECT * from employees WHERE age > 35; -- Only rows where age is greater than 35 (control rows)
SELECT name from employees WHERE age > 35; -- Control columns and rows
SELECT count(name) from employees WHERE age > 35; -- Aggregate functions (how many employees are older than 35)

-- Modifying rows

update employees set occupation='Waiter' where name = 'Fredrick'; -- Change Fredrick's job to waiter

-- Deleting rows

delete from employees where name = 'Bill'; -- Delete Bill

-- Joining tables
select dependents.name from employees, dependents where employees.name = "Jack" AND dependents.employee_id = employees.id; -- Dependents of Jack



