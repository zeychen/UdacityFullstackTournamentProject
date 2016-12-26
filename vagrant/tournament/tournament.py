#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    con = connect()
    cursor = con.cursor()
    query = "DELETE FROM matches;"
    cursor.execute(query)
    con.commit()
    con.close()


def deletePlayers():
    """Remove all the player records from the database."""
    con = connect()
    cursor = con.cursor()
    query = "DELETE FROM players;"
    cursor.execute(query)
    con.commit()
    con.close()


def countPlayers():
    """Returns the number of players currently registered."""
    con = connect()
    cursor = con.cursor()
    query = "SELECT count(*) FROM players;"
    cursor.execute(query)
    player_count = cursor.fetchone()[0]
    con.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    con = connect()
    cursor = con.cursor()
    bleach_name = bleach.clean(name)
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (bleach_name, ))
    con.commit()
    con.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played

    standing table contains columns:
        +++++++++++++++++++++++++++++++++++++++++++++++++++++
        + player id | player name | win count | match count +
        +++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    con = connect()
    cursor = con.cursor()
    query = "SELECT * from results"
    cursor.execute(query)
    standing_result = cursor.fetchall()
    con.close()
    return standing_result



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    con = connect()
    cursor = con.cursor()
    # bleached_winner = bleach.clean(winner)
    # bleached_loser = bleach.clean(loser)
    cursor.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s)", (winner, loser))
    # if isinstance(bleached_winner, (int, long, float)) and isinstance(bleached_loser, (int, long, float)):
    #     cursor.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s)", (bleached_winner ,) (bleached_loser ,))
    #     con.commit()
    # else:
    #     return "please enter integers for winner and loser ids"
    con.commit()
    con.close()

 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    con = connect()
    cursor = con.cursor()
    query = "SELECT result_id, result_name from results"
    cursor.execute(query)
    standing_result = cursor.fetchall()
    # use pairs array to store tuple
    pairs = []
    standing_length = int(countPlayers())

    # loop through every other row in standing_result
    # append id and name of players in current and +1 position within loop 

    if (standing_length > 0):
        for x in range(standing_length):
            if (x%2 == 0):
                pairing = (standing_result[x][0], standing_result[x][1], standing_result[x+1][0], standing_result[x+1][1])
                pairs.append(pairing)

    con.close()
    return pairs
