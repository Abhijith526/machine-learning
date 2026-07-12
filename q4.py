s = input("Enter a string: ")

freq = {}

# Count frequency of each character
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find maximum frequency
max_freq = 0
for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]

# Print character(s) with maximum frequency
for ch in freq:
    if freq[ch] == max_freq:
        print("Character:", ch)
        print("Frequency:", max_freq)