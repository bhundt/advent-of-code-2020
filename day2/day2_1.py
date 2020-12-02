import re

file1 = open('day2/input.txt', 'r') 
lines = file1.readlines()

lines= [s.strip() for s in lines]

num_valid_pw = 0

for line in lines:
    min_chars = int(re.search('(?P<first_digit>\d{1,2})-', line).group('first_digit'))
    max_chars = int(re.search('-(?P<second_digit>\d{1,2})', line).group('second_digit'))
    char = re.search('\s(?P<char>\w):', line).group('char')
    pw = re.search(':\s(?P<pw>\D+)', line).group('pw')
    
    cnt = pw.count(char)
    if cnt >= min_chars and cnt <= max_chars:
        print( 'Valid PW: {} with policy {}-{} {}'.format(pw, min_chars, max_chars, char) )
        num_valid_pw = num_valid_pw + 1

print('Number of valid passwords: %i' % num_valid_pw)