def bubble_sort(sort_list):
    for j in range(len(sort_list)):
        for k in range(len(sort_list) - 1):
            if sort_list[k] < sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
    print('\nThe sorted list: \t', sort_list)
    print('\n')


lst = [4,-1,2,-4,-5,3]

bubble_sort(lst)