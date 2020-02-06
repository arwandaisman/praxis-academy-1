# super()
class A:
    print("A")
    def truth(self):
        return 'Angka Genap'
    
class B(A):
    print("B")
    pass

class C(A):
    print("C")
    def truth(self):
        return 'Angka Ganjil'

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d = D()
print(d.truth(9))


