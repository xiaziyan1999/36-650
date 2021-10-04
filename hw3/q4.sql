CREATE TABLE new_table (
player integer references more_player_stats, 
prl numeric, 
position text
);

insert into new_table (player,prl) (select id,round(per - 67*va/(gp*minutes),1) from more_player_stats);

update new_table 
set position = case 
when player in (select player from new_table where prl >= 11.3)then 'PF'
when player in (select  player from new_table where prl >= 10.6 and prl < 11.3 )then 'PG'
when player in (select player from new_table where prl >= 0 and prl < 10.6 ) then 'SG/SF'
end;

select * from new_table limit 10;