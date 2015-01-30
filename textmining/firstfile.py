__author__ = 'matjaz'


# conditional expression
a=True
result = "Matjaz" if a else "Karen"
print(result)

# lambda function 1
is_five = lambda x: x + 4 + 1

print(is_five(6))

# lambda function 2
myname = lambda name: name == 'Matjaz'

l = ['Johnny', 'Michael', 'Matjaz']
for i in l:
    print(myname(i))

l2 = [ i for i in l if myname(i) ]
print(l2)
print("Hello Matjaz!")

