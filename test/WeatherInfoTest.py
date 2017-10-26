import unittest

from interface.WeatherInfo import WeatherInfo


class WeatherInfoTest(unittest.TestCase):

    def test_default(self):
        defaultWeather = WeatherInfo()
        print('\n' + defaultWeather.__dict__.__str__())
        self.assertEqual(defaultWeather.city, 'Chicago')
        self.assertEqual(defaultWeather.temperature, '3 degrees Celcius')
        self.assertEqual(defaultWeather.zipcode, 60614)


if __name__ == '__main__':
    unittest.main()
