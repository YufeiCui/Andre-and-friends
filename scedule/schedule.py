from day.day import *


class Schedule(object):
    HOURS = Day.HOURS

    def __init__(self, start=9, work=8) -> None:

        if start > self.HOURS:
            raise ImproperTimeException
        else:
            self._start = start
            self._work = work

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, time):
        self._start = time

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, time):
        self._work = time

    @property
    def finish(self):
        return self._start + self._work - (self.HOURS * ((self._start + self._work) // self.HOURS))

    def create_schedule(self) -> str:
        pass

    def __repr__(self) -> str:
        return "Start today's work at {}, will work for {} hours and finish at {}" \
            .format(self.start, self.work, self.finish)


A = Schedule(start=25, work=10)
print(A)
