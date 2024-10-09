# Opdracht 1
```
name = "harry"
for x in range(3):
    for x in range(3):
        print(name)
```
Wat is de output?

# Opdracht 2
```
lijst = [1, 2, 3]
for i in range(3):
    for j in lijst:
        print(j)
```
Wat is de output?

# Opdracht 3
```
lol = [[1, 2, 3],[ 9, 8, 7]]
for i in lol:
    for j in i:
        print(j)
```
Wat is de output?

# Opdracht 4
```
lol = [[1, 2, 3][9, 8, 7]]
for y in range(len(lol)):
    for x in range(len(lol[y]))
        print(lol[y][x])
```
Wat is de output?

# Opdracht 5
```
lol = [[4, 5], [8, 9], [1, 2]]
k = 1
for i in range(2):
    k = k * 10
    for j in range(2):
        lol[i][j] *= k
print(lol)
```
Wat is de output?

# Opdracht 6
```
for i in range(5):
    for j in range(i):
        print(i * j)
```
Wat is de output?

# Opdracht 7
```
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
```
Wat is de output?

# Opdracht 8
```
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')
```
Wat is de output?