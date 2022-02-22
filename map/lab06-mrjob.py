# Python

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from msdexmps import track
import math 
# import json

class MyMrJob(MRJob):
    OUTPUT_PROTOCOL = JSONValueProtocol
    def mapper(self, _, line):
        t = track.load_track(line)
        if not math.isnan(t['artist_latitude']) \
            and not math.isnan(t['artist_longitude']):
            lng = t['artist_longitude']
            lat = t['artist_latitude']
            yield t['artist_id'], {'aid': t['artist_id'], 'aname': t['artist_name'], 'lnglat': [lng, lat]}

    def reducer(self, key, lval):
        listitems = list(lval)
        for i in listitems:
            songcount = len(listitems)
            pregeojson = {"type": "Feature", "geometry": {"type": "Point", "coordinates": i['lnglat']}, "properties": {"Artist": i['aname'], "Songs": songcount, "A_ID": i['aid']}}
        yield None, pregeojson

if __name__ == '__main__':
    MyMrJob.run()
