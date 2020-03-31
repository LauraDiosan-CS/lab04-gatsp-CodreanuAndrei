from random import randint

from utils.ParseBerlin import parseberlin


def position(repres, el):
    for i in range(len(repres)):
        if repres[i] == el:
            return i
    return -1


def crosseover(self, c):
    # partially mapped XO
    pos1 = randint(1, self.__problParam['network']['noNodes'] - 1)
    pos2 = randint(1, self.__problParam['network']['noNodes'] - 1)
    newrepres = [None] * self.__problParam['network']['noNodes']
    newrepres[0] = c.__repres[0]
    for i in range(pos1, pos2):
        newrepres[i] = self.__repres[i]
    for i in range(pos1, pos2):
        if c.__repres[i] not in newrepres[pos1:pos2]:
            inloc = self.__repres[i]
            pos = self.position(c, inloc)
            if newrepres[pos] is None:
                newrepres[pos] = c.__repres[i]
            else:
                aux = self.__repres[pos]
                newpos = self.position(c, aux)
                newrepres[newpos] = c.__repres[i]


p1 = [0, 1, 3, 4, 2, 5, 6]
p2 = [0, 4, 5, 6, 2, 1, 3]


def cross(p1, p2):
    pos1 = 2
    pos2 = 7
    newrepres = [None] * len(p1)
    for i in range(pos1, pos2):
        newrepres[i] = p1[i]

    for i in range(pos1, pos2):
        if p2[i] not in newrepres[pos1:pos2]:
            inloc = p1[i]
            pos = position(p2, inloc)
            if newrepres[pos] is None:
                newrepres[pos] = p2[i]
            else:
                aux = p1[pos]
                newpos = position(p2, aux)
                while newrepres[newpos] is not None:
                    aux = p1[newpos]
                    newpos = position(p2, aux)
                newrepres[newpos] = p2[i]

    for i in p2[pos2:] + p2[:pos1]:
        if i not in newrepres:
            for j in range(len(newrepres)):
                if newrepres[j] is None:
                    newrepres[j] = i
                    break
    print(newrepres)


mat = parseberlin("data/berlin52.txt")
for i in range(0, 51):
    print(mat[i])
