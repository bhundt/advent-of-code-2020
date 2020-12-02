import re

file1 = open('day2/input.txt', 'r') 
lines = file1.readlines()

lines= [s.strip() for s in lines]

num_valid_pw = 0

for line in lines:
    min_idx = int(re.search('(?P<first_digit>\d{1,2})-', line).group('first_digit'))
    max_idx = int(re.search('-(?P<second_digit>\d{1,2})', line).group('second_digit'))
    char = re.search('\s(?P<char>\w):', line).group('char')
    pw = re.search(':\s(?P<pw>\D+)', line).group('pw')

    if (pw[min_idx-1] == char and pw[max_idx-1] != char) or (pw[min_idx-1] != char and pw[max_idx-1] == char):
        print( 'Valid PW: {} with policy {}-{} {}'.format(pw, min_idx, max_idx, char) )
        num_valid_pw = num_valid_pw + 1
    

print('Number of valid passwords: %i' % num_valid_pw)