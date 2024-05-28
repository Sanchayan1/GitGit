def maxSubarrayProduct(arr):
    product = 1
    ans = arr[0]
    for i in range(len(arr)):
        product *= arr[i]
        ans = max(ans, product)
        if arr[i] == 0:
            product = 1
    return ans

arr = [1, -2, -3, 0, 7, -8, -2]
print("Maximum Sub array product is", maxSubarrayProduct(arr))
