#!/usr/local/bin/python3

def testPhrase(phrase):
    wp = []
    for w in phrase.split():
        if w in wp:
            return False
        wp.append(w)
    return True


assert True == testPhrase("aa bb cc dd ee")
assert False == testPhrase("aa bb cc dd aa")
assert True ==  testPhrase("aa bb cc dd aaa")
