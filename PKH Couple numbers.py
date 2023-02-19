# Write a function that takes as arguments a list and a number.
# The list ordered in ascending fashion and is unique.
# The function should return a tuple containing all couple numbers from the list, which sum up to the number argument.
# "Example: ll = list(my_func([1,2,3,4,5,6,7,8,9], 8), print(ll), [[1,7], [2,6], [3,5]]"
# Keep in mind complexity of algorithms.

def my_func(l, n):
    result = []
    for i in range((len(l) - 1)):
        wanted = n - l[i]
        if wanted in l and wanted != l[i] and wanted <= i:
            result.append([l[i], wanted])
    return tuple(result)


ll = my_func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
print(ll)

