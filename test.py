from elopy import *

i = Implementation()

players = ["Joachim",
           "Julien Lejeune",
           "Julien Laurent",
           "Christopher",
           "Gilles",
           "Olivier",
           "Kader"]

i.addPlayers(players)

print(i)

# print
# i.getPlayerRating("Hank"), i.getPlayerRating("Bill")
#
# i.recordMatch("Hank", "Bill", winner="Hank")
#
# print
# i.getRatingList()
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
