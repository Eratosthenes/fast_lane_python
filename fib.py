def fib_gen(n):
  a,b=0,1
  while b<n:
    a,b=b,a+b
    yield b

