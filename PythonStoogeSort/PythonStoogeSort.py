import sys

def stooge_sort(arr):
    stooge(arr,0,len(arr)-1)
    return arr

def stooge(arr,i,h):
    if(i >= h):
        return
    if(arr[i] > arr[h]):
        arr[i],arr[h] = arr[h], arr[i]
    if(h-i + 1 > 2):
        t = (int)((h - i + 1) / 3)
        stooge(arr,i,(h-t))
        stooge(arr,i+t,(h))
        stooge(arr,i,(h-t))

lst = [4,5,3,2,4,3,2,1]
print(lst)
print(stooge_sort(lst))



