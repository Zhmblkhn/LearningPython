nums = [5, 10, 1, 60, 25, 3]
print(nums) # content print

print(len(nums)) # length of list

print(nums[0]) # first element

print(nums[-1]) # last element

print(max(nums)) # maximum element

print(min(nums)) # minimum element

print(sum(nums)) # sum of all elements

# Two variants of printing in revers
# 1
print(nums[: : -1])
# 2
print(list(reversed(nums)))

print(sorted(nums)) # sort in ascending order
print(sorted(nums, reverse=True)) # sort in descending order

nums[1] = 'text' # changing the value of an element
print(nums) # printing changes