from typing import List

class ConversionService():
    def convert_mg_to_grams(mg:float = 1) -> float:
        return mg/1000

    def convert_grams_to_kg(grams:float = 1) -> float:
        return grams/1000

    def convert_grams_to_lbs(grams:float = 1) -> float:
        return grams * 0.0022046

    def convert_grams_to_oz(grams:float = 1) -> float:
        return grams *  0.035274

class Medication(ConversionService):
    name:str = ""
    mg:float = 0.0
    g:float = 0.0
    kg:float = 0.0
    oz:float = 0.0
    lbs:float = 0.0

    def __init__(self,mg:float, name:str) -> None:
        super().__init__()
        self.mg = mg
        self.g = self.convert_mg_to_grams(self.mg)
        self.kg = self.convert_grams_to_kg(self.g)
        self.oz = self.convert_grams_to_oz(self.g)
        self.lbs = self.convert_grams_to_lbs(self.g)

class MedicationBox():
    medications: List[Medication]
    name:str = ""
    mg:float = 0.0
    g:float = 0.0
    kg:float = 0.0
    oz:float = 0.0
    lbs:float = 0.0

    def add(self,medication: Medication):
        self.medications.append(medication)
        self._process_weight()

    def _process_weight(self) -> float:
        self.mg = 0
        self.g = 0
        self.kg = 0
        self.lbs = 0
        self.oz = 0
        for med in self.medications:
            self.g = self.g + med.g
            self.mg = self.mg + self.mg
            self.kg = self.kg + self.kg
            self.lbs = self.lbs + self.lbs
            self.oz = self.oz + self.oz

