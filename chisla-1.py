

def num_rev(num1):
    s2 = ''
    s1 = str(num1)
    #print('s1     ',s1)
    l1 = len(str(num1))
    #print('l1     ',l1)
    for i in range(l1-1,-1,-1):
    #    print('s2    ',s2)
        s2 = s2+s1[i]  
    num_inv = int(s2)

    return num_inv


print("*"*80, "\n")
n1 = int(input("Number1:  "))
in1 = num_rev(n1)
#print("inv", num_rev(n1))
while n1 != in1:
    print(' n1   ', n1, '\n', 'n2   ', in1)
    print('')
    #print("inv", in1)
    #print("==")
    n1 = n1+in1
    in1 =  num_rev(n1)

print('result', n1)

