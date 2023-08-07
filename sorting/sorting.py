#Quick_sort
def quick_sort(elemens):
    if len(elemens) <=1 :
        return elemens
    pivot = elemens[len(elemens) // 2]
    left = [x for x in elemens if x < pivot]
    middle = [x for x in elemens if x == pivot]
    right = [x for x in elemens if x > pivot]
    
    return quick_sort(left) + middle+ quick_sort(right)



unsorted_list = [45,7,8,9,0,6,7]
sorted_list = quick_sort(unsorted_list)
print (sorted_list)