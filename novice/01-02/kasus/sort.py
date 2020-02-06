#bubble
def bubble_sort(sort_list):
    for j in range(len(sort_list)):
        for k in range(len(sort_list) - 1):
            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
    print('\nThe Bubble sorted list: \t', sort_list)
    print('\n')

#insertion
def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print('\nThe Insertion sorted list: \t', sort_list)
    print('\n')

#merge
def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        leftHalf = sort_list[:mid]
        rightHalf = sort_list[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                sort_list[k] = leftHalf[i]
                i = i + 1
            else:
                sort_list[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            sort_list[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            sort_list[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    
    print('\nThe Merge sorted list: \t', sort_list)

#quick
def quick_sort(lst):
    def partition(lst, low, high):
        i = low - 1 
        pivot = lst[high]
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    def quick(lst, low, high):
        if low < high:
            pi = partition(lst, low, high)
            quick(lst, low, pi - 1)
            quick(lst, pi + 1, high)
    low = 0
    high = len(lst) -1
    quick(lst,low,high)
    print('\nThe Quick sorted list: \t', lst)

#selection
def selection_sort(sort_list):
    for j in range(len(sort_list)):
        smallest_element = min(sort_list[j:])
        index = sort_list.index(smallest_element)
        sort_list[j], sort_list[index] = sort_list[index], sort_list[j]
    print('\n\nThe Selection sorted list: \t', sort_list)
    print('\n')
