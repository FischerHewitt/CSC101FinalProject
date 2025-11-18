# data
class Transportations:
    def __init__(self,
                 mode: str,
                 city: str,
                energy: dict[str,float]|dict[str,str],
                 emissions: dict[str,float]|dict[str,str],
                 passengers: dict[str,float],
                 dailymiles: float
                 ):
        self.mode = mode
        self.city = city
        self.energy = energy
        self.emissions = emissions
        self.passengers = passengers
        self.dailymiles = dailymiles

# Purpose: to get data from the file, and create a list of objects [transportations]
# Input: None
# Output: list[Transportations]
# ExInput: None
# ExOutput:
# How to do:
def get_data() -> list[Transportations]:
    transitFile = open("cities.txt","r")
    transportations = []
    each_data_line = transitFile.readline()
    index = 1
    while index < len(each_data_line):
        words = each_data_line[index].split(",")
        transportations.append(Transportations(words[1],
                               words[0],
                               get_energy(words),
                               get_emissions(words),
                               get_passengers(words),
                               float(words[10])))
        index = index + 1
    transitFile.close()
    return transportations

def get_energy(words: list[str]) -> dict[str,float]|dict[str,str]:
    energy = {'metric': words[2], 'value': float(words[3]), 'unit': words[4]}
    return energy

def get_emissions(words: list[str]) -> dict[str,float]|dict[str,str]:
    emissions = {'factor': float(words[5]), 'unit': words[6]}
    return emissions

def get_passengers(words: list[str]) -> dict[str,float]|dict[str,str]:
    passengers = {'avg on board': float(words[7]), 'avg pass trip': float(words[8]),
                  'avg daily riders': float(words[9])}
    return passengers
