# Method Resolution Order (MRO)
class A:
    print("A")
    num = 4
    
class B(A):
    print("B")
    pass

class C(A):
    print("C")
    num = 5
    
class D(B,C):
    print("D")
    pass

class E:
    print("haha")
    def setup(self):
        print("E")
        pass

class F:
    print("F")

print(D.num)

# Output
# A
# B
# C
# D
# 5

# Karena Python adalah Bahasa PEmrograman Interpreter, maka program dikerjakan secara berurutan
# Semua Class akan dieksekusi
# Kecuali Class yang memiliki objek, onjeknya tidak dieksekusi, namun classnya tetap dieksekusi