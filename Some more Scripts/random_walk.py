import random

a, b, c, d = 0, 0, 0, 0
test = 1000000

result = []

for i in range(test):
    da, db, dc, dd = random.choice([(1 ,0 ,0 ,0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)])
    a += da
    b += db
    c += dc
    d += dd



    if 0 <= op <= 10:
        a += 1
    elif 11 <= op <= 30:
        b += 1
    elif 31 <= op <= 60:
        c += 1
    elif 61 <= op <= 100:
        d += 1
    result.append(op)
"""
maior = menor = a

if maior < b:
    maior = b
if maior < c:
    maior = c
if maior < d:
    maior = d
if menor > b:
    menor = b
if menor > c:
    menor = c
if menor > d:
    menor  = d
"""
dif = (maior - menor)/test*100
print(type(a))

print(f'A = {a}, {a/test*100:.2f}%')
print(f'B = {b}, {b/test*100:.2f}%')
print(f'C = {c}, {c/test*100:.2f}%')
print(f'D = {d}, {d/test*100:.2f}%')
print(f'A maior diferença entre as opçoes é de {dif:.2f}%.')
#print(result)