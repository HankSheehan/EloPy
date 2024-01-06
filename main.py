from elopy import *

i = Implementation()

players = ["Joachim","Julien Lejeune","Julien Laurent","Christopher","Gilles","Olivier","Kader"]

i.addPlayers(players)

print("players list :", players)
print(i.getPlayers(players))
print(i.getRatingList())
print(i.getPlayer("Joachim"))
print(i.getPlayerRating("Joachim"))

i.recordMatch("Joachim", "Julien Lejeune", winner="Joachim")
print(i.getRatingList())
i.recordMatch("Joachim", "Julien Lejeune", winner="Joachim")
print(i.getRatingList())

#
# i.recordMatch("Hank", "Bill", winner="Bill")
#
# print
# i.getRatingList()
#
# i.recordMatch("Hank", "Bill", draw=True)
#
# print
# i.getRatingList()
#
# i.removePlayer("Hank")
#
# print
# i.getRatingList()
