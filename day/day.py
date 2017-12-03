from activities.activities import Length


class Day(object):
    DAY = Length(24, 60)


class ImproperTimeException(Exception, Day):
    """
    When the the value provided > 24 hours or > 60 minutes
    """
    def __init__(self, msg=None):
        if msg is None:
            msg = "There {} hours in a day and {} minutes in an hour"\
                .format(self.DAY.hour, self.DAY.minute)
        super(ImproperTimeException, self).__init__(msg)
