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

#def get_mile_per_passenger(mode:Transportations) -> float:
    return mode.dailymiles/mode.passengers['avg on board']

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
# ExInput: data.get_data()
# ExOutput: {'New York City': 1646340.0885, 'Chicago': 584325.26,
# 'Seattle': 295829.04, 'Los Angeles': 805112.167,
# 'San Francisco': 289827.66000000003}
# how to do: create an empty dictionary -> ={}
# go through each item in the list -> for loop
# determine if it is in the dictionary -> if statement
#   add to the dictionary -> dict[lst_of_transport[idx].city] = (get_co2_per_vehicle_mile(lst_of_transport[idx])*
#                                                                      lst_of_transport[idx].dailymiles)
#   add to the value in the dictionary -> dict[lst_of_transport[idx].city] += (get_co2_per_vehicle_mile(lst_of_transport[idx])*
#                   lst_of_transport[idx].dailymiles)
def get_city_co2_per_day(lst_of_transport2:list[Transportations]) -> dict[str, float]:
    dict_of_city_co2_per_day = {}
    for idx in range(len(lst_of_transport2)):
        co2_per_day = (get_co2_per_vehicle_mile(lst_of_transport2[idx]) *
               lst_of_transport2[idx].dailymiles)
        if lst_of_transport2[idx].city not in dict_of_city_co2_per_day:
            dict_of_city_co2_per_day[lst_of_transport2[idx].city] = co2_per_day
        else:
            dict_of_city_co2_per_day[lst_of_transport2[idx].city] += co2_per_day
    return dict_of_city_co2_per_day

def get_mode_metric_co2_per_day(lst_of_transport3:list[Transportations]) -> dict[str, float]:
    dict_of_mode_co2_per_day = {}
    for idx in range(len(lst_of_transport3)):
        name = str(lst_of_transport3[idx].mode) + "-" + str(lst_of_transport3[idx].energy['metric'])
        if name not in dict_of_mode_co2_per_day:
            dict_of_mode_co2_per_day[name] = (get_co2_per_vehicle_mile(lst_of_transport3[idx])*
                                                                     lst_of_transport3[idx].dailymiles)
        else:
            dict_of_mode_co2_per_day[name] += (get_co2_per_vehicle_mile(lst_of_transport3[idx]) *
                                                                     lst_of_transport3[idx].dailymiles)
    return dict_of_mode_co2_per_day

def get_daily_riders_for_each_mode_metric(lst_of_transport4:list[Transportations]) -> dict[str, float]:
    dict_of_daily_riders_for_each_mode = {}
    for idx in range(len(lst_of_transport4)):
        name = str(lst_of_transport4[idx].mode) + "-" + str(lst_of_transport4[idx].energy['metric'])
        if name not in dict_of_daily_riders_for_each_mode:
            dict_of_daily_riders_for_each_mode[name] = lst_of_transport4[idx].passengers['avg daily riders']
        else:
            dict_of_daily_riders_for_each_mode[name] += lst_of_transport4[idx].passengers['avg daily riders']

    return dict_of_daily_riders_for_each_mode

def get_co2_per_passenger_by_mode_metric(dict_of_co2_per_day_mode_metric:dict[str, float], dict_of_daily_riders_mode_metric:dict[str, float]) -> dict[str, float]:
    dict_of_co2_per_passenger_by_mode = {}
    for key in dict_of_co2_per_day_mode_metric:
        dict_of_co2_per_passenger_by_mode[key] = dict_of_co2_per_day_mode_metric[key]/dict_of_daily_riders_mode_metric[key]

    return dict_of_co2_per_passenger_by_mode



# Purpose: to take in a list of lists that has str and float values (to imitate a dictionary) and sort the
#   list of list based on the float values
# Input: list[list[str, float]]
# Output: list[list[str, float]]
# ExInput: [['New York City', 1646340.0885], ['Chicago', 584325.26], ['Seattle', 295829.04],
#   ['Los Angeles', 805112.167], ['San Francisco', 289827.66000000003]]
# ExOutput: [['San Francisco', 289827.66000000003], ['Seattle', 295829.04], ['Chicago', 584325.26],
#   ['Los Angeles', 805112.167], ['New York City', 1646340.0885]]
# how to do: go through each element -> for loop
#  selection sort/save minimum idx -> min_idx = iteration
#  compare to each element -> for loop
#  check if value is less than the current minimum -> if statement lst[idx] < lst[min]
#  swap if necessary -> if min_idx != idx
#       temp = lst[min]
#       lst[min] = lst[idx]
#       lst[idx] = temp
def sort_dict_in_lst_form(lst_of_key_and_values:list[list[str, float]]) -> list[list[str, float]]:
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


#hello
#testing
def sort

