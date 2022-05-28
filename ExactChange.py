import math

total_change = 1337 #int(input())
dollar_count = 0

if total_change <= 0:
    print('No change')

if len(str(total_change)) >= 3:
    dollar_calc = total_change / 100
    dollar_count = math.floor(dollar_calc)

    quarter_calc = ((dollar_calc - dollar_count) * 100) / 25
    quarter_count = math.floor(quarter_calc)

else:
    quarter_calc = total_change / 25
    quarter_count = math.floor(quarter_calc)

dime_calc = ((quarter_calc - quarter_count) * 25) / 10
dime_count = math.floor(dime_calc)

nickel_calc = ((dime_calc - dime_count) * 10) / 5
nickel_count = math.floor(nickel_calc)

penny_calc = ((nickel_calc - nickel_count) * 5) / 1
penny_count = round(penny_calc)

change = [dollar_count, quarter_count, dime_count, nickel_count, penny_count]

if change[0] != 0:
    if change[0] == 1:
        print(change[0], 'Dollar')
    elif change[0] > 1:
        print(change[0], 'Dollars')
if change[1] != 0:
    if change[1] == 1:
        print(change[1], 'Quarter')
    elif change[1] > 1:
        print(change[1], 'Quarters')
if change[2] != 0:
    if change[2] == 1:
        print(change[2], 'Dime')
    elif change[2] > 1:
        print(change[2], 'Dimes')
if change[3] != 0:
    if change[3] == 1:
        print(change[3], 'Nickel')
    elif change[3] > 1:
        print(change[3], 'Nickels')
if change[4] != 0:
    if change[4] == 1:
        print(change[4], 'Penny')
    elif change[4] > 1:
        print(change[4], 'Pennies')