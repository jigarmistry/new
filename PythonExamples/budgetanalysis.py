budget=int(input("Enter your budget:"))
keep='y'
total=0

while keep=='y':
    expense=int(input("Enter your expense"))
    total=total+expense
    keep=raw_input("Have any another expense(y-yes,n-no)")
    
if budget>total:
    print "under budget",budget-total
else:
    print "over budget",total-budget