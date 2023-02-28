class Human:

     def __init__(self, age: int, name: str, nationality: str, height: int, gender: str):
         self.gender = gender
         self.height = height
         self.name = name
         self.nationality = nationality
         self.age = age

    def get_gender(self) -> str:
        return self.gender

    def get_height(self) -> int:
        return self.height






