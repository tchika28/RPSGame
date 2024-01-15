import random
random.randint(0,2)

# str[0:"グー",1:"パー",2:"チョキ"]

for i in range (100):
    a = int(input("userinput:"))
    b = random.randint(0,2)
    print("a:",a)
    print("b:",b)
    if a == b:
        print("aiko")
        continue

    elif a==0 and b==2:
        print("win")
        break
    elif a==0 and b==1:
        print("lose") 
        break
   
    elif a==1 and b==0:
        print("win")
        break
    elif a==1 and b==2:
        print("lose")
        break

    elif a==2 and b==1:
        print("win")
        break
    elif a==2 and b==0:
        print("lose")
        break
