from lib.elimination.epsilon import EpsilonElimination
from lib.cfg import CFG

def test_01():
  data = {
    "groups":{},
    "terminals":["1","0"],
    "rules":{
      "S": [["S","T"],["S","U","1"],["0"]],
      "T": [["1","S","1"],["0","T"],[]],
      "U": [["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])
  ee = EpsilonElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("S","T"),("S",),("S","U","1"),("0",)),
    "T": (("1","S","1"),("0","T"),("0",)),
    "U": (("S","0","0"),("1","0"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

def test_02():
  data = {
    "groups":{},
    "terminals":["1","0"],
    "rules":{
      "S": [["S","T"],["S","U","1"],["0"]],
      "T": [["1","S","1"],["0","T"],[],["U","S","0"]],
      "U": [["S","0","0"],["1","0"],[]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])
  ee = EpsilonElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("S","T"),("S",),("S","U","1"),("0",),("S","1")),
    "T": (("1","S","1"),("0","T"),("0",),("U","S","0"),("S","0")),
    "U": (("S","0","0"),("1","0"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

def test_03():
  data = {
    "groups":{},
    "terminals":["1","0"],
    "rules":{
      "S": [["T","U"],["T","1","U"],["0"],[]],
      "T": [["S"],["S","T"],["1"],[]],
      "U": [["1","0","S"],[]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])
  ee = EpsilonElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("U",),("T",),("1",),("0",),("T","U"),("T","1","U"),("T","1"),("1","U")),
    "T": (("S",),("T",),("S","T"),("1",)),
    "U": (("1","0","S"),("1","0"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

def test_04():
  data = {
    "groups":{},
    "terminals":["1","0"],
    "rules":{
      "S": [["T","U"],["T","1","U"],["0"]],
      "T": [["S"],["S","T"],["1"]],
      "U": [["1","0","S"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])
  ee = EpsilonElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("T","U"),("T","1","U"),("0",)),
    "T": (("S",),("S","T"),("1",)),
    "U": (("1","0","S"),)
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)
