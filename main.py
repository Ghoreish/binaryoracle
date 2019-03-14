import random
a=random.randint(0,1)
l=''
while True:
    print("I guess your number is:",a)
    print("Is this your number?(y/n):",end=" ")
    x=input()
    if x=="y" or x=="Y":
        l+=str(a)
    elif x=="n" or x=="N":
        l+=str((a+1)%2)
    else:
        print("ERROR!")
        continue
    m=0
    c = 0
    if len(l)>=3:
        for i in range(1,len(l)-1):
            if l[i:] in l[:-1]:
                c=1
                if l[i:]+"1" in l and l[i:]+"0" in l:
                    a=random.randint(0,1)
                else:
                    if l[i:]+"1" in l:
                        a=1
                    else:
                        a=0
                break
    if c==0:
        a=random.randint(0,1)
