declare @tablename varchar(max)
		,@columnname varchar(max)
		,@sql varchar(max);

DECLARE cursor_name CURSOR FOR 
select a.name as TableName
	   ,b.name as ColumnName
from sysobjects a
left join syscolumns b on a.id = b.id
where a.name = 'DBName';

OPEN cursor_name

FETCH NEXT FROM cursor_name 
INTO @tablename, @columnname

WHILE @@FETCH_STATUS = 0
BEGIN
		set @sql = 'sp_RENAME '''+@tablename+'.['+@columnname+']'' , '''+replace(rtrim(@columnname),' ','_')+''', ''COLUMN'''
		exec (@sql)

       FETCH NEXT FROM cursor_name 
	   INTO @tablename, @columnname
END 
CLOSE cursor_name;
DEALLOCATE cursor_name;
