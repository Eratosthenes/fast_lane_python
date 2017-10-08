def add_apples(func):
  def get_fruits():
    fruits = func()
    fruits.append('apple')
    return fruits
  return get_fruits

# @add_apples
# def get_fruits():
#   return ['banana','mango','orange']



