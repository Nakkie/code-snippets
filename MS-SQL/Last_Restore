with LastRestores as
(
select
    DatabaseName = [d].[name] ,
    [d].[create_date] ,
    [d].[compatibility_level] ,
    [d].[collation_name] ,
    r.*,
    RowNum = row_number() over (partition by d.Name order by r.[restore_date] desc)
from master.sys.databases d
left join msdb.dbo.[restorehistory] r ON r.[destination_database_name] = d.Name
)
select *
from [LastRestores]
where [RowNum] = 1
