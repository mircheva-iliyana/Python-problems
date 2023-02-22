# Write a function that takes as arguments a list and a number.
# The list ordered in ascending fashion and is unique.
# The function should return a tuple containing all couple numbers from the list, which sum up to the number argument.
# "Example: ll = list(my_func([1,2,3,4,5,6,7,8,9], 8), print(ll), [[1,7], [2,6], [3,5]]"
# Keep in mind complexity of algorithms.

def my_func(l, n):
    result = []
    start = l[0]
    end = l[-1]
    for item in l:
        if start <= n - item <= end:
            if n - item != item:  # eliminate adding the same number twice
                if item < n // 2 + 1:  # eliminate repeating couples
                    result.append([item, n - item])
    return tuple(result)


ll = my_func([1, 2, 3, 4, 5, 6, 7, 8, 9], 17)
print(ll)

