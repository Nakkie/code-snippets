select 
(@row_number:=@row_number + 1)+max_id as rownumber, 
mycolumns
from mytable
,(select @row_number:=0) as rn
order by mycolumns
