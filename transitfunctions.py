from data import Transportations

# (kWh/mile) x (kgCO2/kWh) = (kgCO2/mile)
# (gal/mile) x (kgCO2/gal) = (kgCO2/mile)
# Purpose: to take in a transportation object, and return the kgco2 per mile as a float
# Input: Transportations object
# Output: Float
# ExInput: (mode:Bus, city:New York City, energy:{'metric': 'diesel', 'value': 0.3, 'unit': 'gal/mile'},
#   emissions:{'factor': 10.16, 'unit': 'kg/gal'},
#   passengers:{'avg on board': 13.6, 'avg pass trip': 3.6, 'avg daily riders': 1166000.0},
#   dailymiles:313800.0)
# ExOutput: 3.048
# how to do: access dictionaries -> .attribute['key']
#   multiply energy value by emissions factor -> .energy['value'] * .emissions['factor']
def get_co2_per_vehicle_mile(mode:Transportations) -> float:
    return mode.energy['value'] * mode.emissions['factor']

# (kgCO2/mile) x (1/passenger) = kgCO2 per passenger mile
# Purpose: to take in a transportation object, and return the kgco2 for every mile a passenger travels as a float
# Input: Transportations object
# Output: Float
# ExInput: (mode:Bus, city:New York City, energy:{'metric': 'diesel', 'value': 0.3, 'unit': 'gal/mile'},
#   emissions:{'factor': 10.16, 'unit': 'kg/gal'},
#   passengers:{'avg on board': 13.6, 'avg pass trip': 3.6, 'avg daily riders': 1166000.0},
#   dailymiles:313800.0)
# ExOutput: 0.22411764705882
def get_co2_per_passenger_mile(mode:Transportations) -> float:
    return get_co2_per_vehicle_mile(mode)/mode.passengers['avg on board']

# This Might be worthless
'''def sort_co2_per_vehicle_mile(lst_of_transport:list[Transportations]) -> list[Transportations]:
    sort_lst_of_cos_per_vehicle_mile = lst_of_transport
    for iterations in range(len(sort_lst_of_cos_per_vehicle_mile)-1):
        min_idx = iterations
        for idx in range(iterations, len(sort_lst_of_cos_per_vehicle_mile)):
            if (get_co2_per_vehicle_mile(sort_lst_of_cos_per_vehicle_mile[idx]) <
                    get_co2_per_vehicle_mile(sort_lst_of_cos_per_vehicle_mile[min_idx])):
                min_idx = idx
        if min_idx != iterations:
            temp = sort_lst_of_cos_per_vehicle_mile[min_idx]
            sort_lst_of_cos_per_vehicle_mile[min_idx] = sort_lst_of_cos_per_vehicle_mile[iterations]
            sort_lst_of_cos_per_vehicle_mile[iterations] = temp
    return sort_lst_of_cos_per_vehicle_mile'''

# This might be worthless
'''def sort_co2_per_passenger_mile(lst_of_transport1:list[Transportations]) -> list[Transportations]:
    sort_lst_of_cos_per_passenger_mile1 = lst_of_transport1
    for iterations in range(len(sort_lst_of_cos_per_passenger_mile1)-1):
        min_idx = iterations
        for idx in range(iterations, len(sort_lst_of_cos_per_passenger_mile1)):
            if (get_co2_per_passenger_mile(sort_lst_of_cos_per_passenger_mile1[idx]) <
                    get_co2_per_passenger_mile(sort_lst_of_cos_per_passenger_mile1[min_idx])):
                min_idx = idx
        if min_idx != iterations:
            temp = sort_lst_of_cos_per_passenger_mile1[min_idx]
            sort_lst_of_cos_per_passenger_mile1[min_idx] = sort_lst_of_cos_per_passenger_mile1[iterations]
            sort_lst_of_cos_per_passenger_mile1[iterations] = temp
    return sort_lst_of_cos_per_passenger_mile1'''

# Purpose: to take in a list of transportation objects, and return a dictionary
#   containing the city and the carbon emissions per day
# Input: list[Transportations]
# Output: dict[str, float]
# ExInput:
def get_city_co2_per_day(lst_of_transport2:list[Transportations]) -> dict[str, float]:
    dict_of_city_co2_per_day = {}
    for idx in range(len(lst_of_transport2)):
        if lst_of_transport2[idx].city not in dict_of_city_co2_per_day:
            dict_of_city_co2_per_day[lst_of_transport2[idx].city] = (get_co2_per_vehicle_mile(lst_of_transport2[idx])*
                                                                     lst_of_transport2[idx].dailymiles)
        else:
            dict_of_city_co2_per_day[lst_of_transport2[idx].city] += (get_co2_per_vehicle_mile(lst_of_transport2[idx]) *
                                                                     lst_of_transport2[idx].dailymiles)
    return dict_of_city_co2_per_day

def sort_dict_in_lst_form(lst_of_key_and_values:list[str, float]) -> list[str, float]:
    lst_to_sort = lst_of_key_and_values
    for iteration in range(len(lst_to_sort)):
        min_idx = iteration
        for idx in range(iteration, len(lst_to_sort)):
            if lst_to_sort[idx][1] < lst_to_sort[min_idx][1]:
                min_idx = idx
        if min_idx != iteration:
            temp = lst_to_sort[min_idx]
            lst_to_sort[min_idx] = lst_to_sort[iteration]
            lst_to_sort[iteration] = temp
    return lst_to_sort

def sort_city_co2_per_day(dic_of_city_co2_per_day:dict[str, float]) -> dict[str, float]:
    lst_city_co2_per_day = []
    for key in dic_of_city_co2_per_day:
        lst_city_co2_per_day.append([key, dic_of_city_co2_per_day[key]])
    lst_city_co2_per_day = sort_dict_in_lst_form(lst_city_co2_per_day)
    dict_city_co2_per_day = {}
    for key_value in lst_city_co2_per_day:
        dict_city_co2_per_day[key_value[0]] = key_value[1]
    return dict_city_co2_per_day



# for each sorted list we assign point value to add to a dictionary, and then at the end we could display multiple
#   or just code these and bypass the sorting
#   dictionaries of which city had the least carbon footprint per day
#   and which transportation mode had the least carbon footprint per mile and per day
#   which city had the least carbon footprint in relation to the passengers
#   which mode had the least carbon footprint in relation to the passengers