import random
lettare="ABCDEWQSZXTGVBYUJNMPLNM"
nombre="123456789"
lowercase_letter=lettare.lower()
symbols="()[]&;:/.\\"
upper ,lower ,num ,syms=True,True,True,True
all=""
if upper:
    all += lettare 
if lower:
    all += lowercase_letter
if num:
    all+= nombre
if syms:
    all+= symbols
length=int(input(print("entre length")))
amount=int(input(print("entre amount")))
for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)