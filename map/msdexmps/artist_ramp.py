

"""
    A map-reduce that calculates the average slow build
    for each artist
"""

from mrjob.job import MRJob
import track

import unicodedata

# if YIELD_ALL is true, we yield all densities, otherwise,
# we yield just the extremes

YIELD_ALL = False

class MRRamp(MRJob):
    """ A  map-reduce job that calculates the ramp factor """

    def mapper(self, _, line):
        """ The mapper loads a track and yields its ramp factor """
        t = track.load_track(line)
        if t and t['duration'] > 60 and len(t['segments']) > 20:
            segments = t['segments']
            half_track = t['duration'] / 2
            first_half = 0
            second_half = 0
            first_count = 0
            second_count = 0

            xdata = []
            ydata = []
            for i in range(len(segments)):
                seg = segments[i]

                # bail out if we have a really long quiet segment
                # these are usually surprise hidden tracks

                if seg['loudness_max'] < -40 and seg['duration'] > 30:
                    return

                seg_loudness = seg['loudness_max'] * seg['duration']

                if seg['start'] + seg['duration'] <= half_track:
                    seg_loudness = seg['loudness_max'] * seg['duration']
                    first_half += seg_loudness
                    first_count += 1
                elif seg['start'] < half_track and seg['start'] + seg['duration'] > half_track:
                    # this is the nasty segment that spans the song midpoint.
                    # apportion the loudness appropriately
                    first_seg_loudness = seg['loudness_max'] * (half_track - seg['start'])
                    first_half += first_seg_loudness
                    first_count += 1

                    second_seg_loudness = seg['loudness_max'] * (seg['duration'] - (half_track - seg['start']))
                    second_half += second_seg_loudness
                    second_count += 1
                else:
                    seg_loudness = seg['loudness_max'] * seg['duration']
                    second_half += seg_loudness
                    second_count += 1

                xdata.append( seg['start'] )
                ydata.append( seg['loudness_max'] )

            # only yield data if we've had sufficient segments in the first
            # and second half of the track. (This is to avoid the proverbial
            # hidden tracks that have extreme amounts of leading or tailing
            # silene

            correlation = pearsonr(xdata, ydata)
            ramp_factor = second_half / half_track - first_half / half_track
            score = correlation * ramp_factor
            yield (t['artist_id'], t['artist_name']), (score, t['track_id'])

    def reducer(self, key, val):
        count = 0
        sum = 0
        best = -60
        best_id = None

        for score, trid in val:
            sum += score
            count += 1
            if score > best:
                best = score
                best_id = trid
        avg = sum / count

        if count > 5 and avg > 5:
            yield key,  (avg, count, best, best_id)


def pearsonr(x, y):
  # Assume len(x) == len(y)
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum([pow(x, 2) for x in x])
    sum_y_sq = sum([pow(x, 2) for x in y])
    psum = sum(map(lambda x, y: x * y, x, y))
    num = psum - (sum_x * sum_y/n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
    if den == 0: 
        return 0
    return num / den


if __name__ == '__main__':
    MRRamp.run()
