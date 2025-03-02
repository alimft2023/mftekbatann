# design patterns
# 1- creational ==> factory 

class Animal:
    def speak(self):
        pass 

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "meow"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError('error!')

if __name__ =="__main__":
    x=input('enter class name:')
    obj=AnimalFactory.create_animal(x)
    print(obj.speak())
