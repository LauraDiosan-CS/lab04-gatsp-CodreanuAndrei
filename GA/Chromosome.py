from random import randint

from utils.utils import generateARandomPermutation


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['network']['noNodes'], problParam['start'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=None):
        if l is None:
            l = []
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    # def crossover(self, c):
    #     # order XO
    #     pos1 = randint(1, self.__problParam['network']['noNodes'] - 1)
    #     pos2 = randint(2, self.__problParam['network']['noNodes'] - 1)
    #     if pos2 < pos1:
    #         pos1, pos2 = pos2, pos1
    #     k = 0
    #     newrepres = self.__repres[pos1: pos2]
    #     for el in c.__repres[pos2:] + c.__repres[1:pos2]:
    #         if el not in newrepres:
    #             if len(newrepres) < self.__problParam['network']['noNodes'] - pos1:
    #                 newrepres.append(el)
    #             else:
    #                 newrepres.insert(k, el)
    #                 k += 1
    #
    #     newrepres.insert(0, self.__repres[0])
    #     offspring = Chromosome(self.__problParam)
    #     offspring.repres = newrepres
    #     return offspring

    def position(self, repres, el):
        for i in range(len(repres)):
            if repres[i] == el:
                return i
        return -1

    def crossover(self, c):
        # partially mapped XO
        pos1 = randint(1, self.__problParam['network']['noNodes'] - 1)
        pos2 = randint(1, self.__problParam['network']['noNodes'])
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        newrepres = [None] * self.__problParam['network']['noNodes']
        newrepres[0] = c.__repres[0]
        for i in range(pos1, pos2):
            newrepres[i] = self.__repres[i]
        for i in range(pos1, pos2):
            if c.__repres[i] not in newrepres[pos1:pos2]:
                inloc = self.__repres[i]
                pos = self.position(c.__repres, inloc)
                if newrepres[pos] is None:
                    newrepres[pos] = c.__repres[i]
                else:
                    aux = self.__repres[pos]
                    newpos = self.position(c.__repres, aux)
                    while newrepres[newpos] is not None:
                        aux = self.__repres[newpos]
                        newpos = self.position(c.__repres, aux)
                    newrepres[newpos] = c.__repres[i]
        for i in c.__repres[pos2:] + c.__repres[:pos1]:
            if i not in newrepres:
                for j in range(len(newrepres)):
                    if newrepres[j] is None:
                        newrepres[j] = i
                        break
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # mutatie prin inversare
        pos1 = randint(1, self.__problParam['network']['noNodes'] - 1)
        pos2 = randint(1, self.__problParam['network']['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1

        newrepes = self.__repres[pos1:pos2]
        j = len(newrepes) - 1
        for i in range(pos1, pos2):
            self.__repres[i] = newrepes[j]
            j -= 1

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
