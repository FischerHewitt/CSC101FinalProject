# data
# Transportation Class
# mode: bus, Light Rail, Heavy Rail
# City: New York City, Chicago, Seattle, San Fransisco, Los Angeles
# Energy: {'metric': 'electric', 'diesel', 'value': #, 'unit': 'kWh/mile, 'gal/mile'}
# Emissions: {'factor': #, 'unit': 'kgCO2/kWh', 'kgCO2/gal'}
# Passengers: {'avg on board': #(Average Passengers on Board),
#       'avg pass trip': #(Average Passenger trip Length in miles),
#       'avg daily riders': #(Average amount of riders per day)}
# dailymiles: #(The distance each mode travels per day in miles)
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
# ExOutput:[(mode:Bus, city:New York City, energy:{'metric': 'diesel', 'value': 0.3, 'unit': 'gal'},
#   emissions:{'factor': 10.16, 'unit': 'kg/gal'},
#   passengers:{'avg on board': 13.6, 'avg pass trip': 3.6, 'avg daily riders': 1166000.0},
#   dailymiles:313800.0)]
# How to do: access data file -> open("citytransit.txt")
# have a place to store all the objects -> empty list = []
# read all lines of the file -> readlines()
# go through each line -> while loop index starting at 1
#   while index < len(data)
# split the data into each different part -> .split(",")
# create an object -> transportations(mode, city, energy, emissions, passengers, dailymiles)
#   for dictionaries call appropriate functions
#   add to the list -> .append()
#   keep track of the index -> += 1
# close the file -> .close()
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

# Purpose: to take in a list of attributes from the data, and return a dictionary with the energy attributes
# Input: list[str|int]
# Output: dict[str,float]|dict[str,str]
# ExInput: ['New York City','Bus','diesel','0.3','gal','10.16','kg/gal','13.6','3.6','1166000','313800']
# ExOutput: {'metric': 'diesel', 'value': 0.3, 'unit': 'gal'}
# how to do: create a dictionary -> {}
# grab values 2,3,4 -> words[#]
# convert 3 to a float -> float(words[3])
def get_energy(words: list[str]) -> dict[str,float]|dict[str,str]:
    energy = {'metric': words[2], 'value': float(words[3]), 'unit': words[4]}
    return energy

# Purpose: to take in a list of attributes from the data, and return a dictionary with the emissions attributes
# Input: list[str|int]
# Output: dict[str,float]|dict[str,str]
# ExInput: ['New York City','Bus','diesel','0.3','gal','10.16','kg/gal','13.6','3.6','1166000','313800']
# ExOutput: {'factor': 10.16, 'unit': 'kg/gal'}
# how to do: create a dictionary -> {}
#   grab values 5,6 -> words[#]
#   convert 5 to a float -> float(words[5])
def get_emissions(words: list[str]) -> dict[str,float]|dict[str,str]:
    emissions = {'factor': float(words[5]), 'unit': words[6]}
    return emissions

# Purpose: to take in a list of attributes from the data, and return a dictionary with the passenger attributes
# Input: list[str|int]
# Output: dict[str,float]
# ExInput: ['New York City','Bus','diesel','0.3','gal','10.16','kg/gal','13.6','3.6','1166000','313800']
# ExOutput: {'avg on board': 13.6, 'avg pass trip': 3.6, 'avg daily riders': 1166000.0}
# how to do: create a dictionary -> {}
#   grab values 7,8,9 -> words[#]
#   convert all to a float -> float(words[#])
def get_passengers(words: list[str]) -> dict[str,float]:
    passengers = {'avg on board': float(words[7]), 'avg pass trip': float(words[8]),
                  'avg daily riders': float(words[9])}
    return passengers