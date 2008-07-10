# Written by Nick Welch in the years 2005-2008.  Author disclaims copyright.

from whimsy.x11.replay import replay_or_swallow

class smart_replay(object):
    def __init__(self):
        self.replayed = []
    def __call__(self, signal):
        key = (signal.ev.time, signal.ev.sequence_number)
        if key not in self.replayed:
            replay_or_swallow(signal.wm.dpy, signal.ev, not hasattr(signal.ev, 'swallow'))

            self.replayed.append(key)
            if len(self.replayed) > 100:
                self.replayed.pop(0)

