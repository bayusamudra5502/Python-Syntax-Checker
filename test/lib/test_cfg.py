from lib.cfg import CFG

def test_inverted():
  data = {
    "groups":{
      "number": "[0-9]+",
      "lower": "[a-z]+"
    },
    "terminals":["(",")","*","+"],
    "rules":{
      "I": [["lower"], ["I", "lower"], ["I", "number"]],
      "F": [["I"], ["(", "E", ")"],["E"]],
      "T": [["F"], ["T", "*", "F"],["T"],["T"]],
      "E": [["T"], ["E", "+", "T"]]
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])
  invert_ans = {
    ("lower",) : ("I",),
    ("I","lower"): ("I",),
    ("I","number"): ("I",),
    ("I",): ("F",),
    ("(","E",")"): ("F",),
    ("E",): ("F",),
    ("F",): ("T",),
    ("T","*","F"): ("T",),
    ("T",): ("T","E"),
    ("E", "+", "T"): ("E",)
  }

  assert obj.getInvertedTable() == invert_ans

def test_properti():
  data = {
    "groups":{
      "number": "[0-9]+",
      "lower": "[a-z]+"
    },
    "terminals":["(",")","*","+"],
    "rules":{
      "I": [["lower"], ["I", "lower"], ["I", "number"]],
      "F": [["I"], ["(", "E", ")"]],
      "T": [["F"], ["T", "*", "F"]],
      "E": [["T"], ["E", "+", "T"]]
    }
  }

  jawaban = {
    "groups":{
      "number": "[0-9]+",
      "lower": "[a-z]+"
    },
    "terminals":("(",")","*","+"),
    "rules":{
      "I": (("lower",), ("I", "lower"), ("I", "number")),
      "F": (("I",), ("(", "E", ")")),
      "T": (("F",), ("T", "*", "F")),
      "E": (("T",), ("E", "+", "T"))
    }
  }

  obj = CFG(data["rules"], data["groups"], data["terminals"])

  assert obj.groups == jawaban["groups"]
  assert obj.terminals == jawaban["terminals"]
  assert obj.rules == jawaban["rules"]
  assert obj.getVariables() == ("I","F","T","E")

  try:
    obj.groups = {}
    assert False
  except:
    assert True
  
  try:
    obj.rules = {}
    assert False
  except:
    assert True
  
  try:
    obj.terminals = {}
    assert False
  except:
    assert True
