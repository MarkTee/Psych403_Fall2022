# Psych403_Fall2022 - Assignment 5 - Mark Thomas

[Level 3 Exercises](https://kerblooee.github.io/pytutorial/level3_exercises.html)

## Experiment Structure Exercises
Please see [experiment.py](experiment.py)

## Import Exercises
**1.**
```python
#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event
import json  # we can save results to .json files
import os
```

## Directory Exercises
1.
```python
n_pics = 10
# create list of images using a list comprehension and format string
pics = [f'image{i:02}.jpg' for i in range(1, n_pics + 1)]
```

2.
```python
import os

# store names of images in 'images' dir in set for efficiency
images = set(os.listdir('images'))

# iterate over pics list
for pic in pics:
    if pic in images:
      print(pic, "was found!")
    else:  # raise an exception if the image wasn't found
      raise Exception(pic, "was not found!")
```

3.
```python
#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
image_dir = os.path.join(main_dir,'images')

# raise an exception if any directories don't exist
if not os.path.isdir(main_dir):
    raise Exception(main_dir, "not found!")
if not os.path.isdir(data_dir):
    raise Exception(data_dir, "not found!")
if not os.path.isdir(image_dir):
    raise Exception(image_dir, "not found!")

#=====================
#PREPARE CONDITION LISTS
#=====================
# store names of images in 'images' dir in set for efficiency
images = set(os.listdir(image_dir))

# check if files to be used during the experiment (e.g., images) exist
n_pics = 10
pics = [f'image{i:02}.jpg' for i in range(1, n_pics + 1)]

# iterate over pics list
for pic in pics:
    if pic not in images:
      # raise an exception if the image wasn't found
      raise Exception(pic, "was not found!")
