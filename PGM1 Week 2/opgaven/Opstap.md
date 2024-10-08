
In de volgende opgaven ga je oefenen met conditionele statements, strings en lijsten in Python. Ook ga je oefenen met het vinden van fouten (bugs) in code.

# Conditionele statements
## Opgave 1-A
#### Wat is de output?
```
    x = 8

    if x > 5 :
        print("if statement is True")
    print("staat buiten de if statement")
```
Output: Beide (if statement is True **en** staat buiten de if statement)


## Opgave 1-B
#### Wat is de output?
```
x = 8

if x < 5 :
    print("if statement is True")
print("staat buiten de if statement")
```
Output: staat buiten de if statement

## Opgave 1-C
#### Wat is de output?
```
x = 8

if x < 5 :
    print("if statement is True")
else:
    print("if statement is false")
print("staat buiten de if-else statement")
```
Output: if statement is false __en__ staat buiten de if-else statement

## Opgave 1-D
#### Wat is de output?
```
x = 5

if x < 5 :
    print("if statement is True")
elif x > 5:
    print("elif statement is True")
else:
    print("zowel de if en elif statements zijn false")
```
Output: zowel de if en elif statements zijn false

## Opgave 1-E
#### Wat is de output?
```
temp = 23.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")
```
Output: Warm

## Opgave 1-F
#### Wat is de output?
```
temp = 15.0

if temp > 35.0:
    print("Heet!")
else:
    if temp > 20.0:
        print("Warm")
    else:
        if temp > 10.0:
            print("Koel")
        else:
            print("Brrr!")
```
Output: Koel

## Opgave 1-G
#### Wat is de output?
```
x = 5

if x < 5 :
    x = x + 3
elif x > 5:
    x = x - 3
print(x)
```
Output: 5

## Opgave 1-H
#### Wat is de output?
```
x = 4

if x < 5 :
    x = x + 3
elif x > 5:
    x = x - 3
else:
    x = x * 2

print(x)
```
Output: 7

# Opgave 1-I
#### Wat is de output?
```
naam = "Suzan"
if naam <= 'E':
    print("groep 1")
elif naam <= 'J':
    print("groep 2")
elif naam <= 'O':
    print("groep 3")
elif naam <= 'U':
    print("groep 4")
else:
    print("groep 5")
```
Output: groep 4

## Opgave 1-J
#### Wat is de output?
```
naam = "Emily"
if naam  <= 'E':
    print("groep 1")
elif naam  <= 'J':
    print("groep 2")
elif naam  <= 'O':
    print("groep 3")
elif naam <= 'U':
    print("groep 4")
else:
    print("groep 5")
```
Output: groep 2


# Strings en lists

## Opgave 2-A
#### Wat is de output?
```
a = "123"
print(2 * a)

```
Output: 123123

## Opgave 2-B
#### Wat is de output?
```
a = "hanze"
b = "Hogeschool"
print(2 * a + b)
```
Output: hanzehanzeHogeschool


## Opgave 2-C
#### Wat is de output?
```
a = 123
b = "456"
print(a, b)
```
Output: 123 456

## Opgave 2-D
#### Wat is de output?
```
p = [3, 1, 4, 1, 5]
c = [2, 9, 9, 7, 9, 2, 4, 5, 8]

answer0 = p[0:3]
answer1 = c[5]

print(answer0 * answer1)
```
Output: [3, 1, 4, 3, 1, 4]