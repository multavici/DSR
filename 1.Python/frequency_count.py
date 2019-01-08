def most_frequent_chars(s):
    """ Returns a list of all characters in a string ordered on the frequency of occurence
    """
    frequencies = dict()
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    frequencies_inverted = {}
    for char, freq in frequencies.items():
        if freq in frequencies_inverted:
            frequencies_inverted[freq] += [char]
        else:
            frequencies_inverted[freq] = [char]
    freq_list = list(frequencies_inverted.keys())
    freq_list.sort(reverse=True)
    char_list_ordered = []
    for freq in freq_list:
        char_list_ordered += frequencies_inverted[freq]
    return char_list_ordered


s = "aaabbccccccddr"
print(most_frequent_chars(s))