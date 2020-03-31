from GA.GeneticAlgorithm import GA


def runGA(popsize, nogen, ffitness, mat, start):
    gaParam = {'popSize': popsize, 'noGen': nogen}
    problParam = {'function': ffitness, 'network': mat, 'start': start}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    for g in range(gaParam['noGen']):
        ga.oneGenerationElitism()
        bestChromosome = ga.bestChromosome()
        print(
            'Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromosome.repres) + 'cost = ' + str(
                bestChromosome.fitness))
