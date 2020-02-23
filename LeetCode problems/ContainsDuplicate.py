#https://leetcode.com/problems/contains-duplicate/

# Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Input: [1,2,3,4]
# Output: false

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


# sol 1:
	
def containsDuplicate(nums):
      return len(nums) > len(set(nums))

# sol 2:

def containsDuplicate(nums):
	if len(nums)==0:
		return False
	if(collection.Counter(nums).most_common(1)[0][0] > 1):
		return True
	else:
		return False

#sol 3:

def containsDuplicate(nums):
	s = list(set(nums))
	for item in s:
		if nums.count(item) > 1:
			return True
		else: 
			continue
	return False

