class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

p2.name = "Charlie"


def mutiply(x, y):
    return x * y

#print(f"{p1.greet()}.\nThe result of multiplying 5 and 3 is: {mutiply(5, 3)}")
#print(f"{p2.greet()}.\nThe result of multiplying 5 and 3 is: {mutiply(5, 3)}")

# ========== HERENCIA MÚLTIPLE ==========
class C:
    def x(self):
        print({'x': 'C'})

class B:
    def x(self):
        print({'x': 'B'})



class D( C, B):
    pass


# Prueba de herencia múltiple
b = D()
b.x()
print(D.mro())



