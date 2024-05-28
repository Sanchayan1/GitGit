def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i, num in enumerate(nums):
        if target - num in buff_dict:
            return [buff_dict[target - num], i]
        buff_dict[num] = i
    return False
nums = [2, 7, 11, 15]

target = 9

print(twoSum(nums, target))

