def more_less():
      num1 = int(input('type a random number : '))
      num2 = int(input('type another random number : '))
      if num1 < num2:
            return(num1 + ' is more than ' + num2)
      else:
            return(num2 + ' is more than ' + num1)


print(more_less())