# design patterns  
# 1- creational  ==> singleton

class Singleton:
    _instance = None

    def __new__(cls):  # consrtuctor 
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(s1 is s2)

