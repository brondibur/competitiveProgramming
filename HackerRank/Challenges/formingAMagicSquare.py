# We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

# You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range .

# Example

# $s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# The matrix looks like this:

# 5 3 4
# 1 5 8
# 6 4 2
# We can convert it to the following magic square:

# 8 3 4
# 1 5 9
# 6 7 2
# This took three replacements at a cost of .

# Function Description

# Complete the formingMagicSquare function in the editor below.

# formingMagicSquare has the following parameter(s):

# int s[3][3]: a  array of integers
# Returns

# int: the minimal total cost of converting the input square to a magic square
# Input Format

# Each of the  lines contains three space-separated integers of row .

# Constraints

# Sample Input 0

# 4 9 2
# 3 5 7
# 8 1 5
# Sample Output 0

# 1
# Explanation 0

# If we change the bottom right value, , from  to  at a cost of ,  becomes a magic square at the minimum possible cost.

# Sample Input 1

# 4 8 2
# 4 5 7
# 6 1 6
# Sample Output 1

# 4
# Explanation 1

# Using 0-based indexing, if we make

# -> at a cost of 
# -> at a cost of 
# -> at a cost of ,
# then the total cost will be .

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    ans = []
    b = []
    m = []
    for i in range(1, 10):
        for j in range(1,10):
            if j!= i:
                for k in range(1,10):
                    if k!=i and k!=j:
                        if i + j + k == 15:
                            b.append([i,j,k])
    for i in b:
        for j in b:
            a = [1,2,3,4,5,6,7,8,9]
            for z in i:
                if z in a:
                    a.remove(z)
            if j != i:
                jdup = 0
                for y in j:
                    if y not in a:
                        jdup = 1
                if jdup == 0:
                    for x in j:
                        a.remove(x)
                    for k in b:
                        if k!= i and k!= j:
                            kdup = 0
                            for w in k:
                                if w not in a:
                                    kdup = 1
                            if kdup == 0:
                                if i[0] == 4 and (i[2] == 2 or i[2] == 8):
                                    if j[2] == 6:
                                        if k[1] == 5:
                                            if i[0] + j[0] + k[0] == 15:
                                                m.append([i,k,j])
                                elif i[0] == 6 and (i[2] == 2 or i[2] == 8):
                                    if j[2] == 4:
                                        if k[1] == 5:
                                            if i[0] + j[0] + k[0] == 15:
                                                m.append([i,k,j])
                                elif i[0] == 2 and (i[2] == 4 or i[2] == 6):
                                    if j[2] == 8:
                                        if k[1] == 5:
                                            if i[0] + j[0] + k[0] == 15:
                                                m.append([i,k,j])
                                elif i[0] == 8 and (i[2] == 4 or i[2] == 6):
                                    if j[2] == 2:
                                        if k[1] == 5:
                                            if i[0] + j[0] + k[0] == 15:
                                                m.append([i,k,j])
    for i in m:
        mins = 0
        for j,k in zip(i,s):
            for x,y in zip(j,k):
                if x!=y:
                    mins += abs(x-y)
        ans.append(mins)
    return(min(ans))


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')