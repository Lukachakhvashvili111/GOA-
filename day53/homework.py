def calculator():
      num1 = int(input('type a number:'))
      num2 = int(input('type another number:'))
      main = input('type either one + ,- ,* , / :')
      if main == '+':
            print(num1 + num2)
      if main == '-':
            print(num1 - num2)
      if main == '*':
            print(num1 * num2)
      if main == '/':
            print(num1 / num2)


calculator()
