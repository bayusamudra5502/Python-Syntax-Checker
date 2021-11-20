from lib.fa.parser import plusParser

def plus_tester(regex, ans):
  res = plusParser(regex)

  assert ans == res

def plus_negative(regex):
  res = False

  try:
    plusParser(regex)
  except:
    res = True
  
  assert res

def test_01():
  plus_tester("",("",))
  plus_tester("1+2+3",("1","2","3"))
  plus_tester("1+( 2+3) +3",("1","(2+3)","3"))
  plus_tester("1 + (2+3)* + 3*",("1","(2+3)*","3*"))

def test_02():
  plus_tester("+1+ 3+ 5*+ (2+ 4*)**", ("","1","3","5*","(2+4*)**"))
  plus_tester("1 + + 4*", ("1", "","4*"))
  plus_tester("1 + (2+3+   ) + +\\ ", ("1", "(2+3+)","", "\\ "))
  plus_tester("1 + \\(2+3+\\) + +\\ ", ("1", "\\(2", "3", "\\)", "", "\\ "))

def test_03():
  plus_negative("((2+)")
  plus_negative("(2+))")
  plus_negative("\\(2+)")

def test_04():
  plus_negative("(2+\\)")