def equilibrium_index(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i, num in enumerate(arr):
        right_sum -= num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1

arr = [1, 3, 5, 6, 2, 4]
print("Equilibrium index is", equilibrium_index(arr))
