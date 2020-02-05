# OOP dan Pustaka Standar
## Materi
Sub Materi
1. OOP (Object Oriented Programming) & Classes
2. CRC Card (Class Responsibility Collaboration)
3. Python Standar library (Pustaka Standar)

    Materi    
## 1. OOP & Classes
Adalah pemrograman yang berbasis objek yang saling berinteraksi. Berisikan data dalam bentuk atribut atau properti, serta kode dalam bentuk methods.
OOP sangan identik dengan _Objects_ dan _Classes_.

  1. Classes : sekumpulan objek
  2. Methods   : perintah perintah yang ada pada objek

_Analogy_
```  
  Class Buah:
    Objek Pear:
        methodsKupasPear:
        methodsAmbilPear:
    
    Objek Duren:
        methodsKupasDuren:
        methodsAmbilDuren:
    
   -------------------------
   class Person:        # class
    def say_hi(self):   # objek, self adalah parameter yang sudah diatur oleh python
        print('Hello, how are you?') # methods
        
   p = Person()
   p.say_hi() # dan parameter self tidak perlu diberikann argumen
   
   # output
   # Hello, how are you?

```
  3. The `__init__` method 
      ```
      class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say_hi(self):
            print('Hello, my name is', self.name, '. My age is', self.age)

      p = Person('Kadek', 12)
      p.say_hi()
      
      # output
      # Hello, my name is Kadek. My age is 12
      ```
  
  4. Class and Object Variables
  
  5. Inheritance

## 2. CRC Card
Adalah sebuah kumpulan _tugas_ yang akan dikerjakan oleh _class_, dan juga terlihat _class_ tersebut berelasi dengan _class_ lain.
Terdapat 3 bagian :
  - Class Name (nama _class_)
  - Responsibilities (_tugas_)
  - Collaborators (_relasi_)
  
<table>
  <tr>
    <td colspan="2">Class Name</td>
  </tr>
  <tr>
    <td>Responsibilities</td>
    <td>Collaborators</td>
  </tr>
</table>

Untuk membuat CRC Card, tahapan awal yang dilakukan adalah membuat sebuah skenario untuk mengidentifikasi aktor utama dan tugas yang harus
dia lakukan. Jika tugas dari aktor-aktor sudah dibuat, relasikan aktor tersebut dengan siapa saja nantinya mereka berinteraksi.


## 3. Python Standar Library

