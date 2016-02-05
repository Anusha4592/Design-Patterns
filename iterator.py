class MyList(list):
    def __iter__(self):
        return Iterator(self) 


class Iterator(object):

    def __init__(self, iterable):
        self.iterable = iterable
        self.len = len(iterable)
        self.idx = 0

    def next(self):
        if self.idx < self.len:
            cur, self.idx = self.idx, self.idx + 1
            return self.iterable[cur]
        else:
            raise StopIteration()

class MyReverseList(list):
    def __iter__(self):
        return ReverseIterator(self)

class ReverseIterator(object):

    def __init__(self, iterable):
        self.iterable = iterable
        self.len = len(iterable)
        self.idx = self.len -1  

    def next(self):
        if self.idx >= 0:
            cur, self.idx = self.idx, self.idx - 1
            return self.iterable[cur]
        else:
            raise StopIteration()


if __name__ == '__main__':
    my_list = MyList([1,2,3])
    for i in my_list:
        print i

    my_rlist = MyReverseList([1,2,3])
    print "Iterate in reverse order.."
    for i in my_rlist:
        print i
