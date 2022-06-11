
# This program takes in a single string of various words, in the
# format: "str str str ...", and returns the order
# and frequency of each word within the string.


words = input()
splitwords = words.split(' ')

freq = []
for i in splitwords:
    x = splitwords.count(i)
    freq.append(x)
# print(freq)

word = []
for i in splitwords:
    word.append(i)
# print(word)

place = 0
while place < (len(word) or len(freq)):
    print('{} {}'.format(word[place], freq[place]))
    place += 1