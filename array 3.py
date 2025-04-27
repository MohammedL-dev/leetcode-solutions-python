nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

seen = set()
ans = []

for num in nums:
    complement = target - num
    if complement in seen:
        ans = [nums.index(complement), nums.index(num)]
        break
    seen.add(num)
if ans:
    print(f"Values: {ans}")
else:
    print("No pair found.")