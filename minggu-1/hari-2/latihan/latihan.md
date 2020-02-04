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
1. Array
    ```
    #A
    import array as arr #lakukan import array
    a = arr.array("I",[1,2,3])
    print(a)
    
    # output 
    # array("I",[1,2,3])

2. List 
```
    b = [1,2,3]
    print(b)
    print(b[2])
    
    # output 
    # [1,2,3]
    # 3
 ```
*cheat sheets*
- b.append(11)

## 2. Modules

## 3. I/O

## 4. Errors and Exception
