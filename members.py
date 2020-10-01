import sys
import os

pwd = os.getcwd()

members = pwd + '\\members.list'
satellites = pwd + '\\satellites.list'

def addMember(name):
    with open(members, 'a') as f:
        f.write(name + '\n')
    return(name)

def listSats():
    with open(satellites, 'r') as f:
        return(f.read())

def addSatToMember():
    pass