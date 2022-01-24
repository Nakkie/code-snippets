select so.name 'Table Name'
		,c.name 'Column Name'
		,t.Name 'Data type'
		,c.max_length 'Max Length'
		,c.precision
		,c.scale
		,c.is_nullable
		,ISNULL(i.is_primary_key, 0) 'Primary Key'
from sys.columns c
inner join sys.types t ON c.user_type_id = t.user_type_id
left join sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id
left join sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
right join sysobjects so on so.id = c.object_id
where so.type = 'u'
order by so.name, c.name
