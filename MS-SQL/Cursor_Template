Declare @var varchar(max)
	 --,@sql varchar(max)
;

DECLARE cursor_name CURSOR FOR 
SELECT field
FROM table_name;

OPEN cursor_name

FETCH NEXT FROM cursor_name 
INTO @var

WHILE @@FETCH_STATUS = 0
BEGIN
	--insert script here

       FETCH NEXT FROM cursor_name 
	   INTO @var
END 
CLOSE cursor_name;
DEALLOCATE cursor_name;
