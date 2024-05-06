#!/bin/bash
mkdir -p ./logs

for i in {1..5}
do
    python3 game_driver.py minimax minimax >& ./logs/log$i.txt
done
