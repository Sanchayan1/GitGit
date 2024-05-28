def find_second_smallest(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    return arr[1]


arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print("The second smallest number in the array is:", find_second_smallest(arr))
