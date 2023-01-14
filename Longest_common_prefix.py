class Solution:
    def longestCommonPrefix(self, strs):
        # create a variable to hold the result, the value should be an empty string
        result = ''

        # find the length of the shortest string in the list
        def len_func(n):
            return len(n)

        minLen = min(list(map(len_func, strs)))

        # check the corner cases

        # check if list is empty
        if len(strs) == 0:
            return result
        # check if list has one string
        if len(strs) == 1:
            result = strs[0]
            return result
        # check if there is an empty string in the list
        for word in strs:
            if word != "":
                continue
            else:
                return result
        # check if first letter is different
        for i in range(len(strs) - 1):
            if strs[i][0] == strs[i + 1][0]:
                continue
            else:
                return result

        # create a loop to cover the length of the shortest string
        for x in range(minLen):
            # store the letters you want to check in the result variable
            result += strs[0][x]
            # create a nested loop to iterate through all the strings in the list
            for i in range(len(strs)):
                # compare the first letter of each string
                if strs[i].startswith(result):
                    # if all first letters are the same, compare the second letters, do this untill there is a difference in the letters
                    continue
                # if there is a string that doesn't start with the same letter, return empty string
                else:
                    # if the result string has more than two letters, trim the last one
                    if len(result) > 1:
                        result = result[:len(result) - 1]
                    else:
                        # if the result string has only one letter, don't trim it
                        return result
        return result

obj = Solution()
print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
print(obj.longestCommonPrefix(["dog", "racecar", "car"]))
print(obj.longestCommonPrefix([""]))
print(obj.longestCommonPrefix(["lpower", "lpow"]))
print(obj.longestCommonPrefix([""]))
print(obj.longestCommonPrefix(["", ""]))
print(obj.longestCommonPrefix(["a"]))
print(obj.longestCommonPrefix(["ab", "a"]))
