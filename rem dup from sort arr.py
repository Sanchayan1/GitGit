def remove_duplicates(arr):
    if not arr:
        return []

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])

    return result
arr=[1,2,2,3,3,3,4]
print(remove_duplicates(arr))
