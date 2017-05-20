from elopy import *

i = Implementation()

i.addPlayer("Hank")
i.addPlayer("Bill",rating=900)

print i.getPlayerRating("Hank"), i.getPlayerRating("Bill")

i.recordMatch("Hank","Bill",winner="Hank")

print i.getRatingList()

i.recordMatch("Hank","Bill",winner="Bill")

print i.getRatingList()

i.recordMatch("Hank","Bill",draw=True)

print i.getRatingList()

i.removePlayer("Hank")

print i.getRatingList()