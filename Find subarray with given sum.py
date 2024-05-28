def find_subarray(arr, target_sum):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target_sum and start < end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return start, end
    return -1, -1

arr = [15, 2, 4, 8, 5, 10, 23]
target_sum = 21
start, end = find_subarray(arr, target_sum)
if start != -1 and end != -1:
    print(f"Sum found between indexes {start} and {end}")
else:
    print("No subarray found")
