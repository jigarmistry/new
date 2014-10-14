def factorial( number ):

   if number <= 1:   # base case
      return 1
   else:
      return number * factorial( number - 1 )  # recursive call

for i in range( 20 ):
   print "%2d! = %d" % ( i, factorial( i ) )
