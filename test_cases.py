import unittest
import data
import transitfunctions

full_data = data.get_data()

class UnitTests(unittest.TestCase):
    """def test_sort_city_mode_co2_per_vehicle_mile(self):
        input1 = full_data
        actual = transitfunctions.sort_co2_per_vehicle_mile(input1)
        empty_list = []
        for idx in range(len(actual)):
            city = actual[idx].city
            transit = actual[idx].mode
            co2 = round(transitfunctions.get_co2_per_vehicle_mile(actual[idx]),5)
            empty_list.append([city, transit, co2])
        print(empty_list)

    def test_sort_city_mode_co2_per_passenger_mile(self):
        input1 = full_data
        actual = transitfunctions.sort_co2_per_vehicle_mile(input1)
        for idx in range(len(actual)):
            city = actual[idx].city
            transit = actual[idx].mode
            co2 = round(transitfunctions.get_co2_per_vehicle_mile(actual[idx]),5)
            print("{}-{}:{} kgCO2, ".format(city, transit, co2))"""

    #dictionaries can be in any order to still be equal to its self
    def test_get_city_co2_per_day(self):
        input1 = full_data
        actual = transitfunctions.get_city_co2_per_day(input1)
        expected = {'New York City': 1646340.0885, 'Chicago': 584325.26, 'Seattle': 295829.04,
                    'Los Angeles': 805112.167, 'San Francisco': 289827.66000000003}
        self.assertEqual(actual, expected)
        print("Unsorted:", actual)

    def test_get_city_co2_per_day2(self):
        input1 = full_data
        actual = transitfunctions.get_city_co2_per_day(input1)
        expected = {'New York City': 1646340.0885, 'Chicago': 584325.26, 'Seattle': 295829.04,
                    'Los Angeles': 805112.167, 'San Francisco': 289827.66000000003}
        self.assertEqual(actual, expected)
        print("Unsorted:", actual)

    def test_sort_city_co2_per_day(self):
        input1 = full_data
        input2 = transitfunctions.get_city_co2_per_day(input1)
        sort = transitfunctions.sort_city_co2_per_day(input2)
        expected = {'San Francisco': 289827.66000000003, 'Seattle': 295829.04, 'Chicago': 584325.26,
                    'Los Angeles': 805112.167, 'New York City': 1646340.0885}
        self.assertEqual(sort, expected)
        print("Sorted:", sort)

    def test_get_mode_metric_co2_per_day(self):
        input1 = full_data
        actual = transitfunctions.get_mode_metric_co2_per_day(input1)
        expected = {'Bus-diesel': 2163998.7199999997, 'Heavy Rail-diesel': 25501.6,
                    'Heavy Rail-electric': 519218.67299999995, 'Light Rail-electric': 912715.2225000001}
        self.assertEqual(actual, expected)
        print("Unsorted:", actual)

    def test_sort_mode_metric_co2_per_day(self):
        input1 = full_data
        input2 = transitfunctions.get_mode_metric_co2_per_day(input1)
        sort = transitfunctions.sort_mode_metric_co2_per_day(input2)
        expected = {'Heavy Rail-diesel': 25501.6, 'Heavy Rail-electric': 519218.67299999995,
                    'Light Rail-electric': 912715.2225000001, 'Bus-diesel': 2163998.7199999997}
        self.assertEqual(sort, expected)
        print("Sorted:", sort)
