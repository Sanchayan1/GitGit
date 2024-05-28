def reverse_array(arr):
    if not arr:
        return None
    return arr[::-1]


arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print("The reversed array is:", reverse_array(arr))
