def calculator():
      num1 = int(input('type a number:'))
      num2 = int(input('type another number:'))
      main = input('type either one + ,- ,* , / :')
      if main == '+':
            return(num1 + num2)
      if main == '-':
            return(num1 - num2)
      if main == '*':
            return(num1 * num2)
      if main == '/':
            return(num1 / num2)


print(calculator())