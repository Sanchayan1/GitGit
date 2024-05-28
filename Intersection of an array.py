def find_intersection(arr1, arr2):
    intersection = list(set(arr1) & set(arr2))
    return intersection

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
intersection = find_intersection(arr1, arr2)
print("Intersection:", intersection)
