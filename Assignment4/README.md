# Psych403_Fall2022 - Assignment 4 - Mark Thomas

[Level 2 Exercises](https://kylemath.github.io/pytutorial/level2_exercises.html)

## Conditional Exercises
**1.**
```python
if not response or response == "NaN":
   print("subject did not respond")
elif response == '1' or response == '2':
   print("OK")
else:
   print("subject pressed the wrong key")
```

**2.**
```python
if not response or response == "NaN":
   print("subject did not respond")
elif response == '1' or response == '2':
   if response == '1':
      print("Correct!")
   elif response == '2':
      print("Incorrect!")
else:
   print("subject pressed the wrong key")
```

**3.**
Yes; here's a table of some inputs and their outputs:
| Input | Output |
| ----- | ------ |
| '1' | Correct! |
| '2' | Incorrect! | 
| '0' | subject pressed the wrong key |
| 'a' | subject pressed the wrong key |
| '' | subject did not respond |



## For Loop Exercises

**1.**
```python
for c in "Mark":
   print(c)
```

**2.**
```python
i = 0
for c in "Mark":
   print(c, i)
   i += 1
```

**3.**
```python
names = ["Amy", "Rory", "River"]
for name in names:
   for c in name:
      print(c)
```

**4.**
```python
names = ["Amy", "Rory", "River"]
for name in names:
   i = 0
   for c in name:
      print(c, i)
      i += 1
```



## While Loop Exercises
**1.**
```python
i = 20
while i > 0:
   if i > 10:
      print("image1.png")
   else:
      print("image2.png")
   i -= 1
```

**2.**
```python
response = None
while response != '1' and response != '2':
   print("Showing an image")
   response = input()
```

**3.**
```python
response = None
failsafe = 5
while response != '1' and response != '2' and failsafe > 0:
   print("Showing an image")
   response = input()
   failsafe -= 1
```
