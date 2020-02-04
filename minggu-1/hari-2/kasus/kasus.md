# Kasus
## Module

Pada kasus ini terdapat 2 buah file dengan ekstensi .py. 
1 adalah main program dengan nama 
![index.py](https://github.com/dummytarget/praxis-academy/blob/master/minggu-1/hari-2/kasus/index.py), 
dan modul terletak pada
![sort.py](https://github.com/dummytarget/praxis-academy/blob/master/minggu-1/hari-2/kasus/sort.py). 
Kedua file tersebut berada dalam 1 direktori yaitu kasus.

Di _index.py_ ada pemanggilan module dengan cara
```
import sort
```
yang dimana _index.py_ saat ini sudah saling terhubung. File _sort.py_ hanya berisikan fungsi fungsi.

Pemanggilan fungsi-fungsi tersebut adalah
```
arg = int(input("Pilihan: \t"))
if arg == 1:
    sort.bubble_sort(lst)
elif arg == 2:
    sort.insertion_sort(lst)
elif arg == 3:
    sort.merge_sort(lst)
elif arg == 4:
    sort.quick_sort(lst)
elif arg == 5:
    sort.selection_sort(lst)
else:
    print("Pilihan Tidak ada")

```
pemanggilan fungsi pada modul berada pada sebuah kondisi yang memungkinkan pengguna untuk memilih salah satu metode sortng yang diinginkan

- dimana `sort` adalah module yang sudah diimportkan pada _index.py_
- `bubble_sort` adalah fungsi yang terdapat pada modul _sort.py_
- `(lst)` adalah parameter pada fungsi _bubble_sort_




