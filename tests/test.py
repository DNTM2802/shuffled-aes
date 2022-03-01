import hashlib
from pprint import pprint
from random_round import random_round, shuffle_array, random_number
import sys

permutations = [
    (0,1,2,3),
    (0,1,3,2),
    (0,2,1,3),
    (0,2,3,1),
    (0,3,2,1),
    (0,3,1,2),
    (1,0,2,3),
    (1,0,3,2),
    (1,2,0,3),
    (1,2,3,0),
    (1,3,2,0),
    (1,3,0,2),
    (2,1,0,3),
    (2,1,3,0),
    (2,0,1,3),
    (2,0,3,1),
    (2,3,0,1),
    (2,3,1,0),
    (3,1,2,0),
    (3,1,0,2),
    (3,2,1,0),
    (3,2,0,1),
    (3,0,2,1),
    (3,0,1,2),
]
def print_16_block(array):
    for i in range(4):
        for j in range(4):
            print(array[j][i], end=" ")
        print()

def shift_rows_suffled(matrix):
    index = int(random_big_number % len(permutations))
    perm = permutations[index]

    matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0] = matrix[(perm[0]) % 4][0], matrix[(perm[0] + 1) % 4][0], matrix[(perm[0] + 2) % 4][0], matrix[(perm[0] + 3) % 4][0]
    matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1] = matrix[(perm[1]) % 4][1], matrix[(perm[1] + 1) % 4][1], matrix[(perm[1] + 2) % 4][1], matrix[(perm[1] + 3) % 4][1]
    matrix[0][2], matrix[1][2], matrix[2][2], matrix[3][2] = matrix[(perm[2]) % 4][2], matrix[(perm[2] + 1) % 4][2], matrix[(perm[2] + 2) % 4][2], matrix[(perm[2] + 3) % 4][2]
    matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3] = matrix[(perm[3]) % 4][3], matrix[(perm[3] + 1) % 4][3], matrix[(perm[3] + 2) % 4][3], matrix[(perm[3] + 3) % 4][3]
    


def inv_shift_rows_shuffled(matrix):
    index = int(random_big_number % len(permutations))
    perm = permutations[index]

    matrix[(perm[0]) % 4][0], matrix[(perm[0] + 1) % 4][0], matrix[(perm[0] + 2) % 4][0], matrix[(perm[0] + 3) % 4][0] = matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0]
    matrix[(perm[1]) % 4][1], matrix[(perm[1] + 1) % 4][1], matrix[(perm[1] + 2) % 4][1], matrix[(perm[1] + 3) % 4][1] = matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1]
    matrix[(perm[2]) % 4][2], matrix[(perm[2] + 1) % 4][2], matrix[(perm[2] + 2) % 4][2], matrix[(perm[2] + 3) % 4][2] = matrix[0][2], matrix[1][2], matrix[2][2], matrix[3][2]
    matrix[(perm[3]) % 4][3], matrix[(perm[3] + 1) % 4][3], matrix[(perm[3] + 2) % 4][3], matrix[(perm[3] + 3) % 4][3] = matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3]


# def mix_columns_shuffle(matrix):
#     offset = int(random_big_number % 4)
#     for i in range(4):
#         t = matrix[i][0] ^ matrix[i][1] ^ matrix[i][2] ^ matrix[i][3]
#         u = matrix[i][0]
#         matrix[i][0] ^= t ^ xtime(matrix[i][0] ^ matrix[i][1])
#         matrix[i][1] ^= t ^ xtime(matrix[i][1] ^ matrix[i][2])
#         matrix[i][2] ^= t ^ xtime(matrix[i][2] ^ matrix[i][3])
#         matrix[i][3] ^= t ^ xtime(matrix[i][3] ^ u)

# def inv_mix_columns_shuffle(matrix):
#     offset = int(random_big_number % 4)
#     for i in range(4):
#         u = xtime(xtime(matrix[i][0] ^ matrix[i][2]))
#         v = xtime(xtime(matrix[i][1] ^ matrix[i][3]))
#         matrix[i][0] ^= u
#         matrix[i][1] ^= v
#         matrix[i][2] ^= u
#         matrix[i][3] ^= v
#     mix_columns_shuffle(matrix)

from copy import copy

