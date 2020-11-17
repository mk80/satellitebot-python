from skyfield.api import Topos, load, EarthSatellite
from datetime import datetime
from pytz import timezone

def getSatelliteVisable(satelliteName):
    #stations_url = 'http://celestrak.com/NORAD/elements/amateur.txt'
    stations_url = 'https://www.amsat.org/tle/current/nasabare.txt'
    satellites = load.tle_file(stations_url)
    #print('Loaded', len(satellites), 'satellites')

    ts = load.timescale()

    # San Diego
    home = Topos('32.48 N', '117.22 W')

    today = datetime.today()

    # timeframe to search for passes
    plus_time = 2
    t0 = ts.utc(today.year, today.month, today.day, today.hour)
    t1 = ts.utc(today.year, today.month, today.day + plus_time)


    # get visible time for requested satellite
    by_name = {sat.name: sat for sat in satellites}
    satellite = by_name[satelliteName]

    t, events = satellite.find_events(home, t0, t1, altitude_degrees=10.0)
    for ti, event in zip(t, events):
            name = ('rise above 10°', 'culminate', 'set below 10°')[event]
            print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
