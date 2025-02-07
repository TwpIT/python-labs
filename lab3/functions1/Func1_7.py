def is33in(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    return False


print(is33in([1, 3, 3]))
print(is33in([1, 3, 1, 3]))
print(is33in([3, 1, 3]))