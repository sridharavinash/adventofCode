import re

def part1(rules=False):
  optional_fields = ['cid']
  expected_fields=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  expected_fields = sorted(expected_fields)
  parsed_passport={}
  passports = []
  for l in open("input.txt"):
    if l == "\n":
      passports.append(parsed_passport)
      parsed_passport = {}
    line = l.strip()
    splits = line.split()
    for val in splits:
      k,v = val.split(':')
      if k in optional_fields:
        #skip optional fields
        continue
      if rules:
        match_h = re.fullmatch("^(\d+)(in|cm)$", v)
        if k == 'byr' and (1920 <= int(v) <= 2002):
          parsed_passport[k] = v
        if k == 'iyr' and (2010 <= int(v) <= 2020):
          parsed_passport[k] = v
        if k == 'eyr' and (2020 <= int(v) <= 2030):
          parsed_passport[k] = v
        if k == 'hgt' and match_h :
          h = int(match_h.groups()[0])
          ut = match_h.groups()[1]
          if ut == 'cm' and ( 150 <= h <= 193):
            parsed_passport[k] = v
          if ut == 'in' and (59 <= h <= 76):
            parsed_passport[k] = v
        if k == 'hcl' and len(v) == 7 and re.fullmatch('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v):
          parsed_passport[k] = v
        if k == 'ecl' and v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(v) == 3:
          parsed_passport[k] = v
        if k == 'pid' and re.fullmatch('^\d{9}$', v):
          parsed_passport[k] = v
      else:
        parsed_passport[k] = v

  
  #get the last one passport
  passports.append(parsed_passport)
  
  valid = 0
  #print(len(passports))
  for p in passports:
    if sorted(list(p.keys())) == expected_fields: 
      #print(sorted(list(p.keys())))
      #print(expected_fields)
      #print(sorted(p.items()))
      #print(p['hgt'])
      valid += 1

  return valid

if __name__ == "__main__":
  print(f"part1 valid: {part1()}")
  print(f'part2 valid: {part1(rules=True)}')