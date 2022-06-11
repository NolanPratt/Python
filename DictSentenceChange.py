
# This program takes in two inputs and combines the two to create
# a new sentence using dictionaries for the string manipulation.
# The first input is a single string that is converted into a
# dictionary and must be in the format: "str str   str str   str str   str ...". --
# inputted with a single space dividing the keys and values, followed by a
# triple space to divide the dictionary items.
# The second input is a sentence string, in the format: "str str str ...",
# that will be manipulated using the corresponding words from the initial input.


keys = input()
sentence = input()
splitwords = keys.split('   ')

my_dict = {}
for i in splitwords:
    x = i.split(' ')
    my_dict[x[0]] = x[1]

senlist = sentence.split(' ')
for i in senlist:
    if i in my_dict:
        word = senlist.index(i)
        senlist[word] = my_dict[i]
        # print(senlist)

senformat = ''
for i in senlist:
    if i == senlist[-1]:
        senformat += i
        break
    senformat += i + ' '

print(senformat)