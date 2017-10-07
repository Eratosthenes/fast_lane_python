class Human:
  species="H. sapiens"

  def __init__(self,name):
    self.name=name
    self.age=0

  def say(self,msg):
    return "{0}: {1}".format(self.name,msg)

  @classmethod
  def get_species(cls):
    return cls.species
