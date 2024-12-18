import random
num=random.randint(1,100)
g=0
while g!=num:
    g=int(input(print("enter guess:")))
    if(g<num):
        print("guess higher!")
    elif(g>num):
        print("guess lower!")
    else:
        print("you won!")    