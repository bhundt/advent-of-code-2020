import re

file1 = open('day4/input.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = ''.join(lines)              # create one long string
passports = lines.split("\n\n")     # seperate individual passports

def validate_byr(arg):
    try:
        birth_year = int(re.search(r'byr:(?P<year>\d{4})', arg).group('year'))
        if (birth_year >= 1920) and (birth_year <= 2002):
            return True
        else:
            return False
    except:
        return False

def validate_iyr(arg):
    try:
        issue_year = int(re.search(r'iyr:(?P<year>\d{4})', arg).group('year'))
        
        if issue_year >= 2010 and issue_year <= 2020:
            return True
        else:
            return False
    except:
        return False

def validate_eyr(arg):
    try:
        exp_year = int(re.search(r'eyr:(?P<year>\d{4})', arg).group('year'))
        
        if exp_year >= 2020 and exp_year <= 2030:
            return True
        else:
            return False
    except:
        return False

def validate_hgt(arg):
    try:
        m = re.search(r'hgt:(?P<height>\d{2,3})(?P<unit>\D\D)', arg)
        height = int(m.group('height'))
        unit = m.group('unit')
        
        if unit == 'cm' and height >= 150 and height <= 193:
            return True
        elif unit == 'in' and height >= 59 and height <= 76:
            return True
        else:
            return False
    except:
        return False

def validate_hcl(arg):
    try:
        col = re.search(r'hcl:#(?P<color>[0-9a-f]{6})', arg).group('color')
        return True
    except:
        return False

def validate_ecl(arg):
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    try:
        eye_color = re.search(r'ecl:(?P<clr>(amb|blu|brn|gry|grn|hzl|oth))', arg).group('clr')
        
        if eye_color in valid_eye_colors:
            return True
        else:
            return False
    except:
        return False

def validate_pid(arg):
    try:
        pid = re.search(r'pid:(?P<pid>[0-9]{9})\b', arg).group('pid')
        return True
    except:
        return False
    
field_validators = {'byr': validate_byr, 'iyr': validate_iyr, 'eyr':validate_eyr, 'hgt': validate_hgt, 
                    'hcl': validate_hcl, 'ecl': validate_ecl, 'pid': validate_pid}
valid_passports = 0


for passport in passports:
    valid_fields = 0
    for _, (key, val) in enumerate(field_validators.items()):
        if val(passport) == True:
            valid_fields = valid_fields + 1
    
    if valid_fields == len(field_validators):
        valid_passports = valid_passports + 1

print("Valid Passports: {}".format(valid_passports))