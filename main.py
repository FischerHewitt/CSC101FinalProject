
import transitfunctions
from test_cases import full_data

# Purpose: to take in a dictionary of strings and floats and return a string
# Input: dict[str, float]
# Output: str
# ExInput: {'Chicago, Bus-diesel': 2.7432000000000003, 'Chicago, Heavy Rail-electric': 1.2468000000000001,
# 'Chicago, Light Rail-electric': 1.0390000000000001, 'Los Angeles, Bus-diesel': 2.54,
# 'Los Angeles, Heavy Rail-electric': 2.4921, 'Los Angeles, Light Rail-electric': 3.24,
# 'New York City, Bus-diesel': 3.048, 'New York City, Heavy Rail-electric': 1.06029,
# 'New York City, Light Rail-electric': 0.98175, 'San Francisco, Bus-diesel': 2.8448,
# 'San Francisco, Heavy Rail-electric': 0.9750000000000001,
# 'San Francisco, Light Rail-electric': 0.6240000000000001,
# 'Seattle, Bus-diesel': 2.9463999999999997,
# 'Seattle, Heavy Rail-diesel': 5.08, 'Seattle, Light Rail-electric': 0.02}
# ExOutput: "1. Seattle, Light Rail-electric:0.02 kgCO2/mile
# 2. San Francisco, Light Rail-electric:0.624 kgCO2/mile
# 3. San Francisco, Heavy Rail-electric:0.975 kgCO2/mile
# 4. New York City, Light Rail-electric:0.9818 kgCO2/mile
# 5. Chicago, Light Rail-electric:1.039 kgCO2/mile
# 6. New York City, Heavy Rail-electric:1.0603 kgCO2/mile
# 7. Chicago, Heavy Rail-electric:1.2468 kgCO2/mile
# 8. Los Angeles, Heavy Rail-electric:2.4921 kgCO2/mile
# 9. Los Angeles, Bus-diesel:2.54 kgCO2/mile
# 10. Chicago, Bus-diesel:2.7432 kgCO2/mile
# 11. San Francisco, Bus-diesel:2.8448 kgCO2/mile
# 12. Seattle, Bus-diesel:2.9464 kgCO2/mile
# 13. New York City, Bus-diesel:3.048 kgCO2/mile
# 14. Los Angeles, Light Rail-electric:3.24 kgCO2/mile
# 15. Seattle, Heavy Rail-diesel:5.08 kgCO2/mile"
# how to do: empty string -> = ""
#   keep track of number -> = 1
#   go through each key -> for loop
#   add to string -> += "{}. {}:{} kgCO2/mile\n".format(placement, key, round(sort[key],4))
#   add to number -> += 1
def get_string_for_co2_per_mile(sort:dict[str, float]) -> str:
    co2_per_mile_str = ""
    placement = 1
    for key in sort:
        co2_per_mile_str += "{}. {}:{} kgCO2/mile\n".format(placement, key, round(sort[key],4))
        placement += 1
    return co2_per_mile_str

# Purpose: to print CO2 per Mile for each city mode:
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get full data -> = full_data
#   get city mode metric co2 per mile -> call get_city_mode_metric_co2_per_mile
#   sort city mode metric co2 per mile -> call sort_city_mode_metric_co2_per_mile
#   get co2 per mile string -> call get_string_for_co2_per_mile
#   print -> print("")
def prt_sort_city_mode_metric_co2_per_mile() -> None:
    input1 = full_data
    input2 = transitfunctions.get_city_mode_metric_co2_per_mile(input1)
    sort = transitfunctions.sort_city_mode_metric_co2_per_mile(input2)
    co2_per_mile_str = get_string_for_co2_per_mile(sort)
    print("CO2 per Mile for each city mode:")
    print(co2_per_mile_str)

# Purpose: to take in a dictionary of strings and floats and return a string
# Input: dict[str, float]
# Output: str
# ExInput: {'San Francisco': 289827.66, 'Seattle': 295409.84}
# ExOutput: "1. San Francisco:289827.66 kgCO2/day
# 2. Seattle:295409.84 kgCO2/day"
# how to do: empty string -> = ""
#   keep track of number -> = 1
#   go through each key -> for loop
#   add to string -> += "{}. {}:{} kgCO2/day\n".format(placement, key, round(sort[key], 3))
#   add to number -> += 1
def get_string_for_co2_per_day(sort:dict[str, float]) -> str:
    co2_per_day_str = ""
    placement = 1
    for key in sort:
        co2_per_day_str += "{}. {}:{} kgCO2/day\n".format(placement, key, round(sort[key], 3))
        placement += 1
    return co2_per_day_str

