#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, visual, monitors, logging
#-import file save functions
#-(import other functions as necessary: os...)
import random

mon = monitors.Monitor('myMonitor', width=34.544, distance=60)
mon.setSizePix([2560,1664])
win = visual.Window(monitor=mon, size=(2924, 1224), color=[-1,-1,-1], units='pix', fullscr=True, useRetina=True)

refresh = 1.0/100.0

# create dropped frame detector
win.recordFrameIntervals = True #record frames
win.refreshThreshold = refresh + 0.004

# Set the log module to report warnings to the standard output window
#(default is errors only).
logging.console.setLevel(logging.WARNING)

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
n_trials = 10  # (per block)
n_blocks = 2
images = ['image01.jpg', 'image02.jpg', 'image03.jpg', 'image04.jpg', 'image05.jpg',
          'image06.jpg', 'image07.jpg', 'image08.jpg', 'image09.jpg', 'image10.jpg']

location = 'center'          # screen location where the image should appear
size = (200, 200)            # (x, y) pixels

duration = 2.0
image_frames = int(duration / refresh)

text_after_image = "wait for next image"
start_message = "Beginning experiment"
block_start_message = "Beginning new block"

# trial_loop_timer = core.CountdownTimer() # WAIT-Q4 #
# block_timer = core.Clock() # WAIT-Q4 #
# trial_timer = core.Clock() # WAIT-Q4 #

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist

# images are the only independent variable; we shuffle them at the start of
# each block below, so they'll be balanced
conditions = images

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
correct_responses = []        # list for correct responses (e.g., "on this trial, a response of X is correct")
participant_responses = []    # list for participant responses (e.g., "on this trial, response was a X")
response_accuracy = []        # list for response accuracy collection (e.g., "was participant correct?")
response_time = []            # list for response time collection
stimulus_identity_order = []  # list for recording the order of stimulus identities
stimulus_property_order = []  # list for recording the order of stimulus properties

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
for block_i in range(n_blocks):
    # block_timer.reset() # WAIT-Q4 #
    # block_start_time = 0 # WAIT-Q4 #

    #-present block start message
    random.shuffle(conditions)
    #-reset response time clock here

    #=====================
    #TRIAL SEQUENCE
    #=====================
    for trial_i in range(n_trials):
        # trial_timer.reset() # WAIT-Q4 #
        # trial_start_time = 0 # WAIT-Q4 #

        trial_image = visual.ImageStim(win, image=conditions[trial_i], units='pix', size=400)
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses

        #=====================
        #START TRIAL
        #=====================
        for frame_n in range(image_frames):

        # trial_loop_timer.reset() # WAIT-Q4 #
        # trial_loop_timer.add(2) # WAIT-Q4 #
        # while trial_loop_timer > 0: # WAIT-Q4 #
            trial_image.draw()
            win.flip()

        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...

        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial

        # trial_end_time = trial_timer.getTime() # WAIT-Q4 #

    print('Overall, %i frames were dropped.' % win.nDroppedFrames)

    # block_end_time = block_timer.getTime() # WAIT-Q4 #

#======================
# END OF EXPERIMENT
#======================
#-write data to a file
win.close()
#-quit experiment
