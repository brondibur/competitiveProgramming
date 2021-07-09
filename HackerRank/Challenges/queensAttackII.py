# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

# A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.

# The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :

# image

# There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location  in the diagram above prevents the queen from attacking cells , , and :

# image

# Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at . In the board above, there are  such squares.

# Function Description

# Complete the queensAttack function in the editor below.

# queensAttack has the following parameters:
# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

# Returns
# - int: the number of squares the queen can attack

# Input Format

# The first line contains two space-separated integers  and , the length of the board's sides and the number of obstacles.
# The next line contains two space-separated integers  and , the queen's row and column position.
# Each of the next  lines contains two space-separated integers  and , the row and column position of .

# Constraints

# A single cell may contain more than one obstacle.
# There will never be an obstacle at the position where the queen is located.
# Subtasks

# For  of the maximum score:

# For  of the maximum score:

# Sample Input 0

# 4 0
# 4 4
# Sample Output 0

# 9
# Explanation 0

# The queen is standing at position  on a  chessboard with no obstacles:

# image

# Sample Input 1

# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
# Sample Output 1

# 10
# Explanation 1

# The queen is standing at position  on a  chessboard with  obstacles:

# image

# The number of squares she can attack from that position is .

# Sample Input 2

# 1 0
# 1 1
# Sample Output 2

# 0
# Explanation 2

# Since there is only one square, and the queen is on it, the queen can move 0 squares.




import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    ans = 0
    obs = {(b[0],b[1]) for b in obstacles if (abs(r_q - b[0]) == abs(c_q - b[1])) or (b[1] == c_q and b[0] != r_q) or (b[0] == r_q and b[1] != c_q)}
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

    for i in dirs:
        nr, nc = r_q, c_q
        while (nr + i[0] > 0 and nr + i[0] <= n) and (nc + i[1] > 0 and nc + i[1] <= n):
            nr += i[0]
            nc += i[1]
            if (nr, nc) in obs:
                break
            ans += 1
    return ans
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
