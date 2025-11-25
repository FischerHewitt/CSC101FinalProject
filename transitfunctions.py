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

def sort_co2_per_vehicle_mile(lst_of_transport:list[Transportations]) -> list[Transportations]:
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
    return sort_lst_of_cos_per_vehicle_mile
