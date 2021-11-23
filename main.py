from lib.cyk.cyk import CYK

o = CYK("data/cnf-repaired.json", "data/input.py")
print(o.parse())

print(o.validityCheck())