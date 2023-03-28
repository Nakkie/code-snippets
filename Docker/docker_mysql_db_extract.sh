docker exec -it 5e9be815b3b2 bash
mysqldump -u root — password=password123 db_name > backup_test.sql

docker cp 5e9be815b3b2:/file/path/within/container /host/path/target
