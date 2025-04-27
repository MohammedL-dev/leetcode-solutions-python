nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))
Nums = nums
if len(nums) < 2:
    print("Not enough numbers to find a pair.")
else:
    x, a, ans = 0, 0, []
    b = len(nums) - 1
    while a < b:  
        x = nums[a] + nums[b]
        if x > target:
            b -= 1
        elif x < target:
            a += 1
        else:
            ans = [Nums.index(nums[a]), Nums.index(nums[b])]
            break  
    print(ans if ans else "No pair found")