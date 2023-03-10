# Write a function that takes as arguments a list and a number.
# The list ordered in ascending fashion and is unique.
# The function should return a tuple containing all couple numbers from the list, which sum up to the number argument.
# "Example: ll = list(my_func([1,2,3,4,5,6,7,8,9], 8), print(ll), [[1,7], [2,6], [3,5]]"
# Keep in mind complexity of algorithms.

def my_func(l, n):
    result = []
    left = 0
    right = len(l) - 1
    while left < right:
        sum = l[right] + l[left]
        if sum == n:
            result.append((l[right], l[left]))
            left += 1
            right -= 1
        elif sum < n:
            left += 1
        elif sum > n:
            right -= 1

    return tuple(result)


ll = my_func([10, 20, 30, 40, 50, 60, 70, 80], 15)
print(ll)

