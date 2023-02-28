class Team(object):
    """Summary of class here.

       Longer class information....
       Longer class information....

       Attributes:
           likes_spam: A boolean indicating if we like SPAM or not.
           eggs: An integer count of the eggs we have laid.
       """

    def __init__(self, team_principal: str, team_budget: int = 0):
        self.team_budget = team_budget
        self.team_principal = team_principal

    def get_team_principal(self):
        return self.team_principal

    def get_team_budget(self):
        return self.team_budget


