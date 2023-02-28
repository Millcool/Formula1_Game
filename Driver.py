from Driver_Race_statistics import Driver_race_statistics


class Driver(object):
    #TODO ILYA write Drivar class description
    """Summary of class here.

       Longer class information....
       Longer class information....

       Attributes:
           likes_spam: A boolean indicating if we like SPAM or not.
           eggs: An integer count of the eggs we have laid.
       """

    def __init__(self, driver_name: str, age: int, team: str):
        self.Driver_name = driver_name
        self.Age = age
        self.team = team
        self.stats = Driver_race_statistics()

    def print_driver_profile(self):
        print(f"--------------{self.get_name()} Profile--------------")
        print(f"Driver Name: {self.get_name()}")
        print(f"Driver Age : {self.get_age()}")
        print(f"Driver Team: {self.get_team()}")
        print()

    def print_stats(self):
        return self.stats.print_Driver_Statistics(self.get_name())

    def get_age(self):
        return self.Age

    def get_name(self):
        return self.Driver_name

    def get_team(self):
        return self.team
