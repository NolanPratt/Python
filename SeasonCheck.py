input_month = input()
input_day = int(input())
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December', 'January', 'February', 'March']
Months31 = [Months[0], Months[2], Months[4], Months[6], Months[7], Months[9], Months[11]]
Months30 = [Months[3], Months[5], Months[4], Months[8], Months[10]]
Months29 = [Months[1]]
Month_Index = 0
Days = list(range(1, 32))
Days31 = list(range(1, 32))
Days30 = list(range(1, 31))
Days29 = list(range(1, 30))

if input_month in Months31 and input_day not in Days31:
    print('Invalid')
    exit()
if input_month in Months30 and input_day not in Days30:
    print('Invalid')
    exit()
if input_month in Months29 and input_day not in Days29:
    print('Invalid')
    exit()


if input_month in Months and input_day in Days:
    Month_Index = Months.index(input_month)

    # Spring check
    if input_month in Months[2:6]:
        # Check if month is March to determine if Spring or Winter
        if input_day >= 20 and input_month == 'March':
            print('Spring')
            exit()
        elif input_day < 20 and input_month == 'March':
            print('Winter')
            exit()
        # Check if month is June to determine if Spring or Summer
        if input_day <= 20 and input_month == 'June':
            print('Spring')
            exit()
        elif input_day > 20 and input_month == 'June':
            print('Summer')
            exit()
        # If neither previous checks were true then it must be Spring
        print('Spring')
        exit()

    # Summer check
    if input_month in Months[5:9]:
        # Check if month is June to determine if Spring or Summer
        if input_day >= 21 and input_month == 'June':
            print('Summer')
            exit()
        elif input_day < 21 and input_month == 'June':
            print('Spring')
            exit()
        # Check if month is September to determine if Summer or Autumn
        if input_day <= 21 and input_month == 'September':
            print('Summer')
            exit()
        elif input_day > 21 and input_month == 'September':
            print('Autumn')
            exit()
        # If neither previous checks were true then it must be Summer
        print('Summer')
        exit()

    # Autumn check
    if input_month in Months[8:11]:
        if input_day >= 22 and input_month == 'September':
            print('Autumn')
        elif input_day < 22 and input_month == 'September':
            print('Summer')
            exit()
        if input_day <= 20 and input_month == 'December':
            print('Autumn')
            exit()
        elif input_day > 20 and input_month == 'December':
            print('Winter')
            exit()
        print('Autumn')

    # Winter check
    if input_month in Months[11:14]:
        if input_day >= 21 and input_month == 'December':
            print('Winter')
            exit()
        elif input_day < 21 and input_month == 'December':
            print('Autumn')
            exit()
        if input_day <= 19 and input_month == 'March':
            print('Winter')
            exit()
        elif input_day > 19 and input_month == 'March':
            print('Spring')
            exit()
        print('Winter')


if input_month not in Months or input_day not in Days:
    print('Invalid')
    exit()