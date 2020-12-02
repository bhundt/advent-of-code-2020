import itertools

file1 = open('input.txt', 'r') 
lines = file1.readlines()

numbers = [int(s.strip()) for s in lines]

for a, b, c in itertools.product(numbers, repeat=3):
    if a+b+c == 2020:
        print(a*b*c)
        break