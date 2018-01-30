#!/usr/bin/env python3

''' Fast Fibonacci Algorithm with O(log(n)) '''

# In the first line please input how many test cases you would like.
# In the second line please input a, b and n where a = F_0, b = F_1 and the (n + 1)th number in the extended fibonacci sequence.
# r = 10**9 + 7

import sys

global r
r = 10**9 + 7

def matmultiply(A, B):
    if len(A[0]) != len(B):
        return False
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def power(A, n):
    if n == 1:
        return A
    elif n % 2:
        return matmultiply(A, power(A, n - 1))
    else:
        B = power(A, n // 2)
        return matmultiply(B, B)

def fib(n):
    M = [[1,1],[1,0]]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        M = power(M, n - 1)
        return M[0][0] % r

# Main

if __name__ == '__main__':
    for _ in range(int(input())):
        a,b,n = [int(temp) for temp in input().split()]
        if n == 0:
            print(a)
        elif n == 1:
            print(b)
        else:
            print(((a * fib(n - 1)) % r + (b * fib(n)) % r) % r)
