
# for-lussen
Leerdoel: het lezen van (eindige) for-lussen
## Opdracht 1
```
for i in range(5):
    print(i)
```
Wat is de output?

## Opdracht 2
```
L = [2, 4, 6, 8]

for x in L:
    print(x)
```
Wat is de output?


## Opdracht 3
```
L = [9, 7, 5, 3, 1]

for i in range(len(L)):
    print(L[i])
```
Wat is de output?

## Opdracht 4
```
L = [5, 3, 1]
result = 0

for i in range(len(L)):
    result = result + L[1]

print(result)
```
Wat is de output?

## Opdracht 5
```
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = 0

for i in range(len(L)):
    if L[i] % 2 == 0:
        result += L[i]

print(result)
```
Wat is de output?

## Opdracht 6
```
s = "Hanze"
result = 0

for _ in s:
    result += 1

print(result)
```
Wat is de output?

## Opdracht 7
```
s = "Dit is een string"
result = ""

for x in s:
    if x in "eauoi":
        result += x

print(result)
```
Wat is de output?

## Opdracht 8
```
s = "Dit is een string"
result = ""

for i in range(len(s)):
    if s[i- 1] == " ":
        result += s[i]

print(result)
```
Wat is de output?

## Opdracht 9
```
L = []

for i in range(10):
    if i < 2:
        L += [1]
    else:
        L += [L[i-1] + L[i-2]]

print(L)
```
Wat is de output?

## Opdracht 10
```
L = []
temp = 1

for i in range(5):
    if(temp % 2 != 0):
        L += [2 * temp]
        temp =  temp + 5
    else:
        L += [temp]
        temp = temp / 2

print(L)
print(temp)
```
Wat is de output?

# while-lussen
Leerdoel: het lezen van (oneindige) while-lussen

## Opdracht 1
```
L = []
n = 0

while n < 5:
    print(n)
    n += 1
```
Wat is de output?


## Opdracht 2
```
L = [1, 2, 3, 4, 5]

while len(L) > 0:
    print(L)
    L = L[1:]
```
Wat is de output?

## Opdracht 3
```
i = 1

while i < 6:
    print(i)
    
    if i == 3:
        break
        
    i += 1
```
Wat is de output?

## Opdracht 4
```
i = 0

while i < 6:
    i += 1
    
    if i == 3:
        continue

    print(i)
```
Wat is de output?

## Opdracht 5
```
number = 4
faculty = 1

while number  > 0:
    faculty = faculty * number
    number -= 1

print(faculty)
```
Wat is de output?

## Opdracht 6
```
num1 = 5
num2 = 8

while num2 > 0:
    num1 = num1 + num1
    num2 -= 1

print(num1)

```
Wat is de output?