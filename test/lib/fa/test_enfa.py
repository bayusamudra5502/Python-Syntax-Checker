from lib.fa.enfa import ENFA

def test_01():
  obj = ENFA("a+b")
  
  obj.fit()

  assert obj.match("a")
  assert obj.match("b")
  assert not obj.match("c")
  assert not obj.match("")

def test_02():
  obj = ENFA("a*")
  obj.fit()

  assert obj.match("")
  assert obj.match("a")
  assert obj.match("aaaaa")
  assert not obj.match("c")
  assert not obj.match(" a")

def test_03():
  obj = ENFA("12")
  obj.fit()

  assert obj.match("12")
  assert not obj.match("")
  assert not obj.match("21")

def test_04():
  obj = ENFA("(1+2)* 21 + 2")
  obj.fit()

  assert obj.match("2")
  assert obj.match("21")
  assert obj.match("112121")
  assert not obj.match("1")
  assert not obj.match("112")

def test_05():
  obj = ENFA("(a-z)*")
  obj.fit()

  assert obj.match("")
  assert obj.match("itebe")
  assert obj.match("tubeskuh")
  assert obj.match("menangis")
  assert not obj.match("kumenanIsh")

def test_06():
  obj = ENFA("(A-Z)(A-Z)*\\-(A-Z+0-9+\\-)*")
  obj.fit()

  assert obj.match("AYAM-12BAKAKAK")
  assert obj.match("H-SAYEMBARA100")
  assert obj.match("AKU-DAN-TUBESKUH")
  assert not obj.match("AKU123-DAN-TUBESKUH")

def test_07():
  # Regex penamaan variabel Python
  obj = ENFA("(a-z + A-Z + _)(a-z+A-Z+_+0-9)*")
  obj.fit()

  assert obj.match("test_07")
  assert obj.match("_AyamBakakak")
  assert obj.match("test")
  assert obj.match("kumbangLaut")
  assert not obj.match("10JutaDollar")
  assert not obj.match("ayamLaut.")
  assert not obj.match("ayamLaut?")