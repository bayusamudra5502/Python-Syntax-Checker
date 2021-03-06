from lib.fa.parser import starParser

def star_tester(regex, ans, star):
  result, isBracket = starParser(regex)

  assert result == ans
  assert star == isBracket

def star_negative(regex):
  result = False

  try:
    starParser(regex)
  except:
    result = True
  
  assert result

def test_01():
  star_tester("","", False)
  star_tester("1","1", False)
  star_tester("123","123", False)
  star_tester("(1+2+   3)","(1+2+3)", False)
  star_tester("\\*a", "\\*a", False)

def test_02():
  star_tester("1*", "1", True)
  star_tester("(1+3)*", "(1+3)", True)
  star_tester("(*1+3)*", "(*1+3)", True)
  star_tester("(1*+3+2**)****", "(1*+3+2**)", True)
  star_tester("a *", "a", True)
  star_tester("(A-Z+0-9+\\-)*", "(A-Z+0-9+\\-)", True)


def test_03():
  star_negative(" *")
  star_negative("*(1+2)")
  star_negative(" *(1)*")
  
def test_04():
  star_tester("(\\*a)*", "(\\*a)", True)