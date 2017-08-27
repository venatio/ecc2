#! /bin/bash

# usage = ./live.sh 1 10
cd live_games

#for i in *.pgn
# grr... copy 1, 10, 2 etc !

for ((i=0;i<$2;i++))
do
 cp "$i.pgn" ../games/live.pgn
 #echo "-> $i.pgn & sleeping $1 sec."
 sleep $1
done
