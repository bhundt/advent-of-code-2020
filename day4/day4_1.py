file1 = open('day4/input.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = ''.join(lines)
passports = lines.split("\n\n")

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0

for passport in passports:
    valid_fields = 0
    for required_field in required_fields:
        if required_field in passport:
            valid_fields = valid_fields + 1
        
    if valid_fields == len(required_fields):
        valid_passports = valid_passports + 1

print("Valid Passports: {}".format(valid_passports))