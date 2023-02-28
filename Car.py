class Car(object):

    def __init__(self, team: str, enginе: str, horse_pover: int, tires_type: str, tires_age_laps: int):
        self.engine = enginе
        self.horse_pover = horse_pover
        self.Tires_age_laps = tires_age_laps
        self.Tires_type = tires_type

    def get_engine(self) -> str:
        return self.engine

    def get_horse_pover(self) -> int:
        return self.horse_pover

    def get_tires_type(self) -> str:
        return self.Tires_type

    def get_tires_age_laps(self) -> int:
        return self.Tires_age_laps
