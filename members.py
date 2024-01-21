import sys
import os
import sqlite3

pwd = os.getcwd()

# build member list
#   -name   -gps    -schedule   -satellite list
#db_conn = sqlite3.connect("members.db")
#db_cur = db_conn.cursor()

satellites = pwd + '\\satellite.list'


def addMember(name, locGPS, schedule, sateHolder):
    db_conn = sqlite3.connect("member.db")
    db_cur = db_conn.cursor()

    result = db_cur.execute("UPSERT ...")
    db_conn.commit()

    db_conn.close()


def listSats():
    with open(satellites, 'r') as f:
        return(f.read())

def addSatToMember(satellite):
    db_conn = sqlite3.connect("member.db")
    db_cur = db_conn.cursor()
    pass

def updateLocation(locGPS):
    db_conn = sqlite3.connect("member.db")
    db_cur = db_conn.cursor()
    pass
