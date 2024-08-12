all_nums = []
odd = []
even = []
for i in range(10):
      all__nums = int(input('enter a random number of your liking '))
      all_nums.append(all__nums)

for i in range(len(all_nums)):
      if all_nums[i] %2 == 0:
            even.append(all_nums[i])
      else:
            odd.append(all_nums[i])
print('this numbers are even',even)
print('this numbers are odd',odd)    
#diddly di doddley do this is as done is it gets to do