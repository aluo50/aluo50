def sum67(nums):
  total=0
  x = False
  
  for num in nums:
    if num==6:
      x = True
    elif num==7 and x:
      x = False
    elif not x:
      total += num
      
  return total
