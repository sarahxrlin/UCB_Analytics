SELECT  count(*) -- players.*, seasons_stats.*
FROM players
INNER JOIN seasons_stats ON
players.player = seasons_stats.player
limit 50;

select * 
from seasons_stats
limit 10;

select *
from players
limit 10;

show tables from Miscellaneous_DB;

select p.player, p.height, p.weight, p.college, p.born, s.pos, s.tm
from players as p 
inner join seasons_stats s
	on p.player = s.player
;

SELECT p.player, s.year, s.pos, s.`2P%`, s.`FG%`, s.`FT%`, s.`TS%`
FROM seasons_stats s
INNER JOIN players p 
	ON s.player = p.player;

