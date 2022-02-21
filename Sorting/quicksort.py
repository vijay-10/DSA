def quick_sort(arr,first,last):
    if(first<last):
        pivot=first
        i=first
        j=last
        print(*arr)
        while(i<j):
            while(arr[i]<=arr[pivot] and i<last):
                i=i+1
            while(arr[j]>arr[pivot]):
                j=j-1
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
        arr[pivot],arr[j]=arr[j],arr[pivot]
        quick_sort(arr,first,j-1)
        quick_sort(arr,j+1,last)
    return arr

arr = list(map(int, input("Enter the elements of array: ").split()))
n = len(arr)
print("Unsorted array: ", arr)
print("Sorted array: ", quick_sort(arr,0,n-1))
