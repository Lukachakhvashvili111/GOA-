def final():
      sum = 0
      nums = [7,3,9,2,10,3,10,10,10]
      final = 0
      for i in range(len(nums)):
            sum = sum + nums[i]
      final = sum / len(nums)
      print('the final average of numbers are:' + str(final))
final()