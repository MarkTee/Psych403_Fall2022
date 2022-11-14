# Psych403_Fall2022 - Assignment 6 - Mark Thomas

[Level 4 Exercises](https://kerblooee.github.io/pytutorial/level4_exercises.html)


## Dialog Box Exercises
```python
from psychopy import gui

exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender': '', 'session': 1}

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title="subject info",
                         fixed='session', 
                         order=['session', 'subject_nr', 'age', 'gender', 
                                'handedness'],
                         show=False)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg.show()
```

**"Set the variable "session" as fixed. What happens?"**  
The user is no longer able to adjust the value for session in the dialog box.


**Fill in the following pseudocode with the real code you have learned so far:**
```python
from psychopy import gui
from datetime import datetime

#=====================
#COLLECT PARTICIPANT INFO
#=====================
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'),
            'gender': '', 'session': 1}

#-create a dialogue box that will collect current participant number, age, gender, handedness
my_dlg = gui.DlgFromDict(dictionary=exp_info,
                         title="subject info",
                         fixed='session',
                         order=['session', 'subject_nr', 'age', 'gender',
                                'handedness'])

#get date and time
date = datetime.now()

#-create a unique filename for the data
exp_info['date'] = f"{date.day}/{date.month}/{date.year}"
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
```


## Monitor and Window Exercises

**How does changing "units" affect how you define your window size?**  
Units defines the default units of stimuli drawn in the window, and can be set to None, 'height', 'norm' (normalised), 'deg', 'cm', or 'px'. The options can be either dynamic or fixed, and the way we define our window size depends on the context ([as described in the documentation here](https://psychopy.org/general/units.html#units)). e.g. if we choose 'cm', then stimuli will be of fixed sizes, and specified by number of cm.

**How does changing colorSpace affect how you define the color of your window? Can you define colors by name?**
colorSpace affects the name of the color space currently being used (RGB, DKL, and LMS.) Yes, you can define colors by name. e.g. "stim.setColor('Firebrick')". [More information can be found in the documentation here.](https://psychopy.org/general/colours.html#colorspaces)


**Fill in the following pseudocode with the real code you have learned so far:**
```python
from psychopy import visual, monitors
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units='None', fullscr=False, useRetina=True)
# Note: I had to specify "useRetina=True" to get my monitor working
```


## Stimulus Exercises
**Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?**
This will resize the images to the specified size. To keep the proper image dimensions, we can set "units" to "pix" when calling ImageStim, which will scale the image appropriately.

```python
from psychopy import visual, monitors, event
import os

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)

mon.setSizePix([2560,1664])

win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units='pix', fullscr=False, useRetina=True)

main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')

for i in range(10):
    pic_loc = os.path.join(image_dir,'face' + str(i) + '.jpg') #point to the specific image

    my_image = visual.ImageStim(win, image=pic_loc, units='height', size=400)
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()
```


**Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode).**
```python
from psychopy import visual, monitors, event
import os

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)

mon.setSizePix([2560,1664])

win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')

corners = [(200, 200), (-200, 200), (-200, -200), (200, -200)]

corner_i = 0
for i in range(10):
    pic_loc = os.path.join(image_dir,'face' + str(i) + '.jpg') #point to the specific image

    my_image = visual.ImageStim(win, pos=corners[corner_i], image=pic_loc, units='pix', size=400)
    my_image.draw()
    win.flip()
    event.waitKeys()

    corner_i += 1
    if corner_i == 4:
        corner_i = 0
win.close()
```


**Create a fixation cross stimulus.**  
fix_text = visual.TextStim(win, text='+')

example use:
```python
from psychopy import visual, monitors, event
import os

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)

mon.setSizePix([2560,1664])

win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units='pix', fullscr=False, useRetina=True)

fix_text = visual.TextStim(win, text='+')

fix_text.draw() #draw fixation at the same time
win.flip()
event.waitKeys()

win.close()
```

**Fill in the following pseudocode with the real code you have learned so far:**
```python
from psychopy import visual, monitors, event
import random

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)

mon.setSizePix([2560,1664])

win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units='pix', fullscr=False, useRetina=True)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
n_trials = 10  # (per block)
n_blocks = 2
images = ['image01.jpg', 'image02.jpg', 'image03.jpg', 'image04.jpg', 'image05.jpg',
          'image06.jpg', 'image07.jpg', 'image08.jpg', 'image09.jpg', 'image10.jpg']
location = 'center'          # screen location where the image should appear
size = (200, 200)            # (x, y) pixels
duration = 1                 # seconds
fixation_cross_duration = 1  # seconds
text_after_image = "wait for next image"
conditions = images

start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
my_text = visual.TextStim(win)

#=====================
#START EXPERIMENT
#=====================
my_text.text = start_msg
my_text.draw()
win.flip()
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
for block in range(n_blocks):
    my_text.text = block_msg
    my_text.draw()
    win.flip()
    event.waitKeys()
    random.shuffle(conditions)

    #=====================
    #TRIAL SEQUENCE
    #=====================
    for trial in range(n_trials):
        my_image = visual.ImageStim(conditions[trial], units='height', size=400)

        #=====================
        #START TRIAL
        #=====================
        fix_text.draw()
        win.flip()
        #? -wait time (stimulus duration)


        my_image.draw()
        win.flip()
        #? -wait time (stimulus duration)

        my_text.text = end_trial_msg
        win.flip()
        #? -wait time (stimulus duration)

#======================
# END OF EXPERIMENT
#======================
win.close()
```
