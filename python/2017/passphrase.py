#!/usr/local/bin/python3

def testPhrase(phrase):
    wp = []
    for w in phrase.split():
        if w in wp:
            return False
        wp.append(w)
    return True

def testPhraseAnagram(phrase):
    wp = []
    for w in phrase.split():
        s = ''.join(sorted(w))
        if s in wp:
            return False
        wp.append(s)
    return True


assert True == testPhrase("aa bb cc dd ee")
assert False == testPhrase("aa bb cc dd aa")
assert True ==  testPhrase("aa bb cc dd aaa")
assert True == testPhraseAnagram("abcde fghij")
assert False == testPhraseAnagram("abcde fghij edcab")

valid = 0
v2=0
for line in open("phraseinput.txt",'r'):
    if testPhrase(line):
        valid += 1
    if testPhraseAnagram(line):
        v2 += 1

print(valid)
print(v2)        
