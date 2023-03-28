drop event if exists `maintain_thisproc`;

create event maintain_event
			on schedule every 10 day_minute
                
			do
				call thisproc;
