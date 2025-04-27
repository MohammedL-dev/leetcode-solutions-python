binary_list = []
win = 0
while True:
    user_input = input()
    if user_input == "":
        break
    elif user_input in ['0', '1']:
        binary_list.append(int(user_input))
for num in binary_list:
	win += num
lost = len(binary_list) - win
print(win, lost)