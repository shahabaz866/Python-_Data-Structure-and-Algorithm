def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    return arr
print(merge_sort([12, 11, 13, 5, 6, 7]))
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort([5, 1, 4, 2, 8]))
