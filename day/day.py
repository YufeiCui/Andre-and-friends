class Day(object):
    HOURS = 24
    MINUTES = 60
    SECONDS = 60


class ImproperTimeException(Exception, Day):
    """
    When the the value provided > 24 hours or > 60 minutes
    """
    def __init__(self, msg=None):
        if msg is None:
            msg = "There {} hours in a day, {} minutes in an hour, and {} seconds in a minute"\
                .format(self.HOURS, self.MINUTES, self.SECONDS)
        super(ImproperTimeException, self).__init__(msg)
