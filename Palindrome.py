class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize a new variable to hold the result string after removing non-alnum chars
        check_string = ''
        # iterate through the input string and take only alnum chars in the result string
        for letter in s:
            if letter.isalnum():
                check_string += letter

        # make all chars in the result string lowercase
        check_string = check_string.lower()
        # reverse the string
        reversed_string = check_string[::-1]

        if check_string == reversed_string:
            return True
        else:
            return False



obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))