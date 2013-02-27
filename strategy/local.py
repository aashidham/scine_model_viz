import strategy


class LocalStrategy(strategy.Strategy):

    name = 'Runs one task after the other, on this machine.'

    def __init__(self):
        super(LocalStrategy, self).__init__()

    def execute(self):
        for t in self._tasks:
            t.go()


if __name__ == '__main__':
    strategy.go(LocalStrategy)
