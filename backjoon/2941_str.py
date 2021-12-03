import sys

a = str(sys.stdin.readline())

t = a.replace('c=', 'a')
t = t.replace('c-', 'a')
t = t.replace('dz=', 'a')
t = t.replace('d-', 'a')
t = t.replace('lj', 'a')
t = t.replace('nj', 'a')
t = t.replace('s=', 'a')
t = t.replace('z=', 'a')
print(len(t)-1) # readline으로 입력받아와서 공백이 포함되어있어 -1해줘야함


# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in croatia:
#   a = a.replace(i, 'a')
# print(len(a))
