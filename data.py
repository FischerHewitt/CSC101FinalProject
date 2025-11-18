# data
# Transportation Class
# mode: bus, Light Rail, Heavy Rail
# City: New York City, Chicago, Seattle, San Fransisco, Los Angeles
# Energy: {'metric': 'electric', 'diesel', 'value': #, 'unit': 'kWh, 'kg/gal'}
# Emissions: {'factor': #, 'unit': 'kWh, 'kg/gal'}
# Passengers: {'avg on board': #(Average Passengers on Board),
#       'avg pass trip': #(Average Passenger trip Length in miles),
#       'avg daily riders': #(Average amount of riders per day)}
# dailymiles: #The distance each mode travels per day in miles
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

    def __repr__(self):
        return "(mode:{}, city:{}, energy:{}, emissions:{}, passengers:{}, dailymiles:{})\n".format(
            self.mode, self.city, self.energy, self.emissions, self.passengers, self.dailymiles
        )

    def __eq__(self, other):
        return (self == other) or ((self.mode == other.mode)
                                   and (self.city == other.city)
                                   and (self.energy == other.energy)
                                    and (self.emissions == other.emissions)
                                    and (self.passengers == other.passengers)
                                   and (self.dailymiles == other.dailymiles))

# Purpose: to get data from the file, and create a list of objects [transportations]
# Input: None
# Output: list[Transportations]
# ExInput: None
# ExOutput:
# How to do:
def get_data() -> list[Transportations]:
    transitFile = open("citytransit.txt","r")
    transportations = []
    each_data_line = transitFile.readlines()
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

print(get_data())