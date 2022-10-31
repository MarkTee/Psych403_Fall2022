#=====================
#IMPORT MODULES
#=====================
import numpy as np
#-import psychopy functions
#-import file save functions
#-(import other functions as necessary: os...)
import random

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
duration = 1                 # seconds
fixation_cross_duration = 1  # seconds
text_after_image = "wait for next image"
start_message = "Beginning experiment"
block_start_message = "Beginning new block"

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
for block_i in n_blocks:
    #-present block start message
    random.shuffle(conditions)
    #-reset response time clock here

    #=====================
    #TRIAL SEQUENCE
    #=====================
    for trial_i in n_trials:
        ...
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses

        #=====================
        #START TRIAL
        #=====================
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...

        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial

#======================
# END OF EXPERIMENT
#======================
#-write data to a file
#-close window
#-quit experiment
