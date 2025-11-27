import unittest
import data
import transitfunctions

full_data = data.get_data()

class UnitTests(unittest.TestCase):
    def test_sort_co2_per_vehicle_mile(self):
        input1 = full_data
        actual = transitfunctions.sort_co2_per_vehicle_mile(input1)
        empty_list = []
        for idx in range(len(actual)):
            city = actual[idx].city
            transit = actual[idx].mode
            co2 = transitfunctions.get_co2_per_vehicle_mile(actual[idx])
            empty_list.append([city, transit, co2])
        print(empty_list)

