def find_union(arr1, arr2):
    union = list(set(arr1 + arr2))
    return union

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
union = find_union(arr1, arr2)
print("Union:", union)
