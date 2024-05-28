from collections import Counter

def sort_by_frequency(arr):
    counter = Counter(arr)
    sorted_arr = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    result = []
    for item, freq in sorted_arr:
        result.extend([item] * freq)
    return result

arr = [10, 20, 30, 40, 40, 50, 50, 50]
print("Original array:", arr)
print("Sorted array by frequency:", sort_by_frequency(arr))
