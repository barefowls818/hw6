import numpy
from numpy import pi
from random import random
import math
from math import sin,cos

#set values factor of 10^8 off true values for code to be able to run
R = 7
r = .004
#N is number of trials to get average of randomized calculations...low so the code will run
N = 2
#hits is total number of scatter it took to escape the sun, summed across trials
hits = 0

for trials in range(N):
    theta = 0
    #offset x to account for initial value of rcos(0)
    x = r*cos(theta) - .004
    y = r*sin(theta)
    #range kinda lower than I'd like.. feel like some hits are missed.
    #but any higher would destroy program functionality..
    for n in range(0,20000000):
        theta = 2*pi*random()
        xnew =x + r*cos(theta)
        ynew =y + r*sin(theta)
        x = xnew
        y = ynew
        #added n=max condition in case we didnt reach a hit due to tiny probability
        #and massive range that bogs down processes
        if x >= R or y >= R or n == 20000000:
        #tally up the scatters..
            hitsnew = hits + n
            hits = hitsnew
            break
    #average scatters per sun escape
    avgscatters = hits/N
#divide scatter # by time each scatter takes: 1.33*10^-11 seconds
timeseconds = avgscatters*1.33*10**-11
print('The time for a photon to escape a sun of radius R=7m is approximately')
print(timeseconds)
print('seconds')
#I kept N relatively small here and just ran it many times to get my own average value
#which is used in the rough estimations below.

#when run with R = .07, .7, 7, it seems as though the time will scale as R^2
#so it is my approximation that R = 7(10)^8 will give a time of 
#(7*10^-5)(10^16)s. This comes out to about 27000 years. 
#With the large potential error of this approach, this could put the real value
#anywhere from 10k to 100k. "real" not meaning physical reality, because even without the 
#code this is a very rudimentary idea of the scattering process. Instead "real" meaning
#the proper answer for this coding problem.
print('using this code I estimate that when using the full R=7(10)^8 meters, the time will be around 50000 years')
