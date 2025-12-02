import unittest
import data
import transitfunctions

full_data = data.get_data()

class UnitTests(unittest.TestCase):
    def test_get_co2_per_vehicle_mile(self):
        mode = full_data[0]
        actual = transitfunctions.get_co2_per_vehicle_mile(mode)
        expected = 3.048
        self.assertEqual(actual, expected)
        print("CO2 per vehicle mile:", actual)

    def test_get_co2_per_passenger_mile(self):
        mode = full_data[0]
        actual = transitfunctions.get_co2_per_passenger_mile(mode)
        expected = 0.22411764705882353
        self.assertEqual(actual, expected)
        print("CO2 per passenger mile:", actual)

    #dictionaries can be in any order to still be equal to its self
    def test_get_city_co2_per_day(self):
        input1 = full_data
        actual = transitfunctions.get_city_co2_per_day(input1)
        expected = {'New York City': 1646340.0885, 'Chicago': 584325.26, 'Seattle': 295409.83999999997,
                    'Los Angeles': 805112.167, 'San Francisco': 289827.66000000003}
        self.assertEqual(actual, expected)
        print("city_co2_per_day Unsorted:", actual)

    def test_sort_city_co2_per_day(self):
        input1 = full_data
        input2 = transitfunctions.get_city_co2_per_day(input1)
        sort = transitfunctions.sort_city_co2_per_day(input2)
        expected = {'San Francisco': 289827.66000000003, 'Seattle': 295409.83999999997, 'Chicago': 584325.26,
                    'Los Angeles': 805112.167, 'New York City': 1646340.0885}
        self.assertEqual(sort, expected)
        print("city_co2_per_day Sorted:", sort)

    def test_get_mode_metric_co2_per_day(self):
        input1 = full_data
        actual = transitfunctions.get_mode_metric_co2_per_day(input1)
        expected = {'Bus-diesel': 2163998.7199999997, 'Heavy Rail-diesel': 25501.6,
                    'Heavy Rail-electric': 519218.67299999995, 'Light Rail-electric': 912296.0225000002}
        self.assertEqual(actual, expected)
        print("mode_metric_co2_per_day Unsorted:", actual)

    def test_sort_mode_metric_co2_per_day(self):
        input1 = full_data
        input2 = transitfunctions.get_mode_metric_co2_per_day(input1)
        sort = transitfunctions.sort_mode_metric_co2_per_day(input2)
        expected = {'Heavy Rail-diesel': 25501.6, 'Heavy Rail-electric': 519218.67299999995,
                    'Light Rail-electric': 912296.0225000002, 'Bus-diesel': 2163998.7199999997}
        self.assertEqual(sort, expected)
        print("mode_metric_co2_per_day Sorted:", sort)

    def test_get_daily_riders_for_each_mode_metric(self):
        input1 = full_data
        actual = transitfunctions.get_daily_riders_for_each_mode_metric(input1)
        expected = {'Bus-diesel': 2494300.0, 'Heavy Rail-diesel': 7341.0, 'Heavy Rail-electric': 457390.0,
                    'Light Rail-electric': 3367165.0}
        self.assertEqual(actual, expected)
        print("Daily Riders:", actual)

    def test_get_co2_per_passenger_by_mode_metric(self):
        input1 = full_data
        input2 = transitfunctions.get_daily_riders_for_each_mode_metric(input1)
        input3 = transitfunctions.get_mode_metric_co2_per_day(input1)
        actual = transitfunctions.get_co2_per_passenger_by_mode_metric(input3, input2)
        expected = {'Bus-diesel': 0.867577564847853, 'Heavy Rail-diesel': 3.4738591472551423,
                    'Heavy Rail-electric': 1.1351771420450818, 'Light Rail-electric': 0.27093891226001704}
        self.assertEqual(actual, expected)
        print("co2_per_passenger_by_mode_metric Unsorted:", actual)

    def test_sort_co2_per_passenger_by_mode_metric(self):
        input1 = full_data
        input2 = transitfunctions.get_daily_riders_for_each_mode_metric(input1)
        input3 = transitfunctions.get_mode_metric_co2_per_day(input1)
        co2_per_passenger = transitfunctions.get_co2_per_passenger_by_mode_metric(input3, input2)
        actual = transitfunctions.sort_co2_per_passenger_by_mode_metric(co2_per_passenger)
        expected = {'Light Rail-electric': 0.27093891226001704, 'Bus-diesel': 0.867577564847853,
            'Heavy Rail-electric': 1.1351771420450818, 'Heavy Rail-diesel': 3.4738591472551423}
        self.assertEqual(actual, expected)
        print("co2_per_passenger_by_mode_metric Sorted:", actual)

    def test_get_city_mode_metric_co2_per_mile(self):
        input1 = full_data
        actual = transitfunctions.get_city_mode_metric_co2_per_mile(input1)
        expected = {'New York City, Bus-diesel': 3.048, 'New York City, Light Rail-electric': 0.98175,
                'New York City, Heavy Rail-electric': 1.06029,'Chicago, Bus-diesel': 2.7432000000000003,
                'Chicago, Light Rail-electric': 1.0390000000000001,
                'Chicago, Heavy Rail-electric': 1.2468000000000001,'Seattle, Bus-diesel': 2.9463999999999997,
                'Seattle, Light Rail-electric': 0.02, 'Seattle, Heavy Rail-diesel': 5.08,
                'Los Angeles, Bus-diesel': 2.54, 'Los Angeles, Light Rail-electric': 3.24,
                'Los Angeles, Heavy Rail-electric': 2.4921, 'San Francisco, Bus-diesel': 2.8448,
                'San Francisco, Light Rail-electric': 0.6240000000000001,
                'San Francisco, Heavy Rail-electric': 0.9750000000000001}
        self.assertEqual(actual, expected)
        print("city_mode_metric_co2_per_mile unsorted:", actual)

    def test_sort_city_mode_metric_co2_per_mile(self):
        input1 = full_data
        input2 = transitfunctions.get_city_mode_metric_co2_per_mile(input1)
        actual = transitfunctions.sort_city_mode_metric_co2_per_mile(input2)
        expected = {'Seattle, Light Rail-electric': 0.02,
                    'San Francisco, Light Rail-electric': 0.6240000000000001,
                    'San Francisco, Heavy Rail-electric': 0.9750000000000001,
                    'New York City, Light Rail-electric': 0.98175,
                    'Chicago, Light Rail-electric': 1.0390000000000001,
                    'New York City, Heavy Rail-electric': 1.06029,
                    'Chicago, Heavy Rail-electric': 1.2468000000000001,
                    'Los Angeles, Heavy Rail-electric': 2.4921,
                    'Los Angeles, Bus-diesel': 2.54,
                    'Chicago, Bus-diesel': 2.7432000000000003,
                    'San Francisco, Bus-diesel': 2.8448,
                    'Seattle, Bus-diesel': 2.9463999999999997,
                    'New York City, Bus-diesel': 3.048,
                    'Los Angeles, Light Rail-electric': 3.24,
                    'Seattle, Heavy Rail-diesel': 5.08}
        self.assertEqual(actual, expected)
        print("City/mode-metric CO2 per mile (sorted):", actual)

    def test_get_daily_riders_city(self):
        input1 = full_data
        actual = transitfunctions.get_daily_riders_city(input1)
        expected = {'New York City': 4315000.0, 'Chicago': 730100.0, 'Seattle': 181556.0, 'Los Angeles': 703480.0,
                    'San Francisco': 396060.0}
        self.assertEqual(actual, expected)
        print("daily_riders_city:", actual)

    def test_get_co2_per_passenger_by_city(self):
        input1 = full_data
        input2 = transitfunctions.get_city_co2_per_day(input1)
        input3 = transitfunctions.get_daily_riders_city(input1)
        actual = transitfunctions.get_co2_per_passenger_by_city(input2, input3)
        expected = {'New York City': 0.38153883858632676, 'Chicago': 0.8003359265853993,
                    'Seattle': 1.6271003987750334,'Los Angeles': 1.1444705848069596,
                    'San Francisco': 0.7317771549765187}
        self.assertEqual(actual, expected)
        print("CO2 per passenger by city:", actual)


