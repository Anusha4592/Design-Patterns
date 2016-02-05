class Singleton(object):
    _instance = None

    def __new__(cls):
        if Singleton._instance is None:
            print "Creating Singleton Object"
            Singleton._instance = object.__new__(cls)
            return Singleton._instance 
        else:
            print "Returning existing Singleton Object"
            return Singleton._instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print s1 is s2
