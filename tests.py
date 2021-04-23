import unittest

from restrictions import Verification
from restrictions import LicensePlate


class TestVerification(unittest.TestCase):

    def setUp(self):
        self.data = [
            ('HTD-1230', '2021-04-21', '16:00', True),
            ('HTD-1230', '2021-04-23', '16:00', False),
            ('HTD-1230', '2021-04-23', '19:30', False),
            ('HTD-1230', '2021-04-23', '19:31', True),
            ('HTD-1230', '2021-04-22', '07:30', True),
            ('HTD-1230', '2021-04-23', '07:30', False),
            ('ASD-1205', '2021-04-21', '09:00', False),
        ]

    def test_can_it_be_on_road(self):
        for plate, date, time, result in self.data:
            verification = Verification(date, time)
            license = LicensePlate(plate)
            self.assertEqual(verification.can_it_be_on_road(license), result)


if __name__ == '__main__':
    unittest.main()
