# creating  a Table

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    salesperson_id INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);


INSERT INTO sales (salesperson_id, sale_amount, sale_date) VALUES 
(1, 12000.00, '2024-08-01'),
(1, 8000.00, '2024-08-01'),
(1, 15000.00, '2024-08-02'),
(1, 11000.00, '2024-08-03'),
(2, 5000.00, '2024-08-01'),
(2, 12000.00, '2024-08-02'),
(2, 9000.00, '2024-08-02'),
(3, 10000.00, '2024-08-01'),
(3, 4000.00, '2024-08-03'),
(4, 8000.00, '2024-08-04'),
(4, 9000.00, '2024-08-04'),
(4, 7000.00, '2024-08-04');


select * from sales;

# select avg sales where salesperson id =1
select * from sales where salesperson_id =1 ; # 
select avg(sale_amount) from sales where salesperson_id =1 group by sale_date;


select * from sales where salesperson_id =1 ;
select avg(sale_amount) from( select * from sales where salesperson_id =1 group by saledate);


# avg of an employee day sales
select avg(avgSalesAmount) from (
	select sum(sale_amount) as avgSalesAmount,sale_date from sales where salesperson_id =1 group by sale_date
    ) as t;
    
# sum up employee daily sale 
select sum(sale_amount) as daily_sale,salesPerson_id from sales group by sale_date , salesPerson_id;

# over all sum of all employees

    select avg(t.daily_avg_sale) from (
select sum(sale_amount) as daily_avg_sale,salesPerson_id from sales group by sale_date , salesPerson_id
    ) as t group by salesperson_id;
    
# table insert formats
select * from offices;

insert into table_name  () values();
insert into offices(officecode,city,phone,addressline1,addressline2,country,postalcode,territory) 
values('1001','karachi','2323','sdsd','aadd2','Pakistan','74800','3323sad');

insert into table_name values();
insert into offices values('1002','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad',"sd");
insert into offices values('1002','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad');
insert into offices values('1002','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad');
insert into offices values('1002','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad');


insert into table_name values (), (),(), (),(),(),();
insert into offices values('1003','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad',"sd"),('1004','karachi','232S3','sdsd','aadd2','Pakistan','74800','3323sad',"dsd") ;


# UPDATE

# to update more tahn one row we need to off this ploicy
set sql_safe_updates =0;

# where is very mcuh necessary ELSE all data can be manipulated
update table_name set col_name = value where  col_name = value;
 # make karacho to hyderapabd
 update offices set city = "Hyderabad" where city ="karachi";


# DELETE 
delete from table where col_name =value;
delete from offices where officecode ="1002";


# constraint
# not nulll
# unique
# foreign key
	# cascade
    # set null
    # restrict
    # No Action
    # Set Default









