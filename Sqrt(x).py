class Solution:
    def mySqrt(self, x: int) -> int:
        # My solution - since the output numebr should be between 0 and x, we check each number in this
        # range until its square is equal to x.
        for i in range(0, x+1):
            if i * i == x:
                return i
            # If the result number is between two integer numbers, we return the smaller one
            if i * i > x >= (i - 1) * (i - 1):
                return i - 1


    # This solution is found on the Internet, but I find it very smart :)
    #     odd_number = 1
    #     counter = 0
    #
    #     while x > 0:
    #         x = x - odd_number
    #         odd_number += 2
    #         counter += 1
    #
    #     return counter


obj = Solution()
print(obj.mySqrt(5))

