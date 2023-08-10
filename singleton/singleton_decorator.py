def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    pass


# Uso:
obj1 = Singleton()
obj2 = Singleton()
assert obj1 is obj2  # Isso será Verdadeiro
print(obj1 is obj2)
