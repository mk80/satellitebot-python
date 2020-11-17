import sys
import os
import numpy as np

pwd = os.getcwd()

#using numpy arrary to build member list
#   -name   -gps    -satellite list
members = pwd + '\\members.npy'
satellites = pwd + '\\satellite.list'

#load members for accessability
memberData = np.load(members)

def addMember(name, locGPS, sateHolder):
    with open(members, '') as f:
        f.write(name + '\n')
    return(name)

def listSats():
    with open(satellites, 'r') as f:
        return(f.read())

def addSatToMember():
    pass