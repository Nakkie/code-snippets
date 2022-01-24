drop procedure if exists `cursorthing`;

DELIMITER $$
create procedure cursorthing ()

BEGIN

	declare finished int default 0;
    declare id int default 0;

	-- declare cursor
	declare <cursorlist>
		cursor for
			<select statement>
      ;

	-- declare NOT FOUND handler
	declare continue handler
        for not found set finished = 1;

	open <cursorlist>;

	<loopname>: loop
		fetch <cursorlist> into id;
		if finished = 1 then
			leave <loopname>;
		end if;

			<select statement>

	end loop <loopname>;
	close <cursorlist>;

END$$
DELIMITER ;
