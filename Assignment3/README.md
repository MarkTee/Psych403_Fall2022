# Psych403_Fall2022 - Assignment 3 - Mark Thomas

[Level 1 Exercises](https://kylemath.github.io/pytutorial/level1_exercises.html)

## Variable Operations Exercises

1. `sub_code = 'sub'`  
   `subnr_int = 2`  
   `subnr_str = "2"`

   We should add `subnr_str` to `sub_code` to create the output "sub2". `subnr_int` isn't valid since it's an integer (`sub_code` is a string; in Python it's not valid to add an integer and a string)

2. `sub_code + ' ' + subnr_str`  
   `sub_code + ' ' + subnr_str * 3`  
   `(sub_code + subnr_str) * 3`  
   `sub_code * 3 + subnr_str * 3`


## List Operations Exercises

1. `numlist = [1, 2, 3] * 2`

2. `numarr = np.array([1,2,3]) * 2`  
   Multiplying a list by some scalar n repeats the list n times. Multiplying an array by n performs (elementwise) scalar multiplication.

3. `strlist = ['do','re','mi','fa']`

   `[strlist[0] * 2, strlist[1] * 2, strlist[2] * 2, strlist[3] * 2]`  
   `strlist * 2`  
   `[strlist[0], strlist[0], strlist[1], strlist[1], strlist[2], strlist[2], strlist[3], strlist[3]]`  
   `[[strlist[0], strlist[0]], [strlist[1], strlist[1]], [strlist[2], strlist[2]], [strlist[3], strlist[3]]`  


## Zipping Exercises

```python
faces = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
houses = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5

faces_i = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
houses_i = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5

cues = [1] * 50 + [2] * 50

combs = list(zip((faces + houses) * 2, 
                 (faces_i + houses_i) * 2, 
                 cues))
np.random.shuffle(combs)
```


## Indexing Exercises

1. `colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']`  
2. `print(colors[-2])`  
3. `print(colors[-2][2], colors[-2][3])`  
4. `colors.remove(colors[-1])`  
   `colors.insert(len(colors), 'indigo')`  
   `colors.insert(len(colors), 'violet')`


## Slicing Exercises

1. `list100 = list(range(101))`
2. `print(list100[:10])`
3. `print(list100[99::-2])`
4. `print(list100[:-5:-1])`
5. `print(list100[39:44] == [39, 40, 41, 42, 43])`   
   Yes, the numbers/integers are equal.
