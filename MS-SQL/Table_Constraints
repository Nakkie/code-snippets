select OBJECT_NAME(OBJECT_ID) AS NameofConstraint
		,b.name as TableName
FROM sys.objects a
left join sysobjects b on a.parent_object_id = b.id
where a.type_desc LIKE '%CONSTRAINT'
and b.name != 'sysdiagrams';
