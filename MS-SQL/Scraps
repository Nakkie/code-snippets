Snippets


if exists(select * from sysobjects where name = 'STG_Coin_Data') begin drop table dbo.STG_Coin_Data end

---------

IF OBJECT_ID('tempdb..#temp_cc_li') IS NOT NULL DROP TABLE #temp_cc_li

---------

if exists(select * 
          from sys.objects a
		  left join sys.schemas b on a.schema_id = b.schema_id
		  where a.name = 'sources'
		  and b.name = 'dim') 
begin 
drop table dbo.STG_Coin_Data 
end

create index option 1
if not exists(select * from sys.indexes where name = 'CT_Index' and object_id = object_id('maestrodb.maestro.CONTENTTRACE')) 
begin
create nonclustered index CT_Index on maestrodb.maestro.CONTENTTRACE (SEAL desc, LASTUPDATE desc, LUSERUPDATE desc)
with (drop_existing = ON, ONLINE = ON)
end



fixing line breaks in output

replace(replace(replace(@sql,char(10),''),char(13),''),char(32),'')


remove chars from string
WHILE PATINDEX('%[^0-9]%', @strText) > 0
    BEGIN
        SET @strText = STUFF(@strText, PATINDEX('%[^0-9]%', @strText), 1, '')
    END

ApplyComparison("#0 >= convert(int,convert(varchar(6),dateadd(mm,-6,getdate()),112))",Month@ID)
