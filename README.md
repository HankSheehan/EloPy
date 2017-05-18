# EloPy

A python library for the Elo Rating System.

# What is the Elo Rating System?
* The Elo Rating System (Elo) is a rating system used for rating players in games. Originally developed for chess by Arpad Elo, Elo has been applied to a large array of games.
* Essentially, each player is assigned a number as a rating. The system predicts the outcome of a match between two players by using an expected score formula (i.e. a player whose rating is 100 points greater than their opponent's is expected to win 64% of the time).
* Everytime a game is played, the Elo rating of the participants change depending on the outcome and the expected outcome. The winner takes points from the loser; the amount is determined by the players' scores and ratings
* https://en.wikipedia.org/wiki/Elo_rating_system

If Player A has a rating of R<sub>A</sub> and Player B a rating of R<sub>B</sub>, the exact formula for Player A's score is:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/51346e1c65f857c0025647173ae48ddac904adcb)

And Player B's score is

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/4b340e7d15e61ee7d90f428dcf7f4b3c049d89ff)
