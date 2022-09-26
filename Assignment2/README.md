# Psych403_Fall2022 - Assignment 2 - Mark Thomas

[Level 0 - Exercises](https://kylemath.github.io/pytutorial/level0_exercises.html)

## Print Exercises

1. Please see `yourname.py`

2. No, variables don't show up in the Variable Editor (since we didn't use variables in this script).


## Operation Exercises

1. Yes, Python outputs the same value for these (I'm using Python 3.9.5).

2. The modulo operator gives the remainder after dividing the first argument by the second argument.

3. ** is the exponent operator; it raises a number to the power of another. // is the floor division operator; it essentially divides one number by another and rounds the quotient down to the nearest integer.

4. [Yes, Python follows order of operations.](https://docs.python.org/3/reference/expressions.html#operator-precedence)


## Variable Exercises

1. Please see `yourname.py`

2. Yes, a variable (for each letter of my name) shows up in the Variable Editor.

3. No, Python doesn't have a problem with two different variables having the same value; it prints both properly.

4. N/A

5. No, changing the value of letterX didn't change the value of the other variables.

6. No, changing the value of letter1 didn't change the value of letterX. This shows that, for mutable types, Python is storing the underlying value itself rather than a reference to it. For integers like this, we can redefine variables without changing the value of other variables.


## Boolean Exercises

1. Yes, 1 and 1.0 are equivalent since they're both numeric types. No, "1" and "1.0" aren't equivalent, since they're strings with a different number of characters

2. Yes, 5 and (3+2) are equivalent (since Python evaluates the expression inside the brackets and gets 5).

3. 1. (1 == 1.0) or ('1' == '1.0') or (5 == (3+2))
   2. (1 == 1.0) and not ('1' == '1.0') and (5 == (3+2))
   3. (1 == 1.0) and not ('1' == '1.0') or (5 == (3+2))
   4. (1 == 1.0) or ('1' == '1.0') and (5 == (3+2))
   5. (1 == 1.0) and not ('1' == '1.0') or (5 == (3+2))


## List Exercises

1. `oddlist = [1, 3, 5, 7, 9]` Yes, oddlist became a variable.

2. oddlist prints properly. Output: [1, 3, 5, 7, 9]

3. Python says the list has a length of 5.

4. Python says oddlist is a list.

5. `intlist = list(range(0, 101))`

6. Yes, it prints all integers between 0 and 100.


## Dictionary Exercises

1. `about_me = {'name': 'Mark', 'age': 99.0, 'year_of_study': 4, 'favorite_foods': ['pizza', 'steak', 'burgers']}`

2. I confirmed that about_me prints properly and that the type function returned dict.

3. Python says about_me has a length of 4. Python bases the length of a dict on the number of keys that it contains.


## Array Exercises

1. `mixnums = np.array([1, 2, 3, 4.0, 5.0, 6.0])` Python converts the integers to floats.

2. `mixtypes = [1, 2, 3.0, 4.0, '5', '6']` The array's values remain unchanged; Python leaves arrays with mixed types as they are.

3. `oddarray = np.arange(1, 101, 2)`

4. `logarray = np.logspace(1,5,16)`
