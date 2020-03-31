class Repo:

    def __init__(self, filename):
        self.__filename = filename
        self.__net = {}
        self.readData()

    def readData(self):
        adj = {}
        with open(self.__filename, 'r') as f:
            N = f.readline()
            mat = [[int(num) for num in line.split(',')] for line in f]
        adj['mat'] = mat
        adj['noNodes'] = int(N)
        self.__net = dict(adj)

    @property
    def net(self):
        return self.__net
