<h1>Tournament Results Project</h1>
Udacity Fullstack Nanodegree
December 26th, 2016

The goal here is to create a simple tournament results database that uses a swiss tournament style to keep track of players, matches, and standing.

<h3>Project specifications</h3>
1. tournament.sql - database schema
2. tournament_test.py
3. tournament.py - module code with functions
	a. deletePlayer - Clear out all the player records from the database.
	b. deleteMatch - Clear out all the match records from the database.
	c. countPlayers - Returns the number of currently registered players.
	d. registerPlayer(name) - Adds a player to the tournament by putting an entry in the database.
	e. reportMatch(winner, loser) - Stores the outcome of a single match between two players in the database.
	f. playerStanding() - Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.
	g. swissParing() - Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players.
	

<h3>Running the project</h3>
1. Install Python if necessary.
2. Install Vagrant and VirtualBox.
3. Clone repository to local machine.
4. Navigate to vagrant/tournament folder
5. Launch Vagrant VM by 'vagrant up'
6. Access VM by 'vagrant ssh'
7. Start psql -> type '\i tournament.sql' -> type '\q'
9. Type 'python tournament_test.py'

NOTE: The same tournament files are present in root folder in case user already have vagrant set up and want to test the files.
