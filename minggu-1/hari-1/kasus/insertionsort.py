def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print('\nThe sorted list: \t', sort_list)
    print('\n')


lst = [4,-1,2,-4,-5,3]

insertion_sort(lst)