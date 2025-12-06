USE classicmodels;

select * from employees;
select * from classicmodels.employees;
select * from employees limit 5;
select * from employees order by firstName;
select * from employees order by firstName desc;
select * from employees order by firstName desc limit 2;



select firstname , lastname from employees;
select firstname as fname, lastname as lname from employees;


select * from employees limit 5; 
select * from employees limit 5 offset 5; 
select * from employees limit 5 offset 10; 

select MAX(amount) from payments;
select MAX(amount) from payments where year(paymentDate) =2003;
select *,MAX(amount) from payments where year(paymentDate) =2003;
select * from payments where year(paymentDate) =2003 And amount =MAX(amount);

