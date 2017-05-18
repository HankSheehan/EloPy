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

    def addResults(self, name1, name2):
        """
        Should be called after a game is played.
        @param name1 - name of the first player.
        @param name2 - name of the second player.
        """
        expected1 = ( 1+10**( ( R2-R1 )/400 ) ) ** -1
        expected2 = ( 1+10**( ( R1-R2 )/400 ) ) ** -1
        rating1 = #new rating formula
        rating2 = #new rating forula

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