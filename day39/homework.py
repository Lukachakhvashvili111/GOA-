more = []
less = []

for i in range(10):
      input_number = int(input('enter a random number of your liking '))
      if input_number ==100:
            continue
      elif input_number < 100:
            less.append(input_number)
      else:
            more.append(input_number)
print('this numbers that you have wrote are more than a 100',more)
print('the numbers you have wrote are less than a 100',less)
#as done as pushups by nika keshelava