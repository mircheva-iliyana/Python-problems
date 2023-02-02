class Solution:
    def plusOne(self, digits):
        counter = 0
        # Checking input numbers not ending in 9
        if (digits[len(digits)-1] + 1) < 9:
            digits[len(digits)-1] += 1
        # Checking input = 9
        elif len(digits) == 1 and digits[0] == 9:
            digits.pop()
            digits.append(1)
            digits.append(0)
        # Checking numbers ending in 9
        else:
            while (len(digits) > 0 and digits[len(digits)-1]) == 9:
                counter += 1
                digits.pop()
            if len(digits) == 0:
                digits.append(1)
            else:
                digits[len(digits)-1] += 1
            for i in range(0, counter):
                digits.append(0)
        return digits


obj = Solution()
print(obj.plusOne([9, 9]))
