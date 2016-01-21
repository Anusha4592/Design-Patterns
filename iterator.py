class Iterator(object):

    def __init__(self, iterable):
        self.iterable = iterable
        if isinstance(iterable, dict):
            self.iterable = iterable.keys()
        self.len = len(iterable)
        self.idx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.idx < self.len:
            cur, self.idx = self.idx, self.idx + 1
            return self.iterable[cur]
        else:
            raise StopIteration()



# Generator is an example of the iteration pattern

def generate(n):
    for i in range(n):
        yield n


if __name__ == '__main__':

    l = [1,2,3]
    li = Iterator(l)
    for i in li:
        print i

    s = "Hello"
    si = Iterator(s)
    for i in si:
        print i

    d = {3:4, 6:7}
    di = Iterator(d)
    for i in di:
        print i
    #gen = generate(5)
    #for i in gen:
    #    print i

