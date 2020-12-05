import re

file1 = open('day5/input.txt', 'r') 
lines = file1.readlines()
file1.close()

boardingpasses = [s.strip() for s in lines]
seat_ids = []

# part1
def calc_row_and_column(arg):
    row_binary = re.search(r'(?P<row>(B|F){7})', arg).group('row')
    col_binary = re.search(r'(?P<col>(L|R){3})', arg).group('col')
    
    rows = range(128)
    columns = range(8)
    
    for c in row_binary:
        if c == 'F':
            rows = rows[:len(rows)//2]
        if c == 'B':
            rows = rows[len(rows)//2:]
    
    row = rows[0]

    for c in col_binary:
        if c == 'L':
            columns = columns[:len(columns)//2]
        if c == 'R':
            columns = columns[len(columns)//2:]

    col = columns[0]

    return row, col

def calc_seat_id(row, col):
    return row * 8 + col


for boardingpass in boardingpasses:
    r, c = calc_row_and_column(boardingpass)
    seat_ids.append( calc_seat_id(r, c) )

print('Max. Seat-ID: {}'.format(max(seat_ids)))

# part 2
all_seat_ids = range(1, 851, 1)
empty_seats = list(set(all_seat_ids).difference(seat_ids))
for seat in empty_seats:
    if (seat-1 in seat_ids) and (seat+1 in seat_ids):
        print('My Seat: {}'.format(seat))