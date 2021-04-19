def compress(nums):
    return [int(nums[i]) + int(nums[i+1]) for i in range(0, len(nums)-1)]
    
def decompress(nums):
    second_num = abs(nums[1] - nums[0])
    first_num = abs(nums[0] - second_num)
    real_nums = [first_num, second_num]
    for i in range(1, len(nums)):
        real_nums.append(abs(nums[i] - real_nums[i]))
        
    return real_nums
    
while True:
    nums = input().split()
    nums2 = compress(nums)
    print(nums2)
    nums3 = decompress(nums2)
    print(nums3)