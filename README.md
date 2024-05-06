[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.

<h1 align="center">Analysis</h1>

1. Simulate four games between yourself and the minimax player on a 4x4 board, with the depth parameter set to 5, 3, 2, and 1 respectively.
    * What were the results of each game?

        The results of the games were: 
        * Minimax
        * Human
        * Human
        * Human

    * Did the minimax player's moves change when the depth was limited to smaller and smaller values?

        Yes, they did change because the depth of the search wasn't as extensive. So, it wasn't able to expand the search tree enough to start to find the optimal locations to make moves. I honestly think I got lucky when winning, and I found strategies online that our heuristic doesn't consider. I found that if I made moves that resulted in stable pieces the heuristic couldn't really take that into consideration, and instead takes the moves that will result in the best scores. So, I was able to bait the bot into making certain moves.

    * What was the average time per move for each of the games? Commen on why there is or is not a difference.
        * 0.01343071460723877
        * 0.002863788604736328
        * 0.0010637839635213215
        * 0.000513911247253418

        The difference is because of the depth. When the depth is limited it doesn't search as many actions as it would if it was doing a search until only terminal state nodes. Essentially, by limiting the depth we can limit the amount of time it takes for the algorithm to run.

2. Simulate two games between yourself and the minimax player on an 8x8 board, with the depth parameter set to 5 and 2.
    * What were the results of each game?
        * Human
        * Human

    * Did the minimax player's moves change when the depth changed?
        Yes, they were less optimal the less depth it had to search. This is because it isn't able to check as many action's and resulting states from the actions as the depth increases. Limiting the depth can be very beneficial for large search spaces as long as the heuristic is solid. 

    * What was the average time for each of the games? Commend on why there is or is not a difference.
        * 1.9516873113040267
        * 0.008437855490322771

        It is the same as the other answer, limiting the depth can limit the search space decreasing the amount of memory required to search, but it also limits the search algorithms ability to find the optimal route as well. Especially as the number of moves that can occur gets larger. It takes longer and longer to compute the moves at a given depth.