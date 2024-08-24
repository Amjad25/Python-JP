import pymysql
def get_employees(db_conn: pymysql.Connection):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM employees")
  return cur.fetchall()


def add_employee(db_conn, data):
  cur = db_conn.cursor()
  employee_id = data['employee_id']
  fname = data['fname']
  lname = data['lname']
  email = data['email']
  cur.execute(
    f"""
      INSERT INTO employees 
      VALUES (
        {employee_id}, 
        '{fname}',
        '{lname}', 
        '{email}', 
        '515.123.4567', 
        '1987-06-17', 
        'AD_PRES', 
        '24000.00', 
        '0.00', 
        '0', 
        '90'
      )

    """)
  db_conn.commit()
  
# Assignment 1: Employees in Specific Departments
# Task: Retrieve the EMPLOYEE_ID, FIRST_NAME, and LAST_NAME of employees who work in departments located in cities that start with the letter 'S'.
# Hint: Use a subquery after the WHERE clause to find DEPARTMENT_IDs based on LOCATION_IDs from the locations table.
def get_employees_in_specific_departments(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT employee_id, first_name, last_name
    FROM employees
    WHERE department_id IN (
      SELECT department_id
      FROM departments
      WHERE location_id IN (
        SELECT location_id
        FROM locations
        WHERE city LIKE 'S%'
      )
    )
    """
  )
  return cur.fetchall()

# Assignment 2: High Salary Jobs
# Task: List the JOB_ID and JOB_TITLE for jobs that have a minimum salary greater than the average salary across all jobs.
# Hint: Use a subquery after the WHERE clause to calculate the average salary.

def get_high_salary_jobs(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    select job_id, department_id from employees 
    where salary >(select avg(salary) 
    from employees)
    """
  )
  return cur.fetchall()


# Assignment 3: Employee and Their Manager's Details
# Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and MANAGER_ID of employees along with the FIRST_NAME and LAST_NAME of their managers.
# Hint: Use a subquery after the FROM clause to join the employees table to itself to get the manager's details.

def emp_and_mgr_details(db_conn: pymysql.Connection):
    cur = db_conn.cursor()
    cur.execute(
        """
        SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, m.first_name as manager_fname, m.last_name as manager_lname
        FROM employees e
        JOIN employees m
        ON e.manager_id = m.employee_id
        
        """
    )
    return cur.fetchall()


# Assignment 4: Departments with Employees Hired After a Specific Date
# Task: Retrieve DEPARTMENT_ID and DEPARTMENT_NAME for departments that have employees hired after '01-JAN-2010'.
# Hint: Use a subquery after the WHERE clause to find departments based on hire dates in the employees table.

def get_departments_hired_after_date(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT department_id, department_name
    FROM departments
    WHERE department_id IN (
      SELECT department_id
      FROM employees
      WHERE hire_date > '2010-01-01'
    )
    """
  )
  return cur.fetchall()



# Assignment 5: Locations with Multiple Departments
# Task: List LOCATION_ID and CITY for locations that have more than one department.
# Hint: Use a subquery after the FROM clause to group and count departments per location.


def get_locations_with_multiple_departments(db_conn: pymysql.Connection):
   
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT location_id, city
    FROM locations
    WHERE location_id IN (
      SELECT location_id
      FROM departments
      GROUP BY location_id
      HAVING COUNT(*) > 1
    )
    """
  )
  return cur.fetchall()

# Assignment 6: Employees with Maximum Salary in Their Department
# Task: Retrieve the EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and SALARY of employees who earn the maximum salary in their respective departments.
# Hint: Use a subquery after the WHERE clause to find the maximum salary per department.

def get_employees_with_max_salary(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT employee_id, first_name, last_name, salary
    FROM employees e
    WHERE salary = (
      SELECT MAX(salary)
      FROM employees
      WHERE department_id = e.department_id
    )
    """
  )
  return cur.fetchall()

# Assignment 7: Jobs with Employees in More Than One Department
# Task: List JOB_ID and JOB_TITLE for jobs where employees have worked in more than one department (including past jobs from the job_history table).
# Hint: Use a subquery after the WHERE clause to check the number of distinct departments per employee from the job_history table.

def get_jobs_with_employees_in_multiple_departments(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT job_id, job_title
    FROM jobs
    WHERE job_id IN (
      SELECT job_id
      FROM job_history
      GROUP BY employee_id
      HAVING COUNT(DISTINCT department_id) > 1
    )
    """
  )
  return cur.fetchall()

# Assignment 8: Departments Without Managers
# Task: Retrieve DEPARTMENT_ID and DEPARTMENT_NAME for departments that do not have a manager assigned.
# Hint: Use a subquery after the WHERE clause to identify departments where MANAGER_ID is NULL.

def get_departments_without_managers(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT department_id, department_name
    FROM departments
    WHERE department_id NOT IN (
      SELECT department_id
      FROM employees
      WHERE manager_id IS NOT NULL
    )
    """
  )
  return cur.fetchall()

# Assignment 9: Employees Hired in Regions with a Specific Name
# Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and HIRE_DATE of employees who were hired in regions with the name 'Europe'.
# Hint: Use a subquery after the FROM clause to join employees with locations, countries, and regions tables.

def get_employees_hired_in_specific_region(db_conn: pymysql.Connection):
 
  cur = db_conn.cursor()
  cur.execute(
    """
select employee_id, first_name, last_name , hire_date from employees where department_id in 
( select department_id from departments where location_id in
( select location_id from locations where country_id in
( select country_id from countries where region_id in 
( select region_id from regions where region_name ="Europe")
)
)
)
    """
  )
  return cur.fetchall()


# Assignment 10: Recent Job Changes
# Task: List EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and the latest job JOB_ID for employees who have had more than one job.
# Hint: Use a subquery after the FROM clause to get the latest START_DATE from the job_history table.

def get_recent_job_changes(db_conn: pymysql.Connection):
   
  cur = db_conn.cursor()
  cur.execute(
    """
    SELECT employee_id, first_name, last_name, job_id
    FROM employees
    WHERE employee_id IN (
      SELECT employee_id
      FROM job_history
      WHERE start_date = (
        SELECT MAX(start_date)
        FROM job_history
        WHERE employee_id = employees.employee_id
      )
      GROUP BY employee_id
      HAVING COUNT(*) > 1
    )
    """
  )
  return cur.fetchall()

