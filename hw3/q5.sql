alter table player_bios
add column position text;

UPDATE player_bios
SET position = (SELECT new_table.position FROM new_table
WHERE new_table.player=player_bios.id);

select firstname,lastname,position from player_bios limit 5;