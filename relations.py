from fuzzy import Set

"""
Simple Relation defined by lists
"""
class Relation():
  def __init__(self, rel: list):
    self.rel = rel

  def __repr__(self) -> str:
    prt = str()
    for row in self.rel:
      for el in row:
        prt += f'{el}\t'
      prt += '\n'
    return prt

  def row(self, index) :
    return self.rel[index]

  def col(self, index):
    res = list()
    for row in self.rel:
      res.append(row[index])
    return res


"""
Relation between sets
"""
class SetRelation(Relation):
  def __init__(self, fr: Set, to: Set):
    super(SetRelation, self).__init__([])
    for ela in fr.set:
      row = list()
      for elb in to.set:
        row.append((min(ela[0],elb[0]), (ela[1],elb[1])))
      self.rel.append(row)

  def __repr__(self) -> str:
    prt = str()
    for row in self.rel:
      for el in row:
        prt += f'{el[0]}\t'
      prt += '\n'
    return prt