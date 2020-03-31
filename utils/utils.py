from random import randint


def generateARandomPermutation(n, start):
    perm = [start]
    for i in range(0, n):
        if i != start:
            perm.append(i)
    pos1 = randint(1, n - 1)
    pos2 = randint(1, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


def costofpath(path, param):

    mat = param['mat']
    cost = 0
    for i in range(0, len(path) - 1):
        cost += mat[path[i]][path[i + 1]]
    cost += mat[path[i + 1]][path[0]]
    return cost
