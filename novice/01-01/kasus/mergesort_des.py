def merge_sort(sort_list):
    print("splitting", sort_list)
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
            if leftHalf[i] > rightHalf[j]:
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
    print("merging...", sort_list)


lst = [4,-1,2,-4,-5,3]

merge_sort(lst)