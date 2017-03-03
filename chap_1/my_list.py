# custom list implementation to write your own method 
class MyList:
    def __init__(self, data):
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __delitem__(self, i):
        del self._list[i]

    def __getitem__(self, i):
        return self._list[i]

    def __setitem__(self, i, val):
        return self._list[ii]

    def insert(self, i, val):
        self._list.insert(i, val)

    def append(self, val):
        self.insert(len(self._list), val)

    def __str__(self):
        return ','.join([str(i) for i in self._list])

    def __len__(self):
        return len(self._list)

if __name__=='__main__':
    foo = MyList([1,2,3,4,5])
    foo.append(6)
    print str(foo)