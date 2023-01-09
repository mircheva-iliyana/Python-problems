#Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0

        while index < len(s):
            if s[index] == 'I':
                if index < len(s)-1 and s[index+1] == "V":
                    result += 4
                    index += 2
                elif index < len(s)-1 and s[index+1] == "X":
                    result += 9
                    index += 2
                else:
                    result += 1
                    index += 1
            elif s[index] == 'V':
                result += 5
                index += 1
            elif s[index] == 'X':
                if index < len(s)-1 and s[index+1] == "L":
                    result += 40
                    index += 2
                elif index < len(s)-1 and s[index+1] == "C":
                    result += 90
                    index += 2
                else:
                    result += 10
                    index += 1
            elif s[index] == 'L':
                result += 50
                index += 1
            elif s[index] == 'C':
                if index < len(s)-1 and s[index+1] == "D":
                    result += 400
                    index += 2
                elif index < len(s)-1 and s[index+1] == "M":
                    result += 900
                    index += 2
                else:
                    result += 100
                    index += 1
            elif s[index] == 'D':
                result += 500
                index += 1
            elif s[index] == 'M':
                result += 1000
                index += 1

        return result

obj = Solution()
print(obj.romanToInt('IXC'))