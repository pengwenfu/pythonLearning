print("hello" , 2000)
print('''dssssssss
...333333
...weeeeeee''')
# i = int(input())
# i = int(input())
classmate = ['mechile','bob','tracty']
print(classmate)
print(len(classmate))
print(classmate[0],classmate[1],classmate[2])
print(classmate[-1],classmate[-2],classmate[-3])
classmate.append('vinnypeng')
print(classmate)
print(classmate.pop(2))
print(classmate)
classmate[0] = 'new_mechile'
print(classmate)
classmate.insert(2,122)
print(classmate)
classmate.append(['eee',222])
print(classmate)
print(classmate[4][0])

classmate = ('mecidhd','bod',2233);
print(classmate)
set = (3,);
print(set)

age = 12
if age > 18 :
    print("age lager than 18")
    age = 13
else:
    print("your age is %d" %(age))

for name in classmate:
    print(name)

for i in range(5):
    print(i)

j = 0
while j < 10:
    print(j)
    j +=1

d = {'d1':23, 'd2':32,'d3':44,'d4':55}
print(d['d2'],d.get("ggee"))
if d.get("222"):
    print(d['d2'])
else:
    print('not find key')

d.pop('d2')
print(d)


def my_abs(x):
    if x > 0 :
        return x
    else:
        return -x


print(my_abs(-19))

def nonf(age):
    if not isinstance(age,(int,float)):
        raise TypeError('dddddddd')

    if age > 18:
        print('age > 18')

nonf('dddd')