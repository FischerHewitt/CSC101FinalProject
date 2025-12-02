
import transitfunctions
from test_cases import full_data

def get_string_for_co2_per_mile(sort:dict[str, float]) -> str:
    co2_per_mile_str = ""
    placement = 1
    for key in sort:
        co2_per_mile_str += "{}. {}:{} kgCO2/mile\n".format(placement, key, round(sort[key],4))
        placement += 1
    return co2_per_mile_str

def prt_sort_city_mode_metric_co2_per_mile() -> None:
    input1 = full_data
    input2 = transitfunctions.get_city_mode_metric_co2_per_mile(input1)
    sort = transitfunctions.sort_city_mode_metric_co2_per_mile(input2)
    co2_per_mile_str = get_string_for_co2_per_mile(sort)
    print("CO2 per Mile for each city mode:")
    print(co2_per_mile_str)

def get_string_for_co2_per_day(sort:dict[str, float]) -> str:
    co2_per_day_str = ""
    placement = 1
    for key in sort:
        co2_per_day_str += "{}. {}:{} kgCO2/day\n".format(placement, key, round(sort[key], 3))
        placement += 1
    return co2_per_day_str

def prt_sort_mode_metric_co2_per_day() -> None:
    input1 = full_data
    input2 = transitfunctions.get_mode_metric_co2_per_day(input1)
    sort = transitfunctions.sort_mode_metric_co2_per_day(input2)
    mode_metric_co2_per_day_str = get_string_for_co2_per_day(sort)
    print("CO2 Per Day by Mode across all cities:")
    print(mode_metric_co2_per_day_str)

def prt_sort_city_co2_per_day() -> None:
    input1 = full_data
    input2 = transitfunctions.get_city_co2_per_day(input1)
    sort = transitfunctions.sort_city_co2_per_day(input2)
    city_co2_per_day_str = get_string_for_co2_per_day(sort)
    print("CO2 Per Day by City:")
    print(city_co2_per_day_str)

def get_string_for_co2_per_passenger(sort:dict[str, float]) -> str:
    co2_per_day_str = ""
    placement = 1
    for key in sort:
        co2_per_day_str += "{}. {}:{} kgCO2/passenger\n".format(placement, key, round(sort[key], 3))
        placement += 1
    return co2_per_day_str

def prt_sort_co2_per_passenger_by_mode_metric() -> None:
    input1 = full_data
    dict_co2_per_day_mode_metric = transitfunctions.get_mode_metric_co2_per_day(input1)
    dict_of_daily_riders = transitfunctions.get_daily_riders_for_each_mode_metric(input1)
    dict_of_co2_per_passenger_by_mode_metric = transitfunctions.get_co2_per_passenger_by_mode_metric(dict_co2_per_day_mode_metric, dict_of_daily_riders)
    sort = transitfunctions.sort_co2_per_passenger_by_mode_metric(dict_of_co2_per_passenger_by_mode_metric)
    co2_per_passenger_modemetric_str = get_string_for_co2_per_passenger(sort)
    print("CO2 Per Passenger by Mode across all cities:")
    print(co2_per_passenger_modemetric_str)

def prt_sort_co2_per_passenger_by_city() -> None:
    input1 = full_data
    dict_co2_per_day_city = transitfunctions.get_city_co2_per_day(input1)
    dict_of_daily_riders = transitfunctions.get_daily_riders_city(input1)
    dict_of_co2_per_passenger_by_city = transitfunctions.get_co2_per_passenger_by_city(dict_co2_per_day_city, dict_of_daily_riders)
    sort = transitfunctions.sort_co2_per_passenger_by_mode_metric(dict_of_co2_per_passenger_by_city)
    co2_per_passenger_city_str = get_string_for_co2_per_passenger(sort)
    print("CO2 Per Passenger by City:")
    print(co2_per_passenger_city_str)

def prt_max_co2_per_passenger() -> None:
    max_co2_per_passenger = transitfunctions.max_co2_per_passenger(full_data)
    print("Highest CO2 per passenger-mile:")
    for key in max_co2_per_passenger:
        print("{}:{} kgCO2/passenger-mile".format(key,max_co2_per_passenger[key]))

def main():
    prt_sort_city_mode_metric_co2_per_mile()
    prt_sort_mode_metric_co2_per_day()
    prt_sort_city_co2_per_day()
    prt_sort_co2_per_passenger_by_mode_metric()
    prt_sort_co2_per_passenger_by_city()


if __name__ == "__main__":
    main()



