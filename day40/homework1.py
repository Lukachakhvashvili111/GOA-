numbers_list =[]
double_digits =[]
for i in range(10):
      user_numbers = int(input('enter a number'))
      numbers_list.append(user_numbers)
for i in range(len(numbers_list)):
    if numbers_list[i] > 9 and numbers_list[i] < 100:
         double_digits.append(numbers_list[i])
    else:
      continue
    print('double digit numbers : ',double_digits)
    #done ez