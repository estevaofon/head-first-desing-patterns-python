class singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    s1 = singleton()
    s2 = singleton()
    print(id(s1), id(s2))
    print(s1 is s2)