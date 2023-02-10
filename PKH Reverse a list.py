# Write a program that reverses a list

def reverse_a_list(n):
    for i in range(0, len(n)//2):
        current = n[i]
        n[i] = n[len(n)-1 - i]
        n[len(n) - 1 - i] = current

    print(n)


reverse_a_list(['a', 'b', 'c'])
