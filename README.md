# Swiss Pairings Tournament Code

Udacity Fullstack Web Developer Nanodegree project Tournament Results

## Overview

This project includes a SQL module that creates a database for storing data on a "swiss pairings" style tournament, as well as a Python code module for creating records of tournament players, matches and results to be stored in the database.

## Requirements

- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Python ~2.7](https://www.python.org/)

## Set Up

For an initial set up please follow these 2 steps:

1. Download or clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Find the *tournament* folder and replace it with the content of this current repository, by either downloading it or cloning it - [Github Link](https://github.com/famazi111/Tournament).

## Testing the modules

1. On the vagrant machine go to the folder */vagrant/tournament*
2. Open PSQL by typing psql
3. Type \i tournament.sql
4. Type \q to quit out of PSQL
5. Run the tests by typing python tournament_test.py and the output should be:
```
    vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
    1. countPlayers() returns 0 after initial deletePlayers() execution.
    2. countPlayers() returns 1 after one player is registered.
    3. countPlayers() returns 2 after two players are registered.
    4. countPlayers() returns zero after registered players are deleted.
    5. Player records successfully deleted.
    6. Newly registered players appear in the standings with no matches.
    7. After a match, players have updated standings.
    8. After match deletion, player standings are properly reset.
    9. Matches are properly deleted.
    10. After one match, players with one win are properly paired.
    Success!  All tests pass!
```
