from GA.RunGA import runGA
from Repo import Repo
from Service import Service
from utils.ParseBerlin import parseberlin
from utils.utils import costofpath


def main():
    # file = input("Introduceti nume fisierului:")
    # pop = input("Introduceti populatia initiala:")
    # gen = input("Introduceti numarul de generatii:")
    file = "mediumF.txt"
    pop = "100"
    gen = "500"
    start = 3

    file = "data/" + file
    r = Repo(file)
    s = Service(r)
    net = parseberlin("data/hardE.txt")
    runGA(int(pop), int(gen), costofpath, s.getNet(), start)


main()
