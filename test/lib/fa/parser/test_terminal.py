from lib.fa.parser import *

def isEqual(regex, ans):
  return terminalParser(regex) == ans

def test_terminal_1():
  assert isEqual("","")
  assert isEqual("\\\\","\\")
  assert isEqual("\.",".")

def test_terminal_2():
  assert isEqual(r"\n","n")

def test_teminal_3():
  assert isEqual("a","a")

def test_terminal_n1():
  isError = False

  try:
    terminalParser("ab")
  except:
    isError = True
  
  assert isError

def test_terminal_n2():
  isError = False
  
  try:
    terminalParser("\\")
  except:
    isError = True
  
  assert isError

def test_terminal_n3():
  isError = False
  
  try:
    terminalParser("abc")
  except:
    isError = True
  
  assert isError