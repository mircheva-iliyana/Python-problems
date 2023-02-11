# Given an array containing variables like a = 0b10111011, b = 0b10110001..
# Use a bitmask and the values in the list in order to achieve a result
# where all of the bits in one variable are flipped.
# Be sure to print your answer as a bin() string for each variable in the list

def flip_bits(bits_list):
    for i in range(len(bits_list)):
        # the mask should be as long as the current number without the first two symbols
        mask = (1 << (len(bin(bits_list[i])) - 2)) - 1
        bits_list[i] = bits_list[i] ^ mask
        print(bin(bits_list[i]))


flip_bits([0b10111011, 0b10110001])
