
# This program takes in a single string of integers, in the
# format: "str str str ...", and returns the average and
# maximum value of the string.


nums = input()
splitnums = nums.split(' ')
num = 0
place = 0
formatnums = splitnums.copy()
for i in splitnums:
    num += int(i)
    formatnums[place] = int(i)
    place += 1
print('{} {}'.format(int(num / len(splitnums)), max(formatnums)))