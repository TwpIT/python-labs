def spy_game(nums):
    spy_nums = [0, 0, 7]
    for i in nums:
        if len(spy_nums) == 0:
            return True
        if i == spy_nums[0]:
            spy_nums.pop(0)
    if len(spy_nums) == 0:
        return True
    return False  

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))