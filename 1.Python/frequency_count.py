def most_frequent_chars(s):
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
    return 'bla'


s = "blablalknkdùjkjgfgugdhvfhdhfbla"
print(most_frequent_chars(s))