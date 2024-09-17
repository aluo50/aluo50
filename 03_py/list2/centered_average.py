def centered_average(nums):
  tot = sum(nums) - min(nums) - max(nums)
  return tot/(len(nums)-2)

