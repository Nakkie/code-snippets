-- dummy table used as example
drop table if exists example_param_tbl;

create table example_param_tbl (
   date_input date,
   data_field_1 text,
   data_field_2 text,
   run_date date
);

-- procedure to execute code
-- basic insert functionality
-- need to always have a destination, otherwise proc breaks on call
create or replace procedure example_param_proc (
   date_input text,
   data_field_1 text,
   data_field_2 text
)
language plpgsql    
as $$
begin
   
	insert into example_param_tbl
	select date_input::date, data_field_1, data_field_2, now()::date as payload_date;
	
end;$$

-- calling / executing the proc
call example_param_proc ('2021-10-01', 'Data Value 1', 'Data Value 2');


-- example of proc call result
select *
from example_param_tbl;