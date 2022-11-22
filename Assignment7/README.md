# Psych403_Fall2022 - Assignment 7 - Mark Thomas

[Level 4 Exercises](https://kerblooee.github.io/pytutorial/level5_exercises.html)


Image sources:
- https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg



## Wait Exercises
**1.**
```python
from psychopy import core, visual, monitors

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])
win = visual.Window(monitor=mon, size=(2924, 1224), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

duration = 2

start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win, image='my_image.png', units='pix', size=400)
my_text = visual.TextStim(win)

#=====================
#START TRIAL
#===================== 
fix_text.draw()
win.flip()
core.wait(duration)

my_image.draw()
win.flip()
core.wait(duration)

my_text.text = end_trial_msg
win.flip()
core.wait(duration)
```



## Clock Exercises
**1.**
```python
from psychopy import core, visual, monitors

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])
win = visual.Window(monitor=mon, size=(2924, 1224), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

wait_timer = core.Clock()

duration = 2  # seconds

start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win, image='my_image.png', units='pix', size=400)
my_text = visual.TextStim(win)
#=====================
#START TRIAL
#=====================
fix_text.draw()
win.flip()
start = wait_timer.getTime()
core.wait(duration)
end = wait_timer.getTime()
print("Actual elapsed time:", end - start)

my_image.draw()
win.flip()
start = wait_timer.getTime()
core.wait(duration)
end = wait_timer.getTime()
print("Actual elapsed time:", end - start)

my_text.text = end_trial_msg
my_text.draw()
win.flip()
start = wait_timer.getTime()
core.wait(duration)
end = wait_timer.getTime()
print("Actual elapsed time:", end - start)
```

**How precise?**  
  
core.wait(2) is fairly precise (at least to about 5 decimal places, based on these runs). The times I got were:  
- 2.001092540798709 seconds
- 2.0010974160395563 seconds
- 2.001099209068343 seconds


**2.**
```python
from psychopy import core, visual, monitors

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])
win = visual.Window(monitor=mon, size=(2924, 1224), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

clock_wait_timer = core.Clock()

duration = 2  # seconds

start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win, image='my_image.png', units='pix', size=400)
my_text = visual.TextStim(win)
#=====================
#START TRIAL
#=====================
clock_wait_timer.reset()
last_time = 0
while clock_wait_timer.getTime() <= 2:  # 2 seconds
    fix_text.draw()
    win.flip()
current_time = clock_wait_timer.getTime()
print("Actual elapsed time:", current_time - last_time)
last_time = current_time

while 2 < clock_wait_timer.getTime() <= 4:  # 4 seconds
    my_image.draw()
    win.flip()
current_time = clock_wait_timer.getTime()
print("Actual elapsed time:", current_time - last_time)
last_time = current_time

while 4 < clock_wait_timer.getTime() <= 6:  # 6 seconds
    my_text.text = end_trial_msg
    my_text.draw()
    win.flip()
current_time = clock_wait_timer.getTime()
print("Actual elapsed time:", current_time - last_time)
last_time = current_time
```

**How precise?**  
  
Using core.wait with while loops is somewhat less precise (there is more variance in wait times).The times I got were:  
- 2.0027510412037373 seconds
- 2.0010669589973986 seconds
- 2.000026957830414 seconds


**3.**
```python
from psychopy import core, visual, monitors

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])
win = visual.Window(monitor=mon, size=(2924, 1224), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

countdown_timer = core.CountdownTimer()

duration = 2  # seconds

start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win, image='Assignment7/my_image.png', units='pix', size=400)
my_text = visual.TextStim(win)
#=====================
#START TRIAL
#=====================
countdown_timer.reset()
countdown_timer.add(6)
last_time = countdown_timer.getTime()
while countdown_timer.getTime() >= 4:  # 2 seconds
    fix_text.draw()
    win.flip()
current_time = countdown_timer.getTime()
print("Actual elapsed time:", last_time - current_time)
last_time = current_time

last_time = countdown_timer.getTime()
while countdown_timer.getTime() >= 2:  # 2 seconds
    my_image.draw()
    win.flip()
current_time = countdown_timer.getTime()
print("Actual elapsed time:", last_time - current_time)
last_time = current_time

last_time = countdown_timer.getTime()
while countdown_timer.getTime() > 0:  # 2 seconds
    my_text.text = end_trial_msg
    my_text.draw()
    win.flip()
current_time = countdown_timer.getTime()
print("Actual elapsed time:", last_time - current_time)
last_time = current_time
```

**How precise?**  
  
Using core.wait with a countdown timer isn't that precise either (again, there is quite a bit of variance in wait times).The times I got were:  
- 2.0050285840407014 seconds
- 2.0009629169944674 seconds
- 2.000957665964961 seconds


**4.** Please see [experiment.py](experiment.py). The next question has us comment out the relevant lines so I added "# WAIT-Q4 #" to the end of each relevant line.



## Frame-Based Timing Exercises
**1.** Please see [experiment.py](experiment.py).

**2.** Please see [experiment.py](experiment.py). I only had 4 dropped frames, so I will keep frame-based timing in my experiment. 
