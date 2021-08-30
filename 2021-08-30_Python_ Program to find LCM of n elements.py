#Python Program to find LCM of n elements
"Computer Programming Tutor, Aug 30,2021"

def lcmsolver(no1,no2):
    if(no1 > no2):
        no = no1
        tp = no2
    else:
        no = no2
        tp = no1
    rem = no % tp
    while(rem != 0):
        no = tp
        tp = rem
        rem = no % tp
    gcd = tp
    lcm = int(int(no1*no2)/int(gcd))
    return lcm

l = [7,5,8]
no1 = l[0]
no2 = l[1]
lcm = lcmsolver(no1,no2)

for i in range(2,len(l)):
    lcm = lcmsolver(lcm,l[i])

print(lcm)
    
    
        