def galoisMult(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256


def mixColumnsS(matrix):
    offset = int(random_big_number % 4)
    columns = []
    for i in range(4):
        column = matrix[i]
        temp = copy(column)
        column[0] = galoisMult(temp[0],2) ^ galoisMult(temp[3],1) ^ galoisMult(temp[2],1) ^ galoisMult(temp[1],3)
        column[1] = galoisMult(temp[1],2) ^ galoisMult(temp[0],1) ^ galoisMult(temp[3],1) ^ galoisMult(temp[2],3)
        column[2] = galoisMult(temp[2],2) ^ galoisMult(temp[1],1) ^ galoisMult(temp[0],1) ^ galoisMult(temp[3],3)
        column[3] = galoisMult(temp[3],2) ^ galoisMult(temp[2],1) ^ galoisMult(temp[1],1) ^ galoisMult(temp[0],3)
        columns.append(column)
    print(columns)
    for index,column in enumerate(columns):
        matrix[(index+offset) % 4] = column

def mixColumnsSInv(matrix):
    offset = int(random_big_number % 4)
    columns = []
    for i in range(4):
        column = matrix[i]
        temp = copy(column)
        column[0] = galoisMult(temp[0],14) ^ galoisMult(temp[3],9) ^ galoisMult(temp[2],13) ^ galoisMult(temp[1],11)
        column[1] = galoisMult(temp[1],14) ^ galoisMult(temp[0],9) ^ galoisMult(temp[3],13) ^ galoisMult(temp[2],11)
        column[2] = galoisMult(temp[2],14) ^ galoisMult(temp[1],9) ^ galoisMult(temp[0],13) ^ galoisMult(temp[3],11)
        column[3] = galoisMult(temp[3],14) ^ galoisMult(temp[2],9) ^ galoisMult(temp[1],13) ^ galoisMult(temp[0],11)
        columns.append(column)
    
    for index,column in enumerate(columns):
        matrix[(index+(offset if offset == 2 or offset == 0 else offset - 2)) % 4] = column

# def mixColumns(matrix):
#     offset = int(random_big_number % 4)
#     for i in range(4):
#         column = matrix[i]
#         temp = copy(column)
#         column[0] = galoisMult(temp[(0 + offset) % 4],2) ^ galoisMult(temp[(3 + offset) % 4],1) ^ galoisMult(temp[(2 + offset) % 4],1) ^ galoisMult(temp[(1 + offset) % 4],3)
#         column[1] = galoisMult(temp[(1 + offset) % 4],2) ^ galoisMult(temp[(0 + offset) % 4],1) ^ galoisMult(temp[(3 + offset) % 4],1) ^ galoisMult(temp[(2 + offset) % 4],3)
#         column[2] = galoisMult(temp[(2 + offset) % 4],2) ^ galoisMult(temp[(1 + offset) % 4],1) ^ galoisMult(temp[(0 + offset) % 4],1) ^ galoisMult(temp[(3 + offset) % 4],3)
#         column[3] = galoisMult(temp[(3 + offset) % 4],2) ^ galoisMult(temp[(2 + offset) % 4],1) ^ galoisMult(temp[(1 + offset) % 4],1) ^ galoisMult(temp[(0 + offset) % 4],3)
#         matrix[i] = column

# def mixColumnsInv(matrix):
#     offset = int(random_big_number % 4)
#     for i in range(4):
#         column = matrix[i]
#         temp = copy(column)
#         column[0] = galoisMult(temp[(0 + offset) % 4],14) ^ galoisMult(temp[(3 + offset) % 4],9) ^ galoisMult(temp[(2 + offset) % 4],13) ^ galoisMult(temp[(1 + offset) % 4],11)
#         column[1] = galoisMult(temp[(1 + offset) % 4],14) ^ galoisMult(temp[(0 + offset) % 4],9) ^ galoisMult(temp[(3 + offset) % 4],13) ^ galoisMult(temp[(2 + offset) % 4],11)
#         column[2] = galoisMult(temp[(2 + offset) % 4],14) ^ galoisMult(temp[(1 + offset) % 4],9) ^ galoisMult(temp[(0 + offset) % 4],13) ^ galoisMult(temp[(3 + offset) % 4],11)
#         column[3] = galoisMult(temp[(3 + offset) % 4],14) ^ galoisMult(temp[(2 + offset) % 4],9) ^ galoisMult(temp[(1 + offset) % 4],13) ^ galoisMult(temp[(0 + offset) % 4],11)
#         matrix[i] = column

def xtime(b):
    return (((b << 1) ^ 0x1B) & 0xFF) if (b & 0x80) else (b << 1)

plain = sys.stdin.read()
skey = hashlib.md5(bytes(plain, encoding='utf8')).digest()

# Get random round
random_r = random_round(skey)

# Get a big number dependent of the skey
random_big_number = random_number(skey)

matrix = [[176, 220, 136, 110], [141, 26, 24, 187], [218, 163, 132, 102], [246, 105, 114, 230]]
print(f'offset -> {int(random_big_number % 4)}')
print_16_block(matrix)
print()
#mix_columns_shuffle(matrix)
mixColumnsS(matrix)
print_16_block(matrix)
print()
#inv_mix_columns_shuffle(matrix)
mixColumnsSInv(matrix)
print_16_block(matrix)