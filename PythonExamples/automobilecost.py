print "Enter your monthly Costs for Expenses:";

loanpayment=int(input('Enter loan payment:'))
insurance=int(input('Enter Insurance:'))
gas=int(input('Enter gas :'))
oil=int(input('Enter oil :'))
tires=int(input('Enter tires :'))
maintenance=int(input('Enter maintenance :'))

total=loanpayment+insurance+gas+oil+tires+maintenance;

print "your total monthly cost for expenses is",total
print "your total annual cost for expenses is",total*12



