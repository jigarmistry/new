def main():
    digits= { 
                'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,
                'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9
            }
    list3=[]
    telephone=raw_input("Enter telephone no(XXX-XXX-XXXX): ")
    if len(telephone)==12:
        telephone1=telephone.split('-')
        for i in telephone1:
            for j in i:
                if j in digits:
                    list3.append(digits[j])
                else:
                    list3.append(j)
        list3.insert(3,'-')
        list3.insert(7,'-')
        string=''
        for i in range(len(list3)):
                print string.join(str(list3[i])),       
    else:
        print "Not valid no."
        
    
main()
