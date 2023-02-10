# Given an array containing variables like a = 0b10111011, b = 0b10110001..
# Use a bitmask and the values in the list in order to achieve a result
# where all of the bits in one variable are flipped.
# Be sure to print your answer as a bin() string for each variable in the list

def flip_bits(bits_list):
    for number in bits_list:
        number = bin(number)[2:]
        mask = ''
        for i in range(len(number)):
            mask += '1'
        result = int(number) ^ int(mask)
        print(result)


flip_bits([0b10111011, 0b10110001])
