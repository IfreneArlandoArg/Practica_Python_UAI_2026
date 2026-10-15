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


