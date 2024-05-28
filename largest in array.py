def find_largest(arr):
    if not arr:
        return None
    return max(arr)


arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print("The largest number in the array is:", find_largest(arr))
