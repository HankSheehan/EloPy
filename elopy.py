"""
Created 5-18-17
All of the classes for EloPy. The users should only interact with the Implementation class
@author - Hank Hang Kai Sheehan
"""

class Implementation:
    """
    A class that represents an implementation of the Elo Rating System
    """

    def __init__(self, base_rating=1000):
        """
        Runs at initialization of class object.
        @param base_rating - The rating a new player would have
        """
        self.base_rating = base_rating
        self.players = []

    def newPlayer(self, name, rating=base_rating):
        """
        Adds a new player to the implementation.
        @param name - The name to identify a specific player.
        @param rating - The player's rating.
        """
        self.players = Player(name=name,rating=rating)

    def contains(self, name):
        """
        Returns true if this object contains a player with the given name.
        Otherwise returns false.
        @param name - name to check for.
        """
        for player in self.players:
            if player.name == name:
                return True
        return False

    def __getPlayer(self, name):
        """
        TODO
        @param name - TODO
        """
        #TODO

    def addResults(self, name1, name2):
        """
        Should be called after a game is played.
        @param name1 - name of the first player.
        @param name2 - name of the second player.
        """
        expected1 = #new rating formula
        expected2 = #new rating formula
        rating1 = #new rating formula
        rating2 = #new rating formula

class _Player:
    """
    A class to represent a player in the Elo Rating System
    """

    def __init__(self, name, rating):
        """
        Runs at initialization of class object.
        @param name - TODO
        @param rating - TODO
        """
        self.name = name
        self.rating = rating

    def compareRating(self, opponent):
        """
        Compares the two ratings of the this player and the opponent.
        @param opponenet - the player to compare against.
        @returns - The expected score between the two players.
        """
        return ( 1+10**( ( opponent.rating-self.rating )/400 ) ) ** -1
