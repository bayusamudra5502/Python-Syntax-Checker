from lib.cfg import CFG
from lib.elimination.unreachable import UnreachableElimination

def test_01():
  data = {
    "groups":{},
    "terminals":["1","0","2"],
    "rules":{
      "S": [["S","T"],["S","U","1"],["0"],["D","U","S"]],
      "T": [["1","S","1"],["0","T"]],
      "U": [["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"S")
  ue = UnreachableElimination(obj)

  res = ue.eliminate()
  ans = {
    "S": (("S","T"),("S","U","1"),("0",)),
    "T": (("1","S","1"),("0","T")),
    "U": (("S","0","0"),("1","0"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

  assert set(res.terminals) == {"0","1"}

def test_02():
  data = {
    "groups":{},
    "terminals":["1","0","2","3"],
    "rules":{
      "S": [["S","T"],["S","U","1"],["0","3","D"]],
      "T": [["1","S","1"],["0","T","2"]],
      "U": [["S","0","0"],["1","0"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"S")
  ue = UnreachableElimination(obj)

  res = ue.eliminate()
  ans = {
    "S": (("S","T"),("S","U","1")),
    "T": (("1","S","1"),("0","T","2")),
    "U": (("S","0","0"),("1","0"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

  assert set(res.terminals) == {"0","1","2"}

def test_03():
  data = {
    "groups":{},
    "terminals":["a","b"],
    "rules":{
      "S": [["A","S","B"],["A","B"]],
      "A": [["a","A","S"],["a","A"],["a"]],
      "B": [["S","b","S"],["b","S"],["S","b"],["b"],["a","A","S"],["a","A"],["a"],["b","b"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"S")
  ue = UnreachableElimination(obj)

  res = ue.eliminate()
  ans = {
      "S": (("A","S","B"),("A","B")),
      "A": (("a","A","S"),("a","A"),("a",)),
      "B": (("S","b","S"),("b","S"),("S","b"),("b",),("a","A","S"),("a","A"),("a",),("b","b"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

  assert set(res.terminals) == {"a","b"}

