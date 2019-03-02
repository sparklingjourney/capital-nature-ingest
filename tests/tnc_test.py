import unittest
from events.tnc import main
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

class MyEventsTestCase(unittest.TestCase):
    '''
    Test cases for My Events
    '''
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_my_events(self):
        result = main()
        expected = [{
                    "Event Cost": "0",
                    "Event Currency Symbol": "$",
                    "Event Description": "foo",
                    "Event End Date": "2019-01-27",
                    "Event End Time": "12:00:00",
                    "Event Name": "baz",
                    "Event Organizers": "buz",
                    "Event Start Date": "2019-01-27",
                    "Event Start Time": "10:00:00",
                    "Timezone": "America/New_York",
                    "Event Venue Name": "Dawson Terrace",
                    "Event Website": "https://www.fizbuz.com",
                    "All Day Event":False}]
        self.assertCountEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()
