import sort

lst = []
size = int(input("Masukan panjang list: \t"))

for i in range(size):
    elements = int(input("Masukkan nilai: \t"))
    lst.append(elements)

print(
    "1. Bubble \n2. Insertion \n3. Merge \n4. Quick \n5. Selection"
)
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
