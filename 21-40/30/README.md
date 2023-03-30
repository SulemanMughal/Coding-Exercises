# Exercise No. 30

Given an list of scrabble tiles (as dictionaries), create a function that outputs the maximum possible score a player can achieve by summing up the total number of points for all the tiles in their hand. 

Each hand contains 7 scrabble tiles.


Here's an example hand:

    [ { "tile": "N", "score": 1 },
    { "tile": "K", "score": 5 },
    { "tile": "Z", "score": 10 },
    { "tile": "X", "score": 8 },
    { "tile": "D", "score": 2 },
    { "tile": "A", "score": 1 },
    { "tile": "E", "score": 1 }]

The player's maximum_score from playing all these tiles would be `1 + 5 + 10 + 8 + 2 + 1 + 1`, or `28`.