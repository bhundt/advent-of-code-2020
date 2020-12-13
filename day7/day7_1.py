import re
import itertools 

file1 = open('day7/input.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = [l.replace('\n', '') for l in lines]
rules = list()

for line in lines:
    bag = dict()
    bag['name'] = re.search(r'(?P<bag>.*)\sbags contain', line).group('bag')
    bag['holds'] = list()

    for match in re.findall(r'\s(?P<num>\d*)\s(?P<type>[\D\s]*)(\sbag|\sbags)', line):
        holds = dict()
        holds['count'] = int(match[0])
        holds['name'] = match[1]

        bag['holds'].append(holds)

    rules.append(bag)

# part 1
possible_bags = list()
def follow1(bag):
    for rule in rules:
        for hold in rule['holds']:
            if bag in hold['name']:
                possible_bags.append(rule['name'])
                follow1(rule['name'])
    return

follow1('shiny gold')
print( len(set(possible_bags)) )

# part2
cnt = 0
def follow2(bag):
    global cnt
    local_cnt = 0
    for rule in rules:
        if bag in rule['name']:
            if len(rule['holds']) == 0:
                local_cnt = local_cnt + 1
            for h in rule['holds']:
                local_cnt = local_cnt + h['count']
                cnt = cnt + h['count'] * follow2(h['name']) + 1
    return local_cnt

follow2('shiny gold')
print(cnt)


