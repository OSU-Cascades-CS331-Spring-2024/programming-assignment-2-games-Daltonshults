#!/bin/bash

for i in {1..5}
do
    python3 game_driver.py minimax minimax >& log$i.txt
done
