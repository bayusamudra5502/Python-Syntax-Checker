from lib.fa.parser import bracketParser

def bracket_tester(regex, ans, bracket):
  result, isBracket = bracketParser(regex)

  assert result == ans
  assert bracket == isBracket

def bracket_negative(regex):
  result = False

  try:
    bracketParser(regex)
  except:
    result = True
  
  assert result

def test_01():
  bracket_tester("123","123", False)
  bracket_tester("","", False)
  bracket_tester("1","1", False)

def test_02():
  bracket_tester("((1) + 3)","(1)+3", True)
  bracket_tester("(1 + 2+3  +5)","1+2+3+5", True)
  bracket_tester("(1 + 2+3  +5+  \\  +12)","1+2+3+5+\\ +12", True)

def test_03():
  bracket_negative("1+2)")
  bracket_negative("(((1)+2)")
  bracket_negative("(   (     1")
  bracket_negative("(1\\)")