class Solution:
    def climbStairs(self, n):
        # declare a variable holding the possible options if starting from the last step
        last = 1
        # declare a variable holding the possible options if starting from last but one step
        lbo = 1
        # declare a variable to hold the temporary step, which will be the sum of the previous two steps
        # starting from the back
        temp = lbo

        # iterating n -2 times (because we know the options for the last two steps),
        # we determine the options for each previous step and it will be the sum of its next two steps
        for i in range(n-1):
            temp = lbo + last
            last = lbo
            lbo = temp

        return temp

obj = Solution()
print(obj.climbStairs(1))
print(obj.climbStairs(2))
print(obj.climbStairs(3))
print(obj.climbStairs(4))
print(obj.climbStairs(5))
print(obj.climbStairs(6))
print(obj.climbStairs(7))
print(obj.climbStairs(8))
print(obj.climbStairs(9))



