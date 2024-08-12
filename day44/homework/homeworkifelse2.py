num = int(input('type a random number and for 3 bucks ill tell you if its odd or even'))
answer1 = input('will you spend 3 bucks for it ? ')
if answer1 == 'yes':
      num1 = int(input('please retype the number that you wrote'))
      if num1 / 2:
            print('this is even')
      elif num1 / 3:
            print('this number is odd')
if answer1 == 'no':
      print('well its your miss not knowing what number is odd and what number is even')