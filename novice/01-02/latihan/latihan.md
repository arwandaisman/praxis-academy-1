# Dasar Pemrograman Python
Sub BAB 
1. Data Structures
2. Modules
3. I/O
4. Errors and Exception

## 1. Data Structures
Struktur data adalah cara untuk __mengorganisir dan menyimpan__ data, dengan itu memudahkan pengguna untuk mengakses dan bekerja secara efektif. 

Beberapa jenis tipe data:
- Abstrak
- Primitive: integers; float; string; boolean
- Non-Primitive: arrays; list; tuples; dictionary; sets; files

### Beberapa cheat Sheets
- + untuk menggabungkan string `x + y`a
- * untuk mengulangi string `x * 2`
- pemotongan string juga bisa dilakukan dengan cara `x[2:]` memotong dengan range `x[0]` memotong dengan mengambil index

### Pengolahan Data Primitive
- `+` untuk menggabungkan string `x + y`
  ```
  x = 'Halo '
  y = 'Kadek!'
  x+y

  # output
  # Halo Kadek!
  ```
- `*` untuk mengulangi string `x * 2`
  ```
  x * 2
  
  # output
  # Halo Halo
  ```
- pemotongan string juga bisa dilakukan dengan cara 
  - `x[2:]` memotong dengan range (index)
    ```
    print(x[2:])
    
    # output
    # lo
    ```
  - `x[0]` memotong dengan mengambil index
    ```
    print(x[2])
    
    # output
    # l
    ```
- membuat huruf kapital awal `x.capitalize('aaa') => Aaa`
- mengecek panjang isi variabel `len(x)`
- mengecek apakah variabel tersebut menyimpan digit atau tidak `x.isdigit()`
- replace string dengan cara `x.replace('Aaa', y)` output `Yyy`
- mencari string, jika sama akan menghasilkan `index dari string` jika tidak ada yang sama akan menghasilkan `-1`
  ```
  str1 = 'aabb'
  str2= 'bb'
  str1.find(str2)
  
  # output
  2
  
  str1 = 'aabc'
  str2= 'bb' 
  str1.find(str2)
  
  #output 
  -1
  ```

### Data Type Conversion
- `type()` untuk mengetahui tipe data
  ```
  x = 'Halo'
  type(x)
  
  #output
  <class 'str'>
  ```
-  untuk mengubah tipe data gunakan fungsi `int(), float(), & str()`

### Non-Primitive Data Structure
__1. Array__

    ```
    import array as arr #lakukan import array
    a = arr.array("I",[1,2,3])
    print(a)
    
    # output 
    # array("I",[1,2,3])
    ```

__2. List__

    ```
        b = [1,2,3]
        print(b)
        print(b[2])

        # output 
        # [1,2,3]
        # 3
     ```
 
  *cheat sheets*
  - mengubah isi list
    ```
    b[1]=10
    print(b)

    # output
    # [1,10,3]
    ```
  - menambah isi list, default dari belakang
    ```
    b.append(12)

    # output
    # [1,10,3,12]
    ```
  - menyisipkan list dengan index `insert(index, value)`
    ```
    b.insert(2,50)

    # output
    # [1,10,50,3,12]
    ```
  - menghapus list, jika ada list yang sama, maka index pertama yang akan terhapus
    ```
    b.remove(12)
    
    # output
    # [1,10,50,3]
    ```
  - menghapus dengan menggunakan index 
    ```
    b.pop(-2)
    
    # output
    # 50
    # [1,10,3]
    ```
  - mengurutkan list (asc) dan reverse
    ```
    b.sort()
    print(b)
    b.reverse()
    print(b)
    b.reverse()
    
    # output
    # [1,3,10]
    # [10,3,1]
    
### Array vs List
Kenapa masih membtuhkan array padahal list sangat mudah digunakan? Perlunya menggunakan array untuk pengolahan data yang bertipe data sama, yang nantinya memudahkan si programmer untuk mengolah data. berikut contoh kode yang tidak bisa dijalankan oleh list

  ```
  import numoy as np
  a=np.array([2,4,6,8])
  print(a/2)
  
  # output
  # [1. 2. 3. 4]
  
  print(np.ones((3,4)))
  
  # output 
  # [[1. 1. 1. 1]
     [1. 1. 1. 1]
     [1. 1. 1. 1]]
  # multi dimensi array
  ```
  
__3. Stack-List__
  - menambah stack
  ```
  stack = [1,2,3,4,5]
  print(stack.append(6))
  # [1,2,3,4,5,6]
  ```
  - menghapus sesuai index, jika `pop()` tanpa parameter, maka akan menghapus list paling terakhir
  ```
  stack.pop(3) 
  # [1,2,3,5,6]
  ```
  - menghitung banyak list yang dicari
  ```
  stack = [1,2,3,3,4,5,3]
  stack.count(3)
  
  # 3
  ```
  - indexing `index(list_yang_dicari, index_mulai)`
  ```
  stack.index(3,4)
  
  # 6
  ```

  - reverse list & sort
  ```
  stack.reverse()
  stack.sort()
  
  #[3,5,4,3,3,2,1]
  #[1,2,3,3,3,4,5]
  ```
  
  - menghapus list
  ```
  del stack[0]
  #[2,3,3,3,4,5]
  
  del stack # untuk menghapus semua list
  ```
  
## 2. Modules
Modul adalah sebuah kumpulan fungsi-fungsi yang dapat dipanggil dan dijadikan sebagai pendukung sistem.
Menggunakan modul sangat mudah, dengan catatan package modul sudah terinstal dahulu. Pemanggilan modul dengan cara menambahakan sintak dibawah pada main program. 

```
# A
import <nama modul>
import sort

# B
from sort import bubble_sort
# sintak diatas digunakan ketika hendak hanya melaukan import terhadap salah satu module

# C
import sort as urut
# atau menjadikannya alias
# jika module berada dalam sub folder tambahkan titik(.) untuk memisahkan direktorinya

import util.sort
```

pemanggilan fungsi dalam modul dengan cara menambahkan sintak dibawah pada main program
```
<nama modul>.<nama fungsi>()
sort.bubble_sort(lst)
```
Modul-modul yang sederhana maupun yang kompleks juga bisa dibuat sendiri oleh programmer.


## 3. I/O

## 4. Errors and Exception
Error and Exception adalh sebuah cara bagaimana pesan error dalam program disampaikan secara informatif terhadap pengguna. Error tersebut bisa diatasi dan bisa saja disembunyikan. Contohnya jika program membutuhkan input angka namun user melakukan input berupa huruf maka Handling Exception akan bekerja disitu

  ```
  while True:
      try:
          size = int(input("Masukan panjang list: \t")) 
          break
      except ValueError:
          print("Masukkan angka Bos!")
  ```
