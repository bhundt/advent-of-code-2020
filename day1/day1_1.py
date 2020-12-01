import itertools

file1 = open('input.txt', 'r') 
lines = file1.readlines()

numbers = [int(s.strip()) for s in lines]

for a, b in itertools.product(numbers, repeat=2):
    if a+b == 2020:
        print(a*b)
        break