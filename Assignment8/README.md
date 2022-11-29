# Psych403_Fall2022 - Assignment 8 - Mark Thomas

[Level 6 Exercises](https://kerblooee.github.io/pytutorial/level6_exercises.html)


## PsychoPy keypress exercises
**1.**
```python
keys = event.getKeys()
if keys:
    response = keys[0] # only store the first pressed key
```

**2.** **What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop?**

Any keys that have been pressed before event.ClearEvents() is called will be flushed and key collection effectively restarts. This means that if we call the function within the trial loop, the keys will be cleared every trial (so key collection is effectively restarted). If we call the function outside of the trial loop, the keys will never be cleared, so ALL of the keys that are pressed at any time after the first trial will be stored.

**What happens if you unindent the "if keys:" line?**

Only the time of the last trial's keypress will be printed. 


## Psychtoolbox keypress exercises
N/A


## Recording data exercises

**1. and 2.** Please see [exercises.py](exercises.py).


## Save csv exercises

**1.** Please see [exercises.py](exercises.py).


## Save JSON exercises

**1.** Please see [exercises.py](exercises.py).


## Read JSON exercises

**1. and 2. and 3.** Please see [read_and_analysis.py](read_and_analysis.py).
