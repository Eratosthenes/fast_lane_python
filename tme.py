import sys

content = open(sys.argv[1]).read().splitlines()
nlines = len(content)
nwords = sum(map(lambda x:len(x.split()), content))
print "# lines:",nlines
print "# words:",nwords

