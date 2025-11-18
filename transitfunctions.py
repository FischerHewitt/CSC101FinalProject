from data import Transportations


def get_co2_per_vehicle_mile(mode:Transportations) -> float:
    return mode.energy['value'] * mode.emissions['factor']