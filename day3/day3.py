file1 = open('day3/input.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = [s.strip() for s in lines]

width = len( lines[0] )
height = len( lines )
lines = ''.join(lines)

advance_right = 3
advance_down = 1
trees = 0

x = 0
y = 0

while y < height:
    if lines[ x + y * width] == '#':
        trees = trees + 1

    x = x + advance_right
    y = y + advance_down

    if x >= width:
        x = x-width

print('Trees: {}'.format(trees))

# Part 2:
# (1, 1): 90
# (3, 1): 278
# (5, 1): 88
# (7, 1): 98
# (1, 2): 45