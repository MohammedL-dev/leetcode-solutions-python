x = 'basma'

custom_mapping = {
	'I' : 1,
	'V' : 5,
	'X' : 10,
	'L' : 50,
	'C' : 100,
	'D' : 500,
	'M' : 1000
}

a = input()

s = a[::-1]

custom_numbers = [custom_mapping[char] for char in s]    

num_befor, solution = 0, 0

for num in custom_numbers:
	if num >= num_befor:
		solution += num
	else:
		solution -= num
	num_befor = num
print(solution)
'''
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


M CM XC IV
M = 1000, CM = 900, XC = 90, IV = 4

VICXMCM
adcd....

5
1
100
10
1000
100
1000

5 - 1 + 100 - 10 + 1000 - 100 + 1000
4 + 90 + 900 + 1000
1994

if a < d -> a-b
if a => b -> a+b
'''







