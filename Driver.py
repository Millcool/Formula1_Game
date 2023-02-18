from Driver_Race_statistics import  Driver_race_statistics

class Driver(object):
    """Summary of class here.

       Longer class information....
       Longer class information....

       Attributes:
           likes_spam: A boolean indicating if we like SPAM or not.
           eggs: An integer count of the eggs we have laid.
       """
    def __init__(self, Driver_name : str, age: int, team: str):
        self.Driver_name = Driver_name
        self.Age = age
        self.team = team
        self.stats = Driver_race_statistics()


    def print_Driver_Profile(self):
        print(f"--------------{self.getName()} Profile--------------")
        print(f"Driver Name: {self.getName()}")
        print(f"Driver Age : {self.getAge()}")
        print(f"Driver Team: {self.getTeam()}")
        print()

    def printStats(self):
        return self.stats.print_Driver_Statistics(self.getName())


    def getAge(self):
        return self.Age


    def getName(self):
        return self.Driver_name


    def getTeam(self):
        return self.team