# Purpose: to take in a dictionary of [str: float] and return a list of lists with [string, float] pairs
# Input: dict[str, float]
# Output: list[list[str, float]]
# ExInput: {'Chicago': 584325.26, 'Los Angeles': 805112.167, 'New York City': 1646340.0885,
#  'San Francisco': 289827.66000000003, 'Seattle': 295829.04}
# ExOutput: [['Chicago', 584325.26], ['Los Angeles', 805112.167], ['New York City', 1646340.0885],
#  ['San Francisco', 289827.66000000003], ['Seattle', 295829.04]]
# how to do: have an empty list -> empty = []
# go through each item in the dictionary -> for loop
# add each item to the empty list -> .append([key, any_dict[key]])
def get_dict_in_lst_form(any_dict:dict[str, float]) -> list[list[str, float]]:
    lst_of_dict = []
    for key in any_dict:
        lst_of_dict.append([key, any_dict[key]])
    return lst_of_dict

# Purpose: take in a list of lists with [string, float] pairs and return a dictionary of [str: float]
# Input: list[list[str, float]]
# Output: dict[str, float]
# ExInput: [['Chicago', 584325.26], ['Los Angeles', 805112.167], ['New York City', 1646340.0885],
#  ['San Francisco', 289827.66000000003], ['Seattle', 295829.04]]
# ExOutput: {'Chicago': 584325.26, 'Los Angeles': 805112.167, 'New York City': 1646340.0885,
#  'San Francisco': 289827.66000000003, 'Seattle': 295829.04}
# how to do: have an empty dictionary -> empty = {}
# go through each element in the list -> for loop
# add to the dictionary -> empty[pair[0]] = pair[1]
def get_lst_in_dict_form(any_lst:list[list[str, float]]) -> dict[str, float]:
    lst_of_dict = {}
    for key_value in any_lst:
        lst_of_dict[key_value[0]] = key_value[1]
    return lst_of_dict

# Purpose: to take in a dictionary of city keys and floats of CO2 emissions per day, sort them from least
#   to greatest CO2 emissions per day, and return a dictionary that is sorted
# Input: dict[str, float] ({city: CO2 Emission Per Day})
# Output: dict[str, float] ({city: CO2 Emission Per Day})
# ExInput: {'Chicago': 584325.26, 'Los Angeles': 805112.167, 'New York City': 1646340.0885,
#   'San Francisco': 289827.66000000003, 'Seattle': 295829.04}
# ExOutput: {'San Francisco': 289827.66000000003, 'Seattle': 295829.04,
#   'Chicago': 584325.26, 'Los Angeles': 805112.167, 'New York City': 1646340.0885}
# how to do: get dictionary into list -> call get_dict_in_lst_form(dic_of_city_co2_per_day)
#   sort list -> call sort_dict_in_lst_form(lst_city_co2_per_day)
#   get into dictionary -> call get_lst_in_dict_form(lst_city_co2_per_day)
def sort_city_co2_per_day(dic_of_city_co2_per_day:dict[str, float]) -> dict[str, float]:
    lst_city_co2_per_day = get_dict_in_lst_form(dic_of_city_co2_per_day)
    lst_city_co2_per_day = sort_dict_in_lst_form(lst_city_co2_per_day)
    dict_city_co2_per_day = get_lst_in_dict_form(lst_city_co2_per_day)
    return dict_city_co2_per_day

# Purpose: to take in a dictionary of mode-metric keys and floats of CO2 emissions per day, sort them from least
#   to greatest CO2 emissions per day, and return a dictionary that is sorted
# Input: dict[str, float] ({mode-metric: CO2 Emission Per Day})
# Output: dict[str, float] ({mode-metric: CO2 Emission Per Day})
# ExInput: {'Bus-diesel': 2163998.7199999997, 'Heavy Rail-diesel': 25501.6,
#         'Heavy Rail-electric': 519218.67299999995, 'Light Rail-electric': 912715.2225000001}
# ExOutput: {'Heavy Rail-diesel': 25501.6, 'Heavy Rail-electric': 519218.67299999995,
#             'Light Rail-electric': 912715.2225000001, 'Bus-diesel': 2163998.7199999997}
# how to do: get dictionary into list -> call get_dict_in_lst_form(dic_of_mode_metric_co2_per_day)
#   sort list -> call sort_dict_in_lst_form(lst_mode_metric_co2_per_day)
#   get into dictionary -> call get_lst_in_dict_form(lst_mode_metric_co2_per_day)
def sort_mode_metric_co2_per_day(dic_of_mode_metric_co2_per_day:dict[str, float]) -> dict[str, float]:
    lst_mode_metric_co2_per_day = get_dict_in_lst_form(dic_of_mode_metric_co2_per_day)
    lst_mode_metric_co2_per_day = sort_dict_in_lst_form(lst_mode_metric_co2_per_day)
    dict_mode_metric_co2_per_day = get_lst_in_dict_form(lst_mode_metric_co2_per_day)
    return dict_mode_metric_co2_per_day



# for each sorted list we assign point value to add to a dictionary, and then at the end we could display multiple
#   or just code these and bypass the sorting
#   dictionaries of which city had the least carbon footprint per day
#   and which transportation mode had the least carbon footprint per mile and per day
#   which city had the least carbon footprint in relation to the passengers
#   which mode had the least carbon footprint in relation to the passengers