alter table player_bios
add column new_height numeric;

UPDATE player_bios
SET new_height = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer ;

alter table player_bios
drop column height;

alter table player_bios 
rename column new_height to height;

select firstname,lastname,height from player_bios limit 5;