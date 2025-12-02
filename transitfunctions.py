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
# how to do: divide co2 per vehicle mile by average passenger on board
#   access class attribute passengers -> .passengers
#   access dictionary value -> key = ['avg on board']
#   get co2 per vehicle mile -> call get_co2_per_vehicle_mile
def get_co2_per_passenger_mile(mode:Transportations) -> float:
    return get_co2_per_vehicle_mile(mode)/mode.passengers['avg on board']


# Purpose: to take in a list of transportations and return a dictionary of mode-metric and
#   their associated kgCO2 per mile {mode-metric: kgCO2/mile}
#   # Input: list[Transportations]
# # Output: dict[str, float]
# # ExInput: [data.get_data()[0], data.get_data()[1], data.get_data()[2]]
# # ExOutput: {'New York City, Bus-diesel': 3.048, 'New York City, Light Rail-electric': 0.98175,
#                 'New York City, Heavy Rail-electric': 1.06029,
# # how to do: create an empty dictionary -> empty = {}
# # go through each item in the list -> for loop
# # determine if it is in the dictionary -> if statement
# #   add to the dictionary -> dict[key] = value
# #       co2 per mile = call get_co2_per_vehicle_mile
# #   add to the value in the dictionary -> dict[key] += value
def get_city_mode_metric_co2_per_mile(lst_of_transport1:list[Transportations]) -> dict[str, float]:
    dict_of_city_mode_metric_co2_per_mile = {}
    for idx in range(len(lst_of_transport1)):
        name = "{}, {}-{}".format(str(lst_of_transport1[idx].city),
                                 str(lst_of_transport1[idx].mode),str(lst_of_transport1[idx].energy['metric']))
        if name not in dict_of_city_mode_metric_co2_per_mile:
            dict_of_city_mode_metric_co2_per_mile[name] = get_co2_per_vehicle_mile(lst_of_transport1[idx])
        else:
            dict_of_city_mode_metric_co2_per_mile[name] += get_co2_per_vehicle_mile(lst_of_transport1[idx])
    return dict_of_city_mode_metric_co2_per_mile

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
#       city = (kgCO2/mile) * daily miles = (kgCO2/per day)
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

# Purpose: to take in a list of transportation objects, and return a dictionary
#   containing the mode-metric and the carbon emissions per day
# Input: list[Transportations]
# Output: dict[str, float]
# ExInput: data.get_data()
# ExOutput: {'Bus-diesel': 2163998.7199999997, 'Heavy Rail-diesel': 25501.6,
#      'Heavy Rail-electric': 519218.67299999995, 'Light Rail-electric': 912715.2225000001}
# how to do: create an empty dictionary -> = {}
# go through each item in the list -> for loop
# create the key for each -> lst_of_transport3[idx].mode + "-" + lst_of_transport3[idx].energy['metric']
# determine if it is in the dictionary -> if statement
#   add to the dictionary -> dict_of_mode_co2_per_day[name] = (get_co2_per_vehicle_mile(lst_of_transport3[idx])*
#                                                                      lst_of_transport3[idx].dailymiles)
#     mode-metric = (kgco2/mile) * daily miles = (kgCO2/per day)
#   add to the value in the dictionary -> dict_of_mode_co2_per_day[name] += (get_co2_per_vehicle_mile(lst_of_transport3[idx]) *
#                                                                      lst_of_transport3[idx].dailymiles)
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

# Purpose: to take in a list of transportation objects, and return a dictionary
#   containing the mode-metric and the daily riders per day
# Input: list[Transportations]
# Output: dict[str, float]
# ExInput: data.get_data()
# ExOutput: {'Bus-diesel': 2494300.0, 'Heavy Rail-diesel': 7341.0, 'Heavy Rail-electric': 457390.0,
#                     'Light Rail-electric': 3367165.0}
# how to do: create an empty dictionary -> = {}
# go through each item in the list -> for loop
# create the key for each -> lst_of_transport4[idx].mode + "-" + lst_of_transport4[idx].energy['metric']
# determine if it is in the dictionary -> if statement
#   add to the dictionary -> dict_of_mode_co2_per_day[name] = lst_of_transport4[idx].passengers['avg daily riders']
#   add to the value in the dictionary -> dict_of_daily_riders_for_each_mode[name] += lst_of_transport4[idx].passengers['avg daily riders']
def get_daily_riders_for_each_mode_metric(lst_of_transport4:list[Transportations]) -> dict[str, float]:
    dict_of_daily_riders_for_each_mode = {}
    for idx in range(len(lst_of_transport4)):
        name = str(lst_of_transport4[idx].mode) + "-" + str(lst_of_transport4[idx].energy['metric'])
        if name not in dict_of_daily_riders_for_each_mode:
            dict_of_daily_riders_for_each_mode[name] = lst_of_transport4[idx].passengers['avg daily riders']
        else:
            dict_of_daily_riders_for_each_mode[name] += lst_of_transport4[idx].passengers['avg daily riders']

    return dict_of_daily_riders_for_each_mode

