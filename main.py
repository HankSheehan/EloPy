from elopy import *

i = Implementation()

players = ["Joachim","Julien Lejeune","Julien Laurent","Christopher","Gilles","Olivier","Kader"]

i.addPlayers(players)

print("players list :", players)
print(i.getPlayers(players))
print(i.getRatingList())
print(i.getPlayer("Joachim"))
print(i.getPlayerRating("Joachim"))


"""
This bunch of data represent the match in the Csv files "MTG-scores" for the period from 28/12/2023 to 03/01/2024
"""
i.recordMatch("Joachim", "Julien Lejeune", winner="Joachim")
i.recordMatch("Joachim", "Christopher", winner="Joachim")
i.recordMatch("Julien Lejeune", "Gilles", winner="Gilles")
i.recordMatch("Joachim", "Gilles", winner="Joachim")
i.recordMatch("Julien Lejeune", "Christopher", winner="Julien Lejeune")
i.recordMatch("Joachim", "Christopher", winner="Christopher")


print(i.getRatingList())
