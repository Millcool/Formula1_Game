class Driver_race_statistics(object):
    """Summary of class here.

       Longer class information....
       Longer class information....

       Attributes:
           likes_spam: A boolean indicating if we like SPAM or not.
           eggs: An integer count of the eggs we have laid.
       """
    def __init__(self,
                 points: float = 0,
                 Wins: int = 0,
                 Podiums: int = 0,
                 DNF: int = 0,
                 Out_of_points: int = 0,
                 Races: int = 0):
        self.points = points
        self.wins = Wins
        self.podiums = Podiums
        self.dnf = DNF
        self.Out_of_points = Out_of_points
        self.races = Races

    def print_Driver_Statistics(self, Name: str):
        print(f"-----------------{Name} Race Statistics-----------------")
        print(f"Races: {self.races}")
        print(f"Wins: {self.wins}")
        print(f"Podiums: {self.podiums}")
        print(f"DNF:{self.dnf}")
        print(f"Races Out of points: {self.Out_of_points}")


    def getRaces(self):
        return self.print_Dri
    def getPoints(self):
        return self.points


    def getWins(self):
        return self.wins


    def getPodiums(self):
        return self.dnf


    def getDNF(self):
        return self.dnf


    def getOut_Of_Points(self):
        return self.Out_of_points
