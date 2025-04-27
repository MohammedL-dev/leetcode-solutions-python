import random


def guess_number():
  try:
    X = x = int(input("chos your range: "))
    num = random.randint(1 , X)
  except ValueError:
    print("invalid input! please enter a number")
    return
  t = 1
  while True:
    try:
      t = t + 1
      guess = int(input("guess a number :"))
      if guess == num:
        print("congratulations! you guessed the number.")
        break
      elif guess < num:
         print("too low, try again.")
      elif guess > num:
         print("too high, try again.")
    except ValueError:
      print("invalid input! please enter a number.")
  y = 0
  while x > 1:
    y += 1
    x = x / 2

  print("your score is: ", (y/t)*1000 )
  print("you take " + str(t) + " times to guess the number")
  if y < t:
    print("learn some math")


guess_number()