import sort

lst = []
while True:
    try:
        size = int(input("Masukan panjang list: \t")) 
        break
    except ValueError:
        print("Masukkan angka Bos!")

for i in range(size):
    while True:
        try:
            print(1+i)
            elements = int(input("Masukkan nilai : \t"))
            lst.append(elements)
            break
        except ValueError:
            print("Masukkan angka bos!")

print(
    "1. Bubble \n2. Insertion \n3. Merge \n4. Quick \n5. Selection"
)
while True:
    try:
        arg = int(input("Pilihan: \t"))
        break
    except ValueError:
        print("Masukkan angka bos!")

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
