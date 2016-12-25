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
		player_id serial PRIMARY KEY,
		name text NOT NULL
);

/* create matches table to keep track of results from tournament
	1. assigns unique id for each match
	2. tabulates win or loss for each player
	3. reference to player table using foreign key */
CREATE TABLE matches (
		match_id serial PRIMARY KEY,
		win int,
		loss int,
		FOREIGN KEY (player_id) REFERENCES players(player_id),
		FOREIGN KEY (player_name) REFERENCES players(name)
);

/* create view to show player standing within tournament
	1.  */

