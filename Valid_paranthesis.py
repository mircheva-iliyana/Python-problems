class Solution:
    def isValid(self, s):
        opening_brackets = ["(", "[", "{"]
        closing_brackets = [")", "]", "}"]
        checking_list = []

        #iterate through the string
        for i in s:
            # if i is an opening bracket, add it to the checking list
            if i in opening_brackets:
                checking_list.append(i)
            # if i is a closing bracket, check whether the checking list has the same opening bracket
            # and if it was the last opened one and remove it from the checking list
            else:
                index = closing_brackets.index(i)
                if len(checking_list) > 0 and opening_brackets[index] == checking_list[len(checking_list)-1]:
                    checking_list.pop()
                else:
                    return False

        # if checking list is not empty, this means that not every bracket was closed
        if len(checking_list) > 0:
            return False
        else:
            return True




obj = Solution()
print(obj.isValid("]"))
print(obj.isValid("()"))
print(obj.isValid("{[]}"))
print(obj.isValid("()[]{}"))
print(obj.isValid("([)]"))


