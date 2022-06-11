
# This program takes in a single string of integers, in format: "str str str ...",
# and returns the string without any negative values and sorted in ascending order.


ints = input()
nums = ints.split(' ')

intnums = []
for i in nums:
    i = int(i)
    intnums.append(i)
    #print(intnums)
#print(nums)

intnumspos = []
for i in intnums:
    if i >= 0:
        intnumspos.append(i)
    #print(intnums)
#print(intnums)

sortednums = sorted(intnumspos)
strsortednums = ''
for i in sortednums:
    strsortednums += str(i) + ' '
print(strsortednums, end='')