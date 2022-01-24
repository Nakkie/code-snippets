declare @user varchar(7)
		,@userstring varchar(20)
		,@dbname varchar(20)
		,@sql varchar(max)
		,@statusInd tinyint
		
set @user = 'userID'
set @userstring = 'domain\'+@user
set @dbname = 'DBName'
set @statusInd = 0

while (@statusInd = 0)
begin
	begin try		
		if exists (Select name 
				   from Sys.Databases
					where name = @dbname)
					begin
					set @statusInd = 1
					

			set @sql = 'use master

			if not exists (select loginname 
						  from master.dbo.syslogins 
						  where name = '''+@userstring+''')
			create login ['+@userstring+'] from windows;

			use '+@dbname+'
			if not exists (select name 
						  from sys.database_principals
						  where name = '''+@userstring+''')
			create user ['+@userstring+'] for login ['+@userstring+'] with default_schema = [db_datareader];

			if not exists (select name
							from sys.database_role_members
							left join sys.database_principals on member_principal_id = principal_id
							where role_principal_id = 16390
							and name = '''+@userstring+''')
			exec sp_addrolemember ''db_datareader'', ['+@userstring+'];

			'
			exec (@sql)
					end
	end try

	begin catch
		waitfor delay '00:05:00'
	end catch
end
