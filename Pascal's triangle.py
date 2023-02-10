class Solution:
    def generate(self, numRows):
        final_list = []

        if numRows == 1:
            final_list.append([1])
            return final_list
        elif numRows == 2:
            final_list.append([1])
            final_list.append([1, 1])
            return final_list
        else:
            final_list.append([1])
            final_list.append([1, 1])
            empty_spaces = 1
            for i in range(2, numRows):
                new_list = [1]
                index = 0
                for j in range(0, empty_spaces):
                    temp_sum = final_list[i - 1][index] + final_list[i - 1][index + 1]
                    new_list.append(temp_sum)
                    index += 1

                new_list.append(1)
                final_list.append(new_list)
                empty_spaces += 1

        return final_list

obj = Solution()
print(obj.generate(1))