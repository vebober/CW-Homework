drop table departments;

create table departments(
	id serial primary key,
	dept_no varchar(4) not null,
	dept_Name varchar not null);
	
select * from departments;

drop table dept_emp;

create table dept_emp(
	id serial primary key,
	emp_no integer not null,
	dept_no varchar(4) not null,
	from_date varchar not null,
	to_date varchar not null);
	
select * from dept_emp;

drop table dept_manager;

create table dept_manager(
	id serial primary key,
	dept_no varchar(4) not null,
	emp_no integer not null,
	from_date varchar not null,
	to_date varchar not null);

select * from dept_manager;

drop table employees;

create table employees(
	id serial primary key,
	emp_no integer not null,
	birth_date varchar not null,
	first_name varchar not null,
	last_name varchar not null,
	gender varchar not null,
	hire_date varchar not null);
	
select * from employees;

drop table salaries;

create table salaries(
	id serial primary key,
	emp_no integer not null,
	salary integer not null,
	from_date varchar not null,
	to_date varchar not null);

select * from salaries;

drop table titles;

create table titles(
	id serial primary key,
	emp_no integer not null,
	title varchar not null,
	from_date varchar not null,
	to_date varchar not null);
	
select * from titles;
	


