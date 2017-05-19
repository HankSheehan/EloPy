from elopy import *

i = Implementation()

i.newPlayer("Hank")
i.newPlayer("Bill",900)

print i.getPlayerRating("Hank"), i.getPlayerRating("Bill")

i.addResults("Hank","Bill","Hank")

print i.getPlayerRating("Hank"), i.getPlayerRating("Bill")


