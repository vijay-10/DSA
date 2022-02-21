def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    first = merge_sort(arr[0:mid])
    second = merge_sort(arr[mid:len(arr)])
    return merge(first, second)

def merge(first, second):
    i = j = k = 0
    mix = []
    while (i < len(first) and j < len(second)):
        if first[i] < second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1
        k += 1
    while (i < len(first)):
        mix.append(first[i])
        i += 1
    while (j < len(second)):
        mix.append(second[j])
        j += 1
    return mix

# arr = [7, 4, 2, 9, 6, 5, 11, 67]
# print(merge_sort(arr))


def merge_sort_inplace(arr, start, end):
    if end - start == 1:
        return
    mid = (start + end)//2
    merge_sort_inplace(arr, start, mid)
    merge_sort_inplace(arr, mid, end)
    merge_inplace(arr, start, mid, end)

def merge_inplace(arr, start, mid, end):
    i = start
    j = mid
    k = 0
    mix = []
    while (i < mid and j < end):
        if arr[i] < arr[j]:
            mix.append(arr[i])
            i += 1
        else:
            mix.append(arr[j])
            j += 1
        k += 1
    while (i < mid):
        mix.append(arr[i])
        i += 1
    while (j < end):
        mix.append(arr[j])
        j += 1
    for i in range(len(mix)):
        arr[start + i] = mix[i]

arr = [7, 4, 2, 9, 6, 5, 11, 67]
merge_sort_inplace(arr, 0, len(arr))
print(arr)