# Purpose: to print CO2 Per Day by Mode across all cities:
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get full data -> = full_data
#   get mode metric co2 per day -> call get_mode_metric_co2_per_day
#   sort mode metric co2 per day -> call sort_mode_metric_co2_per_day
#   get co2 per day string -> call get_string_for_co2_per_day
#   print -> print("")
def prt_sort_mode_metric_co2_per_day() -> None:
    input1 = full_data
    input2 = transitfunctions.get_mode_metric_co2_per_day(input1)
    sort = transitfunctions.sort_mode_metric_co2_per_day(input2)
    mode_metric_co2_per_day_str = get_string_for_co2_per_day(sort)
    print("CO2 Per Day by Mode across all cities:")
    print(mode_metric_co2_per_day_str)

# Purpose: to print CO2 Per Day by City:
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get full data -> = full_data
#   get city co2 per day -> call get_city_co2_per_day
#   sort city co2 per day -> call sort_city_co2_per_day
#   get co2 per day string -> call get_string_for_co2_per_day
#   print -> print("")
def prt_sort_city_co2_per_day() -> None:
    input1 = full_data
    input2 = transitfunctions.get_city_co2_per_day(input1)
    sort = transitfunctions.sort_city_co2_per_day(input2)
    city_co2_per_day_str = get_string_for_co2_per_day(sort)
    print("CO2 Per Day by City:")
    print(city_co2_per_day_str)

# Purpose: to take in a dictionary of strings and floats and return a string
#   for CO2 per passenger
# Input: dict[str, float]
# Output: str
# ExInput: {'Light Rail-electric': 0.2709389, 'Heavy Rail-diesel': 3.4739}
# ExOutput: "1. Light Rail-electric:0.271 kgCO2/passenger
# 2. Heavy Rail-diesel:3.474 kgCO2/passenger"
# how to do: empty string -> = ""
#   keep track of number -> = 1
#   go through each key -> for loop
#   add to string -> += "{}. {}:{} kgCO2/passenger\n".format(placement, key, round(sort[key], 3))
#   add to number -> += 1
def get_string_for_co2_per_passenger(sort:dict[str, float]) -> str:
    co2_per_day_str = ""
    placement = 1
    for key in sort:
        co2_per_day_str += "{}. {}:{} kgCO2/passenger\n".format(placement, key, round(sort[key], 3))
        placement += 1
    return co2_per_day_str

# Purpose: to print CO2 Per Passenger by Mode across all cities:
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get full data -> = full_data
#   get mode metric co2 per day -> call get_mode_metric_co2_per_day
#   get daily riders for each mode metric -> call get_daily_riders_for_each_mode_metric
#   get co2 per passenger by mode metric -> call get_co2_per_passenger_by_mode_metric
#   sort co2 per passenger by mode metric -> call sort_co2_per_passenger_by_mode_metric
#   get co2 per passenger string -> call get_string_for_co2_per_passenger
#   print -> print("")
def prt_sort_co2_per_passenger_by_mode_metric() -> None:
    input1 = full_data
    dict_co2_per_day_mode_metric = transitfunctions.get_mode_metric_co2_per_day(input1)
    dict_of_daily_riders = transitfunctions.get_daily_riders_for_each_mode_metric(input1)
    dict_of_co2_per_passenger_by_mode_metric = transitfunctions.get_co2_per_passenger_by_mode_metric(dict_co2_per_day_mode_metric, dict_of_daily_riders)
    sort = transitfunctions.sort_co2_per_passenger_by_mode_metric(dict_of_co2_per_passenger_by_mode_metric)
    co2_per_passenger_modemetric_str = get_string_for_co2_per_passenger(sort)
    print("CO2 Per Passenger by Mode across all cities:")
    print(co2_per_passenger_modemetric_str)

