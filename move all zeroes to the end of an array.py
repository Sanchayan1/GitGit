def move_zeroes_to_end(arr):
    non_zero = []
    zero = []
    for x in arr:
        if x != 0:
            non_zero.append(x)
        else:
            zero.append(x)
    return non_zero + zero

arr = [0, 1, 0, 3, 12, 0, 4, 5, 0, 6]
print("Original array:", arr)
print("Array with zeroes at the end:", move_zeroes_to_end(arr))
