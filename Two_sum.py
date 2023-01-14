class Solution:
    def twoSum(self, nums, target):
        # declare a variable to hold the result array, initial value will be empty list
        result_array = []

        # iterate through the nums list
        for i in range (len(nums)-1):
            # nest a loop which iterates through the nums list again
            for j in range(len(nums)):
                # block summing the same numebr:
                if i == j:
                    continue
                # check if the sum of nums[i] with any of nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # if it does, add the indexes of the two numebrs in the result array
                    result_array.append(i)
                    result_array.append(j)
                    return result_array
        return result_array

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
print(obj.twoSum([3, 2, 4], 6))
print(obj.twoSum([3, 3], 6))

