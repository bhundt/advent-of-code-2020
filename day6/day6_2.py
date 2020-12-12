import re
import itertools 

file1 = open('day6/input.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = ''.join(lines)
forms = lines.split("\n\n")
forms = [s.split('\n') for s in forms]

cnt = 0
for form in forms:

    # make sure we have no bogous entries
    for item in form:
        if len(item) == 0:
            form.remove(item)
    
    length = len(form)
    s = ''.join(form)
    s = s.replace('\n', '')
    s_unique = ''.join(set(s))
    for c in s_unique:
        l = s.count(c)
        if l == length:
            cnt = cnt + 1

print("Count: {}".format(cnt))