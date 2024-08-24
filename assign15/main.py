import db
from query import *
import json

db_conn = db.mysqlconnect()
# assign 1
employees = get_employees(db_conn)
# print(
#   json.dumps(employees, default=str, indent=4)
# )

# assign 2
employees_in_specific_departments = get_employees_in_specific_departments(db_conn)
# print(
#   json.dumps(employees_in_specific_departments, default=str, indent=4)
# )

# assign 3
emp_with_salary_gt_avg =get_high_salary_jobs(db_conn)
# print(
#   json.dumps(emp_with_salary_gt_avg, default=str, indent=4)
# )

# assign 4
emp_and_mgr_detail = emp_and_mgr_details(db_conn)
# print(
#   json.dumps(emp_and_mgr_detail, default=str, indent=4)
# )

# assign 5
location_with_mul_depts =get_locations_with_multiple_departments(db_conn)
# print(
#   json.dumps(location_with_mul_depts, default=str, indent=4)
# )

# assign 6
emp_with_salary_gt_avg =get_employees_with_max_salary(db_conn)
# print(
#   json.dumps(get_employees_with_max_salary, default=str, indent=4)
# )

# assign 7
# emp_in_mul_depts =get_jobs_with_employees_in_multiple_departments(db_conn) // not working
# print(
#   json.dumps(emp_in_mul_depts, default=str, indent=4)
# )


# assign 8

depts_without_mngrs = get_departments_without_managers(db_conn)
# print(
#   json.dumps(depts_without_mngrs, default=str, indent=4)
# )

# assign 9

emp_hired_from_europe = get_employees_hired_in_specific_region(db_conn)
# print(
#   json.dumps(emp_hired_from_europe, default=str, indent=4)
# )

# assign 10
emp_with_recent_job_chnages = get_recent_job_changes(db_conn)
print(
  json.dumps(emp_with_recent_job_chnages, default=str, indent=4)
)