# Purpose: to print CO2 Per Passenger by City:
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get full data -> = full_data
#   get city co2 per day -> call get_city_co2_per_day
#   get daily riders for each city -> call get_daily_riders_city
#   get co2 per passenger by city -> call get_co2_per_passenger_by_city
#   sort co2 per passenger by city -> call sort_co2_per_passenger_by_mode_metric
#   get co2 per passenger string -> call get_string_for_co2_per_passenger
#   print -> print("")
def prt_sort_co2_per_passenger_by_city() -> None:
    input1 = full_data
    dict_co2_per_day_city = transitfunctions.get_city_co2_per_day(input1)
    dict_of_daily_riders = transitfunctions.get_daily_riders_city(input1)
    dict_of_co2_per_passenger_by_city = transitfunctions.get_co2_per_passenger_by_city(dict_co2_per_day_city, dict_of_daily_riders)
    sort = transitfunctions.sort_co2_per_passenger_by_mode_metric(dict_of_co2_per_passenger_by_city)
    co2_per_passenger_city_str = get_string_for_co2_per_passenger(sort)
    print("CO2 Per Passenger by City:")
    print(co2_per_passenger_city_str)

# Purpose: to print the highest CO2 per passenger-mile and its mode-metric
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get max co2 per passenger-mile -> call max_co2_per_passenger(full_data)
#   print -> print("Highest CO2 per passenger-mile:")
#   go through each key in dict -> for loop
#   print key and value -> print("{}:{} kgCO2/passenger-mile".format(key, max_co2[key]))
def prt_max_co2_per_passenger() -> None:
    max_co2 = transitfunctions.max_co2_per_passenger(full_data)
    print("Highest CO2 per passenger-mile:")
    for key in max_co2:
        print("{}:{} kgCO2/passenger-mile".format(key,max_co2[key]))

# Purpose: to print the lowest CO2 per passenger-mile and its mode-metric
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: get min co2 per passenger-mile -> call min_co2_per_passenger(full_data)
#   print -> print("Least CO2 per passenger-mile:")
#   go through each key in dict -> for loop
#   print key and value -> print("{}:{} kgCO2/passenger-mile".format(key, min_co2[key]))
def prt_min_co2_per_passenger() -> None:
    min_co2 = transitfunctions.min_co2_per_passenger(full_data)
    print("Least CO2 per passenger-mile:")
    for key in min_co2:
        print("{}:{} kgCO2/passenger-mile".format(key,min_co2[key]))

# Purpose: to print a social reflection about the CO2 emission results
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: print -> print("Social reflection:")
def prt_social_reflection() -> None:
    print("\nSocial reflection:")
    print("Our project analyzes CO2 emissions from public transportations modes in San Francisco, Seattle, Chicago, "
          "Los Angeles, and New York City. The results show that electric light rail is the most efficient mode"
          "at about 0.27 kg CO2 per passenger per day, while diesel heavy rail is the worst, at around 3.47 kg "
          "CO2 per passenger per day. When we look by city, New York has the highest CO2 emissions per day, however"
          "it has the lowest emissions per passengers. Seattle has the cleanest mode of transportation with its"
          "Light Rail only emitting 0.02 kg CO2/per mile, however Seattle has a higher kg CO2 per rider. Our analysis"
          "suggest that to optimize the amount of clean energy used, you ned to have cleaner modes and lots of riders."
          "From the limited data we have collected, it seems that a combination of Seattle light rail, and number of"
          "riders from New York should be implemented in cities to lower the per-passenger emissions and total emissions.")

# Purpose: to call all the print functions to show results and reflection
# Input: None
# Output: None
# ExInput: None
# ExOutput: None
# How to do: call each print function in order ->
#   prt_sort_city_mode_metric_co2_per_mile()
#   prt_sort_mode_metric_co2_per_day()
#   prt_sort_city_co2_per_day()
#   prt_sort_co2_per_passenger_by_mode_metric()
#   prt_sort_co2_per_passenger_by_city()
#   prt_max_co2_per_passenger()
#   prt_social_reflection()
def main():
    prt_sort_city_mode_metric_co2_per_mile()
    prt_sort_mode_metric_co2_per_day()
    prt_sort_city_co2_per_day()
    prt_sort_co2_per_passenger_by_mode_metric()
    prt_sort_co2_per_passenger_by_city()
    prt_max_co2_per_passenger()
    prt_min_co2_per_passenger()
    prt_social_reflection()


if __name__ == "__main__":
    main()



