from lib.fa.parser import concatParser

def concat_tester(regex: str, ans:str):
  res = concatParser(regex)
  assert res == ans

def concat_negative(regex):
  status = False

  try:
    concatParser(regex)
  except:
    status = True
  
  assert status

def test_01():
  concat_tester("",("",))
  concat_tester("(1+3+5)",("(1+3+5)",))
  concat_tester("abc",("a","b","c"))
  concat_tester("a-z",("a-z",))

def test_02():
  concat_tester("(a-z)*",("(a-z)*",))
  concat_tester("ab*",("a","b*"))
  concat_tester("a*b*",("a*","b*"))
  concat_tester("a*    b*",("a*","b*"))
  concat_tester("a(  b+   c+d)*",("a","(b+c+d)*"))

def test_03():
  concat_tester("\\(bc\\+\\)",("\\(","b","c","\\+","\\)"))
  concat_tester("\\((bc)\\+\\)",("\\(","(bc)","\\+","\\)"))

def test_04():
  concat_negative("((a) + b")
  concat_negative("((a) + b))")
  concat_negative("a + b))")

def test_05():
  concat_tester("(A-Z+0-9+\\-)*",("(A-Z+0-9+\\-)*",))
