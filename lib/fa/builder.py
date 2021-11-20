"""Modul builder
Modul untuk melakukan proses building Regex menjadi
e-NFA

Urutan Parsing:
1. Operator Plus
2. Operator Concat
3. Operator star
4. Operator Kurung
5. Operator Range
6. Parse Termminal
"""

from lib.fa.parser import *
from lib.fa.state import State

def plusBuilder(regex: str) -> tuple[State, State]:
  """Melakukan bulding penjumlahan pada regex.

  Setiap operator \\\+ akan dianggap bukan merupakan operator +.

  Mengembalikan start State dan Final State
  """
  splitted = plusParser(regex)
  
  if len(splitted) == 0:
    # Optimasi supaya langsung dibuat
    return terminalBuilder("")
  elif len(splitted) == 1:
    return concatBuilder(splitted[0])
  else:
    start= State(); end = State()

    for i in splitted:
      resStart, resEnd = concatBuilder(i)
      start.addTransition("", resStart)
      resEnd.addTransition("", end)
    
    return start, end

def concatBuilder(regex: str) -> tuple[State, State]:
  """Melakukan bulding untuk operator concat.
  Tidak boleh terdapat operator + kecuali dalam kurung."""
  splitted = concatParser(regex)
  
  if len(splitted) == 0:
    # Optimasi supaya langsung dibuat
    return terminalBuilder("")
  elif len(splitted) == 1:
    return starBuilder(splitted[0])
  else:
    start = State()
    end = State()

    last = start

    for i in splitted:
      resStart, resEnd = starBuilder(i)
      last.addTransition("", resStart)
      last = resEnd
    
    last.addTransition("", end)

    return start, end

def rangeBuilder(regex: str) -> tuple[State, State]:
  """Melakukan bulding untuk regex range.
  Regex tidak boleh memiliki operator bracket, star, concat, dan +
  
  Range adalah definisi baru dari regex untuk mempesingkat penulisan.
  Contoh regex (0-5) memiliki arti yang sama dengan (0+1+2+3+4+5).
  range berdasarkan urutan pada ASCII.

  Setiap operator \\\- akan dianggap bukan merupakan operator -.
  
  Mengembalikan start state dan final state"""
  
  newRegex, reParse = rangeParser(regex)

  if reParse:
    return plusBuilder(newRegex)
  else:
    return terminalBuilder(newRegex)

def starBuilder(regex: str) -> tuple[State, State]:
  """Melakukan bulding untuk operator *.
  Regex hanya boleh memiliki operator *, kurung, dan range.

  Setiap karakter \\\* akan dianggap bukan operator *.

  Mengambalikan start state dan final state."""
  
  newRegex, isStar = starParser(regex)

  if isStar:
    start = State()
    end = State()

    startInner, endInner = bracketBuilder(newRegex)

    start.addTransition("", startInner)
    start.addTransition("", end)

    endInner.addTransition("", startInner)
    endInner.addTransition("", end)
    return start, end
  else:
    return bracketBuilder(newRegex)

def bracketBuilder(regex:str) -> tuple[State, State]:
  """Melakukan bulding untuk operator kurung. 
  Regex tidak boleh memiliki operator pada level kurung tertinggi.
  
  Setiap operator \\\( ataupun \\\) dianggap bukan 
  operator kurung.
  
  Mengembalikan start state dan final state."""

  regexSplit, isBracketFound = bracketParser(regex)
  
  if isBracketFound:
    return plusBuilder(regexSplit)
  else:
    return rangeBuilder(regexSplit)


def terminalBuilder(regex:str) -> tuple[State, State]:
  """Melakukan bulding untuk terminal. Regex haruslah sebuah terminal.
  
  Mengemblaikan start state dan final state."""

  start = State(); end = State()

  newRegex = terminalParser(regex)
  start.addTransition(newRegex, end)

  return start, end
