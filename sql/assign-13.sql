use hr_db;

# Write a query to select first 10 records from a table.
select * from employees limit 10;

# Write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name"
select first_name as 'First Name', last_name as 'Last Name' from employees;

# Get unique department id list
select distinct department_id from employees;

# Write a query to get all employee details from the employee table order by first name, descending.
select * from employees order by first_name desc;

# Write a query to display fullname and salary
select concat(first_name, "", last_name) as FullName,salary  from employees;

# display all employee salary wise from lowest to highest
select * from employees order by salary asc;

# how much money the company is spending on employees on salary
select sum(salary) from employees;

# show min, max and avg salary of comapny staff
select min(salary) as Min_Salary from employees;
select max(salary) as Min_Salary from employees;
select avg(salary) as Min_Salary from employees;

# show employee name, their salary and the avg salary of all staff
select concat(first_name, "", last_name) as FullName , salary  from employees; -- , avg(salary) as avg_emp_salary 

# how many emplyee does the company have, display the count
select count(employee_ID) from Employees;

# show the number of employees in the company and the avg salary of all staff
select count(employee_ID) as no_of_employees ,avg(salary) as avg_employee_salary from Employees;

# Write a query to get the number of jobs available in the employees table.
select count(distinct job_id) from employees;

# Write a query get all first name from employees table in upper case.
select  upper(first_name) from employees;

# Write a query to get first name from employees table after removing white spaces from both side.
select  trim(first_name) from employees;

# Write a query to get monthly salary (round 2 decimal places) of each and every employee
select round(salary,2) from employees;

# find the 3rd highest paid employee
# NOTE: the query should return 1 row only
select * from employees order by salary desc limit 1 offset 2;

# Write a query to display the fullname (first_name, last_name) and salary 
#for all employees whose salary is in the range $10,000 through $15,000.
select concat(first_name," ",last_name) as FullName , salary from employees where salary between 10000 and 15000;

# Write a query to display the fullname (first_name, last_name) and department ID 
#of all employees in departments 30 or 100. sort the resulting data in ascending order 
#department wise.
select concat(first_name," ",last_name) as FullName , department_id from employees where department_id =30 or  department_id =100;

# Write a query to display the fullname (first_name, last_name) and salary 
# for all employees whose salary is in the range $10,000 through $15,000 and 
# are in department 30 or 100.

select concat(first_name," ",last_name) as FullName , salary , department_id from employees
where salary between 10000 and 15000  
And  
department_id =30 or  department_id =100; 

# Write a query to display the fullname (first_name, last_name) and hire date 
# for all employees who were hired in 1987.
select concat(first_name," ",last_name) as FullName , hire_date from employees where hire_date like "%1987%";


select * from Employees;
select * from departments;
select * from jobs;
select * from countries;
select * from locations;
select * from regions;



# Assignment 1: Employees in Specific Departments
# Task: Retrieve the EMPLOYEE_ID, FIRST_NAME, and LAST_NAME of employees who work in departments located in cities that start with the letter 'S'.
# Hint: Use a subquery after the WHERE clause to find DEPARTMENT_IDs based on LOCATION_IDs from the locations table.

select employee_id, first_name,last_name from employees where department_id in 
(select department_id from departments where location_id in 
(select location_id from locations where city like 'S%')) ;

# Assignment 2: High Salary Jobs
# Task: List the JOB_ID and JOB_TITLE for jobs that have a minimum salary greater than the average salary across all jobs.
# Hint: Use a subquery after the WHERE clause to calculate the average salary.
select job_id, department_id from employees where salary >(select avg(salary) from employees);

select * from employees; 


# Assignment 3: Employee and Their Manager's Details
# Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and MANAGER_ID of employees along with the FIRST_NAME and LAST_NAME of their managers.
# Hint: Use a subquery after the FROM clause to join the employees table to itself to get the manager's details.

        SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, m.first_name as manager_fname, m.last_name as manager_lname
        FROM employees e
        JOIN employees m
        ON e.manager_id = m.employee_id;

# Assignment 4: Departments with Employees Hired After a Specific Date
# Task: Retrieve DEPARTMENT_ID and DEPARTMENT_NAME for departments that have employees hired after '01-JAN-2010'.
# Hint: Use a subquery after the WHERE clause to find departments based on hire dates in the employees table.



-- Assignment 9: Employees Hired in Regions with a Specific Name
-- Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and HIRE_DATE of employees who were hired in regions with the name 'Europe'.
-- Hint: Use a subquery after the FROM clause to join employees with locations, countries, and regions tables.

select employee_id, first_name, last_name , hire_date from employees where department_id in 
( select department_id from departments where location_id in
( select location_id from locations where country_id in
( select country_id from countries where region_id in 
( select region_id from regions where region_name ="Europe")
)
)
);



    SELECT job_id, job_title
    FROM jobs
    WHERE job_id IN (
      SELECT job_id
      FROM job_history
      GROUP BY employee_id
      HAVING COUNT(DISTINCT department_id) > 1
    )






