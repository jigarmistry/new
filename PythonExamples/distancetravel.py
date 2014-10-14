speed=int(input("What is speed of vehicle in mph?"))
hours=int(input("Hoe many hours has it traveled ?"))

print "\nHour\tDistance Traveled"
print "_________________________"
distance=speed*hours
j=1
for i in range(speed,distance+speed,speed):
   print j,"\t",i
   j=j+1
    
