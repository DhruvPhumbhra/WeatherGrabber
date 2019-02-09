import unittest
from unittest import mock

import weather

def mock_response(status, text):
    m = mock.Mock()
    m.status_code = status
    m.text = text
    return m


class WeatherTestCase(unittest.TestCase):

    @mock.patch('weather.requests.get')
    def test_get_city_temp(self, mock_get):
        mock_resp = mock_response(status=200, text='{"coord":{"lon":-92.72,"lat":41.74},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":20.19,"pressure":1038,"humidity":65,"temp_min":15.08,"temp_max":23},"visibility":16093,"wind":{"speed":14.99,"deg":130},"clouds":{"all":90},"dt":1549745700,"sys":{"type":1,"id":4209,"message":0.0048,"country":"US","sunrise":1549717994,"sunset":1549755451},"id":4859343,"name":"Grinnell","cod":200}')
        mock_get.return_value = mock_resp

        temperature = weather.get_city_temp('Grinnell')
        self.assertEqual(temperature, 20)

    @mock.patch('weather.requests.get')
    def test_city_not_found(self, mock_get):
        mock_resp = mock_response(status=404, text='{"cod":"404","message":"city not found"}')
        mock_get.return_value = mock_resp

        with self.assertRaisesRegex(Exception, 'ERROR 404 city not found'):
            weather.get_city_temp('This is not a city')

if __name__ == '__main__':
    unittest.main()
