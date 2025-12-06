
use assignment_db;


insert into category(name) values("Category 1");
insert into category(name) values("Category 2");
insert into product (name,description, cat_id) values("Item 1",Null,1);
insert into product (name,description, cat_id) values("Item 2",Null,1);
insert into product (name,description, cat_id) values("Item 3",Null,1);
update product set cat_id = 2 where id=1;



select * from product;

