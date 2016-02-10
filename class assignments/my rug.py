#creating rows of stars
for rows in range(1):
    for pattern in range(15):
        for columns in range(1):
            print('*', end = '')
        for columns in range(1):
            print(' ', end = '')
    print('')
for rows in range(1):
    for pattern in range(15):
        for columns in range(1):
            print(' ', end = '')
        for columns in range(1):
            print('*', end = '')
    print('')

#creating checker boards of stars
for rows in range(2):
    for pattern in range(5):
        for columns in range(3):
            print('*', end = '')
        for columns in range(3):
            print(' ', end = '')
    print('')
for rows in range(2):
    for pattern in range(5):
        for columns in range(3):
            print(' ', end = '')
        for columns in range(3):
            print('*', end = '')
    print('')

#creating diamond of stars
for rows in range(1,6):
    for spaces in range(15 - rows):
        print(' ', end = '')
    for columns in range(rows + (rows-1)):
        print('*', end = '')
    print('')
for rows in range(5,0,-1):
    for spaces in range(15 - rows):
        print(' ', end = '')
    for columns in range(rows + (rows-1)):
        print('*', end = '')
    print('')

#creating diamond pattern of stars
for rows in range(1,4):
    for pattern in range(5):
        for spaces in range(3 - rows):
            print(' ', end = '')
        for columns in range(rows + (rows-1)):
            print('*', end = '')
        for spaces in range(4 - rows):
            print(' ', end = '')
    print('')
for rows in range(2,0,-1):
    for pattern in range(5):
        for spaces in range(3 - rows):
            print(' ', end = '')
        for columns in range(rows + (rows-1)):
            print('*', end = '')
        for spaces in range(4 - rows):
            print(' ', end = '')
    print('')
#creating heart pattern of stars
for rows in range(1,4):
    for pattern in range(5):
        for spaces in range(3 - rows):
            print(' ', end = '')
        for columns in range(rows + (rows-1)):
            print('*', end = '')
        for spaces in range(4 - rows):
            print(' ', end = '')
    print('')
for rows in range(6,0,-1):
    for pattern in range(2):
        for spaces in range(6-rows):
            print(' ', end = '')
        for columns in range(rows + (rows-1)):
            print('*', end = '')
        for spaces in range(7 - rows):
            print(' ', end = '')
    print('')
