-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

/* clean database for testing if database exists */
DROP DATABASE IF EXISTS tournament;

/* create database tournament */
CREATE DATABASE tournament;

/* connect to tournament databse */
\connect tournamnet;

/* create players table to keep track of players
	1. assigns unique id for each player
	2. contains player name */
CREATE TABLE players (
	id serial PRIMARY KEY,
	name text
);

/* create matches table to keep track of results from tournament
	1. assigns unique id for each match
	2. winner id
	3. reference to player table using foreign key */
CREATE TABLE matches (
	match serial PRIMARY KEY,
	winner_id integer REFERENCES players(id),
	loser_id integer REFERENCES players(id),
);

/* create view that displays player ranking in descending order using subquery
	1. count number of win from matches table
	2. count number of matches
	3. organize player ranking in descending order 
	4. table contains columns:
		+++++++++++++++++++++++++++++++++++++++++++++++++++++
		+ player id | player name | win count | match count +
		+++++++++++++++++++++++++++++++++++++++++++++++++++++
	*/
CREATE VIEW results as
SELECT players.id, players.name,
-- count number of wins for each player
(SELECT count(*) FROM matches, players WHERE winner_id = players.id) as WinCount, 
-- count number of matches for each player
(SELECT count(*) FROM matches WHERE players.id in (winner_id, loser_id)) as MatchCount
FROM players
GROUP BY players.id
ORDER BY WinCount DESC;

/* create view of win count */
-- CREATE VIEW WinCount as
-- SELECT winner_id, count(winner_id) as WinNum
-- FROM matches 
-- WHERE matches.winner_id = players.id
-- GROUP BY matches.winner_id
-- ORDER BY WinNum;

/* create view of win count */
-- CREATE VIEW MatchCount as
-- SELECT count(*) as MatchNum
-- FROM matches 
-- WHERE players.id in (winner_id, loser_id)
-- GROUP BY matches.winner_id
-- ORDER BY MatchNum;