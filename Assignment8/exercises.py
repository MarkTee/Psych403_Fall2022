import csv
import json as json

from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=1
nTrials=1
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
resp_time = [[0]*nTrials]*nBlocks
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

results = [] # for csv exercises, define dict at experiment level
for block in range(nBlocks):
    # trial will be our dictionary's keys
    # results = {}  # for recording data exercises, define dict at block level
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob = prob_sol[np.random.choice(4)]
        corr_resp = prob[1]

        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial

        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp == str(corr_resp):
            sub_acc = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings
        elif sub_resp != str(corr_resp):
            sub_acc = 2 #arbitrary number for inaccurate response
                                    #(should be something other than 0 to distinguish
                                    #from non-responses)


        # for data recording exercises:
        # results[trial] = {'sub_resp': sub_resp, 'resp_time': resp_time,
        #                   'sub_acc': sub_acc, 'corr_resp': corr_resp}
        # print('problem=', prob, 'correct response=',
        #       corr_resp, 'subject response=',sub_resp,
        #       'subject accuracy=',sub_acc)

        # for csv exercises:
        results.append({'block': block, 'trial': trial,
                        'problem': prob,
                       'sub_resp': sub_resp, 'resp_time': resp_time,
                       'sub_acc': sub_acc, 'corr_resp': corr_resp})

with open('saved_csv.csv', 'w') as f:
    # # save csv
    # fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time']
    # data_writer = csv.DictWriter(f, fieldnames=fieldnames)
    # data_writer.writeheader()
    # for result in results:
    #     print(result)
    #     data_writer.writerow(result)

    # save json
    with open('saved_json.json', 'w') as f:
        json.dump(results, f)

win.close()
