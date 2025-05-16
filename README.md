# Scheduler_V2
Need to update the code for the scheduler as apparently anaconda was using a version of tkinter 
that was both outdated and obsolete. 

# Reason for remaking 
For one, anaconda had a lot of outdated packages and was messing with my python. So instead of
relying on anaconda like this I decided to instead delete anaconda and just slowly make my way back
to what the scheduler was in the first version. 

The main differences being that events seem to be recognized differently, there are many outdated
methods in the old version that did not perform as expected, so I am hoping they are now fixed. In
addition I would like to rework how the scheduelr saves and uploads data: I will be using MySQL, or
at least the brew version of it, and aim to connect it to a global data base on a PI later. 
