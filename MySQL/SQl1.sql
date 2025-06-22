use pydata;
UPDATE my_contact
SET address= 'mandalay'
WHERE last_name = 'ma';

select * from my_contact;

truncate table my_contact;

insert into my_contact(first_name, last_name, address, mark) values ('mg', 'mg', 'naypyitaw', 400);
insert into my_contact(first_name, last_name, address, mark) values ('hla', 'mg', 'naypyitaw', 500);
insert into my_contact(first_name, last_name, address, mark) values ('aung', 'mg', 'naypyitaw', 100);

SELECT max(mark)
FROM my_contact

