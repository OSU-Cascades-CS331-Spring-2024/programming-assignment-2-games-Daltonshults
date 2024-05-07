Dalton Shults
CS 331
Dr. Churchill
6 May 2024

Analysis

1. Simulate four games between yourself and the minimax player on a 4x4 board, with the depth parameter set to 5, 3, 2, and 1 respectively.
    * What were the results of each game?

        The results of the games were: 
        * Minimax
        * Minimax
        * Minimax
        * Minimax

    * Did the minimax player's moves change when the depth was limited to smaller and smaller values?

        Yes, they did change because the depth of the search wasn't as extensive. So, it wasn't able to expand the search tree enough to start to find the optimal locations to make moves. Essentially, it was like setting it to an easy, medium, and hard mode. Granted, I am tired while playing this after programming all day, and my othello skills might not be as sharp as they usually are. However, with it being able to look into future moves, and simulate that the closer it gets to a terminal state in the depth of the search it becomes more accurate. Meaning, the higher the depth is set, the sooner it will be able to evaluate terminal nodes, and get the desired outcome.

    * What was the average time per move for each of the games? Commen on why there is or is not a difference.
        * 0.0073994795481363935
        * 0.0030741214752197264
        * 0.0008989810943603515
        * 0.00047588348388671875

        The difference is because of the depth. When the depth is limited it doesn't search as many actions as it would if it was doing a search until only terminal state nodes. Essentially, by limiting the depth we can limit the amount of time it takes for the algorithm to run. Given certain restraints these limitations might be desirable. 

2. Simulate two games between yourself and the minimax player on an 8x8 board, with the depth parameter set to 5 and 2.
    * What were the results of each game?
        * Minimax
        * Human

    * Did the minimax player's moves change when the depth changed?
        Yes, they were less optimal the less depth it had to search. This is because it isn't able to check as many action's and resulting states from the actions as the depth increases. Limiting the depth can be very beneficial for large search spaces as long as the heuristic is solid. 

    * What was the average time for each of the games? Commend on why there is or is not a difference.
        *  0.17832220395406087
        * 0.008065453891096443
        
        It is the same as the other answer, limiting the depth can limit the search space decreasing the amount of memory required to search, but it also limits the search algorithms ability to find the optimal route as well. Especially as the number of moves that can occur gets larger. It takes longer and longer to compute the moves at a given depth.