"""
Fuzzy Set
"""
class Set():
  def __init__(self, var: list, dp = "set|dis"):
    self.set = var
    self.dispmode = dp

  def __repr__(self) -> str:
    prt = str()
    for el in self.set:
      prt += f'{el[0]}|{el[1]} + '
    return prt[0:len(prt)-3]
  
  def value(self, value):
    for el in self.set:
      if el[1] == value: return el
    return None
  
  def level(self, alpha):
    res = list()
    for el in self.set:
      if el[0] >= alpha: res.append(el)
    return Set(res)

  def scale(self, alpha):
    res = list()
    for el in self.set:
      res.append((alpha*el[0], el[1]))
    return Set(res)
  
  def powr(self, alpha):
    res = list()
    for el in self.set:
      res.append((el[0]**alpha, el[1]))
    return Set(res)
