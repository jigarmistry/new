import random

print "Two Nos are between 100,200"
no1=random.randint(100,200)
no2=random.randint(100,200)
sum=no1+no2

#print no1,no2
guess=int(input("Enter the sum of that two nos:"))
if sum==guess:
    print "Congo you win quiz."
else:
    print "Sorry"
    print "Answer:",sum

