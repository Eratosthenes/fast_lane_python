import pdb
import random

class treenode:

  def __init__(self,v):
    self.value = v
    self.left = None
    self.right = None

  def ins(self,val):
    if val < self.value:
      if self.left == None:
	self.left = treenode(val)
      else:
	self.left.ins(val)
    else:
      if self.right == None:
	self.right = treenode(val)
      else:
	self.right.ins(val)
        
  def treemax(self):
    if self.right == None:
      return self.value
    else:
      return self.right.treemax()

class tree:

  def __init__(self):
    self.root = None
    
  def insrt(self,val):
    newnode = treenode(val)
    if self.root == None:
      self.root = newnode
      return
    self.root.ins(newnode)

  def max(self):
    return self.root.treemax()

if __name__ == '__main__':
  a = range(10)
  random.shuffle(a)
  tree = tree()
  print("array:",a)
  for i in a:
    tree.insrt(i)

  print("max = {}".format(tree.max()))
  pdb.set_trace()



