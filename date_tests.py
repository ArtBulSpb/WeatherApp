from articles import parse_date
import unittest
import datetime

correct_dates = ["2024-05-19",
                 "2024-05-15",
                 "2024-01-01",
                 "2020-01-01",
                 "2014-02-02",
                 "2000-02-02",
                 "2001-11-22",
                 "2001-07-10",
                 "2003-01-10",
                 ]

uncorrect_dates = ["",
                   "1",
                   "2011--01-10",
                   "2013-01",
                   "2003-01+01",
                   "2007"]

class DatesTest(unittest.TestCase):
    def test_correct_dates(self):
        for date_val in correct_dates:
            self.assertTrue(isinstance(parse_date(date_val), datetime.date))
    
    def test_uncorrect_dates(self):
        for date_val in uncorrect_dates:
            self.assertFalse(isinstance(parse_date(date_val), datetime.date))
        
if __name__ == '__main__':
    unittest.main()