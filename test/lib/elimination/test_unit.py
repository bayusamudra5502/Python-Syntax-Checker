from lib.elimination.unit import UnitElimination
from lib.cfg import CFG

def test_01():
  data = {
    "groups":{},
    "terminals":["1","0"],
    "rules":{
      "S": [["S","T"],["S","U","1"],["0"]],
      "T": [["1","S","1"],["0","T"]],
      "U": [["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ee = UnitElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("S","T"),("S","U","1"),("0",)),
    "T": (("1","S","1"),("0","T")),
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
      "S": [["U"],["S","T"],["S","U","1"],["0"]],
      "T": [["1","S","1"],["0","T"]],
      "U": [["T"],["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ee = UnitElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("S","T"),("S","U","1"),("0",),("S","0","0"),("1","0"),("1","S","1"),("0","T")),
    "T": (("1","S","1"),("0","T")),
    "U": (("S","0","0"),("1","0"),("1","S","1"),("0","T"))
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
      "S": [["U"],["S","T"],["S","U","1"],["0"]],
      "T": [["1","S","1"],["0","T"], ["T"],["0"]],
      "U": [["T"],["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ee = UnitElimination(obj)

  res = ee.eliminate()
  ans = {
    "S": (("S","T"),("S","U","1"),("0",),("S","0","0"),("1","0"),("1","S","1"),("0","T")),
    "T": (("1","S","1"),("0","T"),("0",)),
    "U": (("S","0","0"),("1","0"),("1","S","1"),("0","T"),("0",))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)