class Car(object):

   def __init__(self, team: str, enginе: str,horse_pover: int, Tires_type: str, Tires_age_laps: int ):
       self.engine = enginе
       self.horse_pover = horse_pover
       self.Tires_age_laps  = Tires_age_laps
       self.Tires_type = Tires_type



    def getEngine(self) -> str:
        return self.engine

    def getHorse_pover(self) -> int:
        return self.horse_pover

    
    def getTires_type(self) -> str:
        return self.Tires_type


    def getTires_age_laps(self) -> int:
        return self.Tires_age_laps
