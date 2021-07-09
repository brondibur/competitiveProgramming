# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# Example



# The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

# Function Description

# Complete the climbingLeaderboard function in the editor below.

# climbingLeaderboard has the following parameter(s):

# int ranked[n]: the leaderboard scores
# int player[m]: the player's scores
# Returns

# int[m]: the player's rank after each new score
# Input Format

# The first line contains an integer , the number of players on the leaderboard.
# The next line contains  space-separated integers , the leaderboard scores in decreasing order.
# The next line contains an integer, , the number games the player plays.
# The last line contains  space-separated integers , the game scores.

# Constraints

#  for 
#  for 
# The existing leaderboard, , is in descending order.
# The player's scores, , are in ascending order.
# Subtask

# For  of the maximum score:

# Sample Input 1

# CopyDownload
# Array: ranked
# 100
# 100
# 50
# 40
# 40
# 20
# 10

 



# Array: player
# 5
# 25
# 50
# 120

 
# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120
# Sample Output 1

# 6
# 4
# 2
# 1
# Explanation 1

# Alice starts playing with  players already on the leaderboard, which looks like this:

# image

# After Alice finishes game , her score is  and her ranking is :

# image

# After Alice finishes game , her score is  and her ranking is :

# image

# After Alice finishes game , her score is  and her ranking is tied with Caroline at :

# image

# After Alice finishes game , her score is  and her ranking is :

# image


# Sample Input 2

# CopyDownload
# Array: ranked
# 100
# 90
# 90
# 80
# 75
# 60

 



# Array: player
# 50
# 65
# 77
# 90
# 102

 
# 6
# 100 90 90 80 75 60
# 5
# 50 65 77 90 102
# Sample Output 2

# 6
# 5
# 4
# 2
# 1


import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here\
    ans = []
    nex = ranked_count - 1
    d = {}
    r = 1
    for j in range(ranked_count):
        if ranked[j] != ranked[j-1] and j!=0:
                r += 1
        d[j] = r
    for i in player:  
        if i >= ranked[0]:
            ans.append(1)
        else:
            j = nex
            while j >= 0:
                if i < ranked[j]:
                    ans.append(d[j]+1)
                    nex = j
                    break
                j -= 1
    return ans



if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
    print('\n')
