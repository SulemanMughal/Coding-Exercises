# Exercise No. 62


John and Sara friend are playing Rock, Paper, Scissors.

Each game is represented by an array of length 2, where the first element represents what you played and the second element represents what Sara played.

Given a sequence of games, determine who wins the most number of matches. 

-   If they tie, output "Tie".
-   R stands for Rock
-   P stands for Paper
-   S stands for Scissors

    Calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "John"

`Sara wins the first game (Paper beats Rock).`

`John wins the second game (Rock beats Scissors).`

`John wins the third game (Scissors beats Paper).`

`John wins 2/3.`

    calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"
    calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"
