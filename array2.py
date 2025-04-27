nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

if len(nums) < 2:
    print("Not enough numbers to find a pair.")
else:
    x, a, ans, defr = 0, 0, [], 0
    b = len(nums) - 1


for num in nums:
	defr = target - num
	if defr in nums:
		ans = [nums.index(num), nums.index(defr)]
#    while a < b:  # Make sure pointers do not cross
#        x = nums[a] + nums[b]
#        if x > target:
#            b -= 1
#        elif x < target:
#            a += 1
#        else:
#            ans = [a, b]
#            break  # Once found, break out of the loop
ans.sort()
print(ans if ans else "No pair found")