def find_smallest(arr):

    if not arr:

        return None


    smallest = arr[0]

    for num in arr:

        if num < smallest:

            smallest = num


    return smallest if smallest >= 0 else min(arr)
arr=[1,2,3,4]
print(find_smallest(arr))