# Purpose: to take in a list of transportation objects, and return a dictionary
#   containing the city and the daily riders per day
# Input: list[Transportations]
# Output: dict[str, float]
# ExInput: data.get_data()
# ExOutput: {'New York City': 4315000.0, 'Chicago': 730100.0, 'Seattle': 181556.0, 'Los Angeles': 703480.0,
#                     'San Francisco': 396060.0}
# how to do: create an empty dictionary -> = {}
# go through each item in the list -> for loop
# create the key for each -> lst_of_transport[idx].city
# determine if it is in the dictionary -> if statement
#   add to the dictionary -> dict_of_mode_co2_per_day[name] = lst_of_transport4[idx].passengers['avg daily riders']
#   add to the value in the dictionary -> dict_of_daily_riders_for_each_mode[name] += lst_of_transport4[idx].passengers['avg daily riders']
def get_daily_riders_city(lst_of_transport5:list[Transportations]) -> dict[str, float]:
    dict_of_daily_riders_for_city = {}
    for idx in range(len(lst_of_transport5)):
        name = lst_of_transport5[idx].city
        if name not in dict_of_daily_riders_for_city:
            dict_of_daily_riders_for_city[name] = lst_of_transport5[idx].passengers['avg daily riders']
        else:
            dict_of_daily_riders_for_city[name] += lst_of_transport5[idx].passengers['avg daily riders']

    return dict_of_daily_riders_for_city

# Purpose: to take in 2 dictionaries, a dictionary of {mode-metric: kgCO2 per day} and {mode-metric: # of daily riders}
#   and return a dictionary of {mode-metric: kgCO2/passenger)
# Input: dict[str, float], dict[str, float]
# Output: dict[str, float]
# ExInput: {Heavy Rail-diesel: 25501.6}, {Heavy Rail-diesel: 7341}
# ExOutput: {Heavy Rail-diesel: 3.47385914726}
# how to do: (kgCO2/day)/(Passenger/day) = (kgCO2/day)*(day/passenger) = kgCO2/passenger
# create an empty dictionary -> empty = {}
# go through each key in one of the dictionaries -> for loop
# add to the empty dictionary -> empty[key] = value
#    = dict_of_co2_per_day_mode_metric[key]/dict_of_daily_riders_mode_metric[key]
def get_co2_per_passenger_by_mode_metric(dict_of_co2_per_day_mode_metric:dict[str, float], dict_of_daily_riders_mode_metric:dict[str, float]) -> dict[str, float]:
    dict_of_co2_per_passenger_by_mode = {}
    for key in dict_of_co2_per_day_mode_metric:
        dict_of_co2_per_passenger_by_mode[key] = dict_of_co2_per_day_mode_metric[key]/dict_of_daily_riders_mode_metric[key]

    return dict_of_co2_per_passenger_by_mode

# Purpose: to take in 2 dictionaries, a dictionary of {city: kgCO2 per day} and {city: # of daily riders}
#   and return a dictionary of {city: kgCO2/passenger)
# Input: dict[str, float], dict[str, float]
# Output: dict[str, float]
# ExInput: {'New York City': 1646340.0885}, {'New York City': 4315000}
# ExOutput: {'New York City': 0.38153883858632676}
# how to do: (kgCO2/day)/(Passenger/day) = (kgCO2/day)*(day/passenger) = kgCO2/passenger
# create an empty dictionary -> empty = {}
# go through each key in one of the dictionaries -> for loop
# add to the empty dictionary -> empty[key] = value
#    = dict_of_co2_per_day_city[key]/dict_of_daily_riders_city[key]
def get_co2_per_passenger_by_city(dict_of_co2_per_day_city:dict[str, float], dict_of_daily_riders_city:dict[str, float]) -> dict[str, float]:
    dict_of_co2_per_passenger_by_city = {}
    for key in dict_of_co2_per_day_city:
        dict_of_co2_per_passenger_by_city[key] = dict_of_co2_per_day_city[key]/dict_of_daily_riders_city[key]

    return dict_of_co2_per_passenger_by_city

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

