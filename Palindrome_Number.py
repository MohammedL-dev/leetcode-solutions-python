def is_palindrome(number):
	if number < 0 or (number!=0 and number%10 == 0):
		return False
	original = number
	reverse = 0
	while number>0:
		last_digit = number % 10
		reverse = 10*reverse + last_digit
		number //= 10
		print(last_digit, reverse, number)
	return original == number

the_number = int(input("give me your number: "))

print(is_palindrome(the_number))









#y=1
#x=0#
#a=z=int(input("give me your number: "))
#while y>0:
#	y = a%10
#	x = x * 10 + y
#	a //= 10
#	print(x, y, a)
#	
#	
#print(x == z)

#print(x//10)
#a = list(input("give me your number: "))
#b = a[::-1]


# can we use this : x(1001) + y(110) ?