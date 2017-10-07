def double_numbers_gen(iterable):
  for i in iterable:
    yield(i+i)

if __name__=='__main__':
  for value in double_numbers_gen(xrange(10)):
    print(value)
    if value>5:
      break


