from lib.elimination.ungenerating import UngeneratingElimination
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
  ue = UngeneratingElimination(obj)

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

def test_02():
  data = {
    "groups":{},
    "terminals":["a","b"],
    "rules":{
      "S": [["A","B"],["C","A"]],
      "A": [["a"]],
      "B": [["B","C"],["A","B"]],
      "C": [["a","B"],["b"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ue = UngeneratingElimination(obj)

  res = ue.eliminate()
  ans = {
    "S": (("C","A"),),
    "A": (("a",),),
    "C": (("b",),)
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

def test_03():
  data = {
    "groups":{},
    "terminals":["a","b"],
    "rules":{
      "S": [["A","B"],["C","A"]],
      "A": [["a"],["b","a"]],
      "B": [["B","C"],["A","B"]],
      "C": [["a","B"],["b"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ue = UngeneratingElimination(obj)

  res = ue.eliminate()
  ans = {
    "S": (("C","A"),),
    "A": (("a",),("b","a")),
    "C": (("b",),)
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)

def test_04():
  data = {
    "groups":{},
    "terminals":["a","b"],
    "rules":{
      "S": [["A","B"],["C","A"]],
      "A": [["a"]],
      "B": [["B","C"],["A","B"],[]],
      "C": [["a","B"],["b"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"],"I")
  ue = UngeneratingElimination(obj)

  res = ue.eliminate()
  ans = {
    "S": (("C","A"),("A","B")),
    "A": (("a",),),
    "B": (("B","C"),("A","B"), ()),
    "C": (("b",),("a","B"))
  }

  for i in ans:
    a = res.rules[i]
    b = ans[i]

    assert set(a) == set(b)