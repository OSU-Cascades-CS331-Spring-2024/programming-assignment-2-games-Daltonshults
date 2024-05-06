#!/bin/bash

# Useful for running multiple games in a row. 
# This script runs 5 games of minimax vs minimax and saves the logs to the logs directory.
mkdir -p ./logs

for i in {1..5}
do
    python3 game_driver.py minimax minimax >& ./logs/log$i.txt
done
