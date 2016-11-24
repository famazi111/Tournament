#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception, e:
        print("The following error happened while trying to connect to the"
              "database\n" + str(e))


def deleteMatches():
    """Remove all the match records from the database."""
    conn, cur = connect()
    cur.execute("TRUNCATE matches;")
    conn.commit()
    cur.close()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, cur = connect()
    cur.execute("DELETE FROM players;")
    conn.commit()
    cur.close()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, cur = connect()
    cur.execute("SELECT count(id) FROM players;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn, cur = connect()
    query = "INSERT INTO players(name) values (%s);"
    params = (name,)
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cur = connect()
    cur.execute("SELECT * FROM standings;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, cur = connect()
    query = "INSERT INTO matches(winner, loser) VALUES(%s,%s);"
    params = (winner, loser)
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()


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
    # Needed information is in standings view, just filter it
    pairings = []
    standings = playerStandings()

    # transforms
    # [(id1, name1), (id2, name2), ...]
    # into
    # [(id1, name1, id2, name2), ...]
    n = len(standings)
    for i in range(0, n-1, 2):
        pairings += [(standings[i][0], standings[i][1], standings[i+1][0],
                      standings[i+1][1])]
    return pairings
