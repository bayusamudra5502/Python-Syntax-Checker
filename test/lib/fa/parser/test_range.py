from lib.fa.parser import rangeParser

def tes(regex, ans, rule):
  hasil, changed = rangeParser(regex)
  assert hasil == ans
  assert rule  == changed

def test_satu():
  tes("abc","abc", False)
  tes("x","x", False)

def test_dua():
  tes("1-9","\\1+\\2+\\3+\\4+\\5+\\6+\\7+\\8+\\9", True)
  tes("a-c","\\a+\\b+\\c", True)

def test_awalan():
  tes("-\x03","\\\x00+\\\x01+\\\x02+\\\x03", True)

def test_akhiran():
  tes("\xfa-","\\\xfa+\\\xfb+\\\xfc+\\\xfd+\\\xfe+\\\xff", True)

def test_haha():
  tes("1\\-9","1\\-9", False)