class Race_track(object):
    """Summary of class here.

       Longer class information....
       Longer class information....

       Attributes:
           likes_spam: A boolean indicating if we like SPAM or not.
           eggs: An integer count of the eggs we have laid.
       """

    def __init__(self, track_name: str, length: float, track_stats):
        self.track_stats = track_stats
        self.track_length = length
        self.track_name = track_name

    def get_track_stats(self):
        return self.track_stats

    def get_track_name(self):
        return self.track_name

    def get_length(self):
        return self.track_length
