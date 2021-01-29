from fuzzy import Set
from matplotlib import pyplot

def dot_graph(fuzzy: Set):
  pyplot.plot(fuzzy.set, ".")
  pyplot.show()
