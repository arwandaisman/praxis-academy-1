#1------------------------------------------------------
def greeting():
    print("Hello World")

greeting()

#2------------------------------------------------------
print()
greeting.lang = 'English'
print(greeting.lang)

#3------------------------------------------------------
print()
def square(a):
    return a*a
b = square(2)
print(b)

#4------------------------------------------------------
print()
def formal():
    print("How are you?")

def casual():
    print("What's up?")

def greet(a):
    if a == "formal":
        formal()
    else:
        casual()

greet('casual')

#5a------------------------------------------------------
print()
list1=[1,2,3]
list2=[]

for i in range(len(list1)):
    list2.append(list1[i] * 2)

print(list2)

#5b------------------------------------------------------
print()
import numpy as np
list1=np.array([1,2,3])
print(list1*2)

#6------------------------------------------------------
print()
list1=np.array([1993,1940,1980,1998,1995])
ages=2020-list1
print(ages)

#7------------------------------------------------------
print()
data = {"people": [
    {"name": "Scott", "age": "24"}, 
    {"name": "Larry", "age": "15"}, 
    {"name": "Tim", "age": "21"}]
}

for p in data['people']:
    print('age: ' + p['age'])

#8------------------------------------------------------
print()
list1=[1,2,3,4,5,6,7,8,9]
print(sum(list1))


#9------------------------------------------------------
print()
list1=['Halo','Hello','BuenosDias','Boom']
list2= []
for i in range(len(list1)):
    list2.append(len(list1[i]))

print(list2)


