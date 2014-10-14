def add(x,y): return x+y
print 'Sum:',reduce(add, range(1, 10000000))
args=(1,2)
print add(*args)