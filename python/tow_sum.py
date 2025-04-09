def two_sum(nums: [int], target: int) -> [int]:
    pre = {}

    for i , n in enumerate(nums):
        diff = target - n
        if diff in pre:
            return [pre[diff], i]
        pre[n] = i

