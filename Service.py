class Service:

    def __init__(self, repo):
        self.__repo = repo

    def getNet(self):
        return self.__repo.net
