def add(x, y):
    return x + y

params = (1, 2)

print add(*params)


params = {'name': 'Sir Robin', 'greeting': 'Well met'}

def with_stars(**kwds):
        print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
        print kwds['name'], 'is', kwds['age'], 'years old'

args = {'name': 'Mr. Joe', 'age': 42}
with_stars(**args)

without_stars(args)
