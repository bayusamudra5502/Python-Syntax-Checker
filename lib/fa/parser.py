"""
Module Parser
Library parsing Regular Expression
"""

def plusParser(regex: str) -> tuple[str]:
  """Melakukan parsing regex untuk operator +.
  
  Regex bolehlah sembarang.
  
  Mengembalikan tuple of string dari operand operator +"""
  splitted = []
  bracketLevel = 0
  isSkipped = False

  for i in regex:
    if i == "\\":
      isSkipped = True
      splitted[-1] += "\\"
    elif isSkipped:
      splitted[-1] += i
      isSkipped = False
    elif i == "(":
      splitted[-1] += i
      bracketLevel += 1
    elif i == ")":
      if bracketLevel > 0:
        splitted[-1] += 1
        bracketLevel -= 1
      else:
        raise SyntaxError("Terdapat kurung yang belum dibuka") 
    elif bracketLevel > 0 and i != "+":
      splitted[-1] += i
    else:
      splitted.append("")
  
  return tuple(splitted)
  

def concatParser(regex: str) -> tuple[str]:
  """Melakukan parsing regex untuk operator concat.
  
  Mengembalikan tuple of string dari operand concat

  Asumsi: Regex tidak memiliki operator + selain dalam kurung"""
  splitted = []
  bracketLevel = 0
  isSkipped = False

  for i in regex:
    if i == "\\":
      isSkipped = True
      splitted.append("\\")
    elif isSkipped:
      splitted[-1] += i
      isSkipped = False
    elif i == "(":
      if bracketLevel > 0:
        splitted[-1] += "("
      else:
        splitted.append("(")
      
      bracketLevel += 1
    elif i == ")":
      if bracketLevel > 0:
        bracketLevel -= 1
        splitted[-1] += ")"
      else:
        raise SyntaxError("Terdapat kurung yang belum dibuka") 
    elif i == " ":
      pass
    elif i == "*" or bracketLevel > 0:
      splitted[-1] += i
    else:
      splitted.append(i)

  return tuple(splitted)

def rangeParser(regex: str) -> tuple:
  """Melakukan parsing untuk operator range pada regex.
  
  Diasumsikan hanya maksimal terdapat sebuah operator range pada regex.
  
  Mengembalikan:
  * newRegex : Regex baru hasil parsing
  * isOpFound : True bila newRegex perlu diparsing ulang"""
  isOpFound = False
  isSkipped = False
  start = 0
  end = 255

  for i in regex:
    if i == "\\":
      isSkipped = True
    elif i == "-" and not isSkipped:
      isOpFound = True
    elif isOpFound:
      end = ord(i)
    else:
      isSkipped = False
      start = ord(i)
  
  if isOpFound:
    newRule = "+".join([chr(i) for i in range(start,end+1)])
    return newRule, (len(newRule) > 0)
  else:
    return regex, False

def starParser(regex: str) -> tuple:
  """Melakukan parsing terhadap operator *.
  
  Diasumsikan hanya terdapat oprator * di luar kurung
  
  Menghasilkan :
  * regex baru hasil parsing
  * boolean yang memberikan True bila terdapat operator *"""
  newRegex = ""
  isOpFound = False
  bracketLevel = 0
  skipped = False

  for i in regex:
    if i == "\\":
      skipped = True
      newRegex += i
    elif skipped:
      newRegex += i
      skipped = False
    elif i == "(" :
      bracketLevel += 1
      newRegex += i
    elif i == ")":
      if bracketLevel > 0:
        bracketLevel -= 1
        newRegex += i
      else:
        raise SyntaxError("Terdapat kurung yang belum dibuka") 
    elif i == " ":
      pass
    elif bracketLevel > 0:
      newRegex += i
    elif i == "*":
      if len(newRegex) > 0:
        if not isOpFound:
          isOpFound = True
      else:
        raise SyntaxError("Tidak ditemukan symbol yang akan diberikan operator *")
    else:
      newRegex += i
  
  return newRegex, isOpFound

def bracketParser(regex: str) -> tuple:
  """Melakukan parsing bracket pada regex.
  
  Asumsi tidak ada operator lain selain di dalam kurung
  
  Mengembalikan :
  * newRegex (bool) : Regex baru hasil parsing
  * isBracketFound (bool) : True bila ada kurung"""
  regexSplit = ""
  isBracketFound = False
  bracketLevel = 0
  skipped = False
  
  for i in regex:
    if i == "\\":
      skipped = True
      regexSplit += i
    elif skipped:
      skipped = False
      regexSplit += i
    elif i == " ":
      pass
    elif i == "(":
      bracketLevel += 1
      if bracketLevel > 1:
        regexSplit += i
      else:
        isBracketFound = True
    elif i == ")":
      if bracketLevel > 0:
        if bracketLevel > 1:
          regexSplit += i
        bracketLevel -= 1
      else:
        raise SyntaxError("Terdapat kurung yang belum dibuka")
    else:
      regexSplit += i
  
  if bracketLevel != 0:
    raise SyntaxError("Terdapat kurung yang belum ditutup")
  
  return regexSplit, isBracketFound

def terminalParser(regex: str) -> str:
  """Mengembalikan string parsing untuk regex terminal.
  
  Menghilangkan tanda \\ saat menggunakan Escape Sequence"""
  if len(regex) > 2:
    raise SyntaxError("Terminal haruslah memiliki hanya satu symbol")
  elif len(regex) > 0 and regex[0] == "\\":
    if len(regex) == 2:
      return regex[1]
    else:
      raise SyntaxError("Terminal haruslah memiliki hanya satu symbol")
  elif len(regex) > 1:
    raise SyntaxError("Terminal haruslah memiliki hanya satu symbol")
  else:
    return regex