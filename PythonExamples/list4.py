listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

print [age for (name, age, job) in listoftuple]

li=[x**2 for x in range(10) ]
for i in li:
    print i
