import sys
import os
import sqlite3

pwd = os.getcwd()

# build member list
#   -name   -gps    -satellite list
db_conn = sqlite3.connect("members.db")
db_cur = db_conn.cursor()

satellites = pwd + '\\satellite.list'


def addMember(name, locGPS, sateHolder):
    pass

def listSats():
    with open(satellites, 'r') as f:
        return(f.read())

def addSatToMember():
    pass
