from data import Transportations

# (kWh/mile) x (kgCO2/kWh) = (kgCO2/mile)
def get_co2_per_vehicle_mile(mode:Transportations) -> float:
    return mode.energy['value'] * mode.emissions['factor']