nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
if len(nums) != 1:
    nums.pop(0) if nums[0] < 0 else 1
    nums.pop(-1) if nums[-1] < 0 else 1
a = 0
b = 1
c = []
x = 1 if len(nums) == 1 else 0
while x != 1:
    nums.pop(0) if len(nums) > 1 and nums[0] < 0 else 0
    nums.pop(-1) if len(nums) > 1 and nums[-1] < 0 else 0
    while b <len(nums):
        num = nums[a] + nums[b]
        c.append(num)
        b += 2
        a += 2
        if b == len(nums):
            break
    nums = c
    a = 0
    b = 0
    c = []
    if len(nums) == 1:
        x = 1
print(''.join(map(str ,nums)))
