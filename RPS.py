import random
random.randint(0,2)

a = random.randint(0,2)
b = random.randint(0,2)

# str[0:"グー",1:"パー",2:"チョキ"]
print(a)
print(b)

for i in range (3):
    if print("win" or "lose"):
        break

    if a==0 and b==2:
        print("win")
    elif a==0 and b==1:
        print("lose") 
    # else:
        continue       

    if a==1 and b==0:
        print("win")
    elif a==1 and b==2:
        print("lose")

    if a==2 and b==1:
        print("win")
    elif a==2 and b==0:
        print("lose")

