def selection_sort(sort_list):
    for j in range(len(sort_list)):
        smallest_element = max(sort_list[j:])
        index = sort_list.index(smallest_element)
        sort_list[j], sort_list[index] = sort_list[index], sort_list[j]
        print("\nPASS", j, sort_list)
    print('\n\nThe sorted list: \t', sort_list)
    print('\n')

lst = [4,-1,2,-4,-5,3]

selection_sort(lst)