def minSubArrayLen(target: int, nums: list[int]) -> int:
    nums_length = len(nums)
    start = 0
    end = 0
    sum = 0
    min_len = nums_length + 1
    while end < nums_length:
        sum += nums[end]
        end += 1
        while sum >= target:
            if sum == target:
                min_len = min(min_len, end - start)
            sum -= nums[start]
            start += 1
    return min_len if min_len != nums_length + 1 else 0


# target = 15
# nums = [1, 2, 3, 4, 5]
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(minSubArrayLen(target, nums))
