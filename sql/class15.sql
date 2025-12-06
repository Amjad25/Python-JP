select * from orderdetails;
select * from products;

select productcode from products where productname ='pont yacht';
select * from orderdetails where productcode ='S72_3212';
# this is same query as line 4 & 5 combined but optimized one
select * from orderdetails where productCode =(select productcode from products where productname ='pont yacht');


select * from orders order by customernumber;

select * from orders where customerNumber = '103'  order by orderdate limit 1 ;# that is my qquery 

select * from orders where orderdate =(select min(orderdate) from orders) and where customernumber ='103';

select min(orderdate), customernumber from orders group by customernumber;
select max(orderNumber), customernumber from orders group by customernumber;

# latest order of all customer
select * from orders where (select max(orderNumber)from orders group by customernumber);

# OFFICES
select * from employees;
select * from offices;

# select all employees who are in USA
select * from employees where (select officeCode from offices where country ='USA' limit 1); # my query
select * from employees where officecode IN (select officeCode from offices where country ='USA' ); # sir's query


# product by price highest
select * from products order by buyPrice ;
# top fice by hughest price
select * from products order by buyPrice desc limit 5 ;

# top 5 in order of asec
select * from (select * from products order by buyPrice desc limit 5) as t order by t.buyPrice asc;

use classicmodels;
select * from employees where jobTitle ='Sales Rep' OR 1=1;
				-- Sales Rep ' OR '1=1
select * from employees where jobTitle = 1=1;

select * from employees where jobTitle ='Sales Rep' OR '1=1';










