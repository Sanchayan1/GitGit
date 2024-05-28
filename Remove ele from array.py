def remove_element(arr, target):

    result = []

    for num in arr:

        if num != target:

            result.append(num)


    return result
arr=[1,2,3,4,8,9]
target=8
print(remove_element(arr, target))
