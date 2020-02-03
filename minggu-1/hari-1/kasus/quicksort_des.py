def partition(lst, low, high):
    i = low - 1 #-1
    pivot = lst[high] #ujung atas array
    for j in range(low, high):  #range(0,4) => 0 1 2 3 4 | array=[3 4 6 1 5] | init i=-1
        if lst[j] >= pivot: #jika j lebih besar atau samadengan pivot
            i += 1 #i = 0
            lst[i], lst[j] = lst[j], lst[i] #penukaran nilai variable 
            
            #0 lst[0=j=3] >= 5] X
            #1 lst[1=j=4] >= 5] X
            #2 lst[2=j=6] >= 5] V i = 
            #3 lst[2=j=1] >= 5] X
            #4 lst[2=j=5] >= 5] V

    lst[i + 1], lst[high] = lst[high], lst[i + 1] #penukaran nilai variable /

                #0 lst(array[i+1=0] => 3), lst(array[high=4] => 5) = lst(array[high=4] => 3), lst(array[i+1=0] => 5)
                #1 lst(array[i+1=1] => 3), lst(array[high=4] => 5) = lst(array[high=4] => 3), lst(array[i+1=0] => 5)

    return i + 1

                #0 i=1,j=0 [6, 5]
                #1
                #2
                #3
                #4

def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high) #mencari pivot(=pi)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)
    print(" sort ", lst)

lst = [3,4,6,1,5] #len = 5

low = 0 #menentukan pivot bawah, ujung array
high = len(lst) - 1 #4 menentukan pivot atas, ujung array
quick_sort(lst, low, high)
print("The desc_sorted list: \t", lst)