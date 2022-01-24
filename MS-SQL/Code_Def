select case when a.type = 'V'
            then 'View'
			when a.type = 'P'
            then 'Proc'
			end as ObjectType
      ,c.name+'.'+a.name as ObjectName
from sys.objects a
left join sys.sql_modules b on a.object_id = b.object_id
left join sys.schemas c on a.schema_id = c.schema_id
where b.definition like '%sample code%'