# Purpose: to take in a dictionary of mode-metric keys and floats of CO2 emissions per mile, sort them from least
#   to greatest CO2 emissions per day, and return a dictionary that is sorted
# Input: dict[str, float] ({mode-metric: CO2 Emission Per mile})
# Output: dict[str, float] ({mode-metric: CO2 Emission Per mile})
# ExInput: {'Chicago, Bus-diesel': 2.7432000000000003, 'Chicago, Heavy Rail-electric': 1.2468000000000001,
# 'Chicago, Light Rail-electric': 1.0390000000000001, 'Los Angeles, Bus-diesel': 2.54,
# 'Los Angeles, Heavy Rail-electric': 2.4921, 'Los Angeles, Light Rail-electric': 3.24,
# 'New York City, Bus-diesel': 3.048, 'New York City, Heavy Rail-electric': 1.06029,
# 'New York City, Light Rail-electric': 0.98175, 'San Francisco, Bus-diesel': 2.8448,
# 'San Francisco, Heavy Rail-electric': 0.9750000000000001,
# 'San Francisco, Light Rail-electric': 0.6240000000000001,
# 'Seattle, Bus-diesel': 2.9463999999999997,
# 'Seattle, Heavy Rail-diesel': 5.08, 'Seattle, Light Rail-electric': 0.02}
# ExOutput: {'New York City, Bus-diesel': 3.048, 'New York City, Light Rail-electric': 0.98175,
#                 'New York City, Heavy Rail-electric': 1.06029,'Chicago, Bus-diesel': 2.7432000000000003,
#                 'Chicago, Light Rail-electric': 1.0390000000000001,
#                 'Chicago, Heavy Rail-electric': 1.2468000000000001,'Seattle, Bus-diesel': 2.9463999999999997,
#                 'Seattle, Light Rail-electric': 0.02, 'Seattle, Heavy Rail-diesel': 5.08,
#                 'Los Angeles, Bus-diesel': 2.54, 'Los Angeles, Light Rail-electric': 3.24,
#                 'Los Angeles, Heavy Rail-electric': 2.4921, 'San Francisco, Bus-diesel': 2.8448,
#                 'San Francisco, Light Rail-electric': 0.6240000000000001,
#                 'San Francisco, Heavy Rail-electric': 0.9750000000000001}
# how to do: get dictionary into list -> call get_dict_in_lst_form(dic_city_mode_metric_co2_per_mile)
#   sort list -> call sort_dict_in_lst_form(lst_city_mode_metric_co2_per_mile)
#   get into dictionary -> call get_lst_in_dict_form(lst_city_mode_metric_co2_per_mile)
def sort_city_mode_metric_co2_per_mile(dic_city_mode_metric_co2_per_mile:dict[str, float]) -> dict[str, float]:
    lst_city_mode_metric_co2_per_mile = get_dict_in_lst_form(dic_city_mode_metric_co2_per_mile)
    lst_city_mode_metric_co2_per_mile = sort_dict_in_lst_form(lst_city_mode_metric_co2_per_mile)
    dict_city_mode_metric_co2_per_mile = get_lst_in_dict_form(lst_city_mode_metric_co2_per_mile)
    return dict_city_mode_metric_co2_per_mile

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

# Purpose: to take in a dictionary of mode-metric keys and floats of CO2 emissions per passenger, sort them from least
#   to greatest CO2 emissions per passenger, and return a dictionary that is sorted
# Input: dict[str, float] ({mode-metric: CO2 Emission Per Passenger})
# Output: dict[str, float] ({mode-metric: CO2 Emission Per Passenger})
# ExInput: {'Bus-diesel': 0.867577564847853, 'Heavy Rail-diesel': 3.4738591472551423,
# 'Heavy Rail-electric': 1.1351771420450818, 'Light Rail-electric': 0.27093891226001704}
# ExOutput: {'Bus-diesel': 0.867577564847853, 'Heavy Rail-diesel': 3.4738591472551423,
# 'Heavy Rail-electric': 1.1351771420450818, 'Light Rail-electric': 0.27093891226001704}
# how to do: get dictionary into list -> call get_dict_in_lst_form(dic_co2_per_passenger_by_mode_metric)
#   sort list -> call sort_dict_in_lst_form(lst_co2_per_passenger_by_mode_metric)
#   get into dictionary -> call get_lst_in_dict_form(lst_co2_per_passenger_by_mode_metric)
def sort_co2_per_passenger_by_mode_metric(dic_co2_per_passenger_by_mode_metric:dict[str, float]) -> dict[str, float]:
    lst_co2_per_passenger_by_mode_metric = get_dict_in_lst_form(dic_co2_per_passenger_by_mode_metric)
    lst_co2_per_passenger_by_mode_metric = sort_dict_in_lst_form(lst_co2_per_passenger_by_mode_metric)
    dict_co2_per_passenger_by_mode_metric = get_lst_in_dict_form(lst_co2_per_passenger_by_mode_metric)
    return dict_co2_per_passenger_by_mode_metric

#Purpose: to find which transportation emits the most CO2
#Input: list of transport
#output: dict: str, float
#ExOutput: "Highest-emitting mode;" CO2 per passenger
def max_co2_per_passenger(lst_of_transport: list[Transportations]) -> dict[str, float]:
    max_mode = None
    max_value = -1.0

    for t in lst_of_transport:
        co2 = get_co2_per_passenger_mile(t)
        if co2 > max_value:
            max_value = co2
            max_mode = f"{t.mode}-{t.energy['metric']}"

    return {max_mode: max_value}

#Purpose: to find which transportation emits the most CO2
#Input: list of transport
#output: dict: str, float
#ExOutput: "Least-emitting mode;" CO2 per passenger
def min_co2_per_passenger(lst_of_transport: list[Transportations]) -> dict[str, float]:
    min_mode = None
    min_value = -1.0

    for t in lst_of_transport:
        co2 = get_co2_per_passenger_mile(t)
        if co2 < min_value:
            min_value = co2
            min_mode = f"{t.mode}-{t.energy['metric']}"

    return {min_mode: min_value}
#done

