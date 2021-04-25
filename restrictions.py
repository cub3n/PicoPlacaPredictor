import datetime

digits_restriction = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 0))


class VerificationError(Exception):
    pass


class LicensePlate:
    def __init__(self, plate_number):
        given_plate = plate_number.split("-")
        if len(given_plate) != 2:
            raise VerificationError("Invalid plate format")
        letter_part, digits_part = given_plate
        if not letter_part.isalpha():
            raise VerificationError("Invalid plate number, only characters A-Z on the left")
        if not digits_part.isdigit():
            raise VerificationError("Invalid plate number, only numbers on the right")
        self._plate = plate_number

    @property
    def last_digit(self):
        return int(self._plate.strip()[-1])


class Verification:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def can_it_be_on_road(self, plate: LicensePlate):

        current_date_time = datetime.datetime.strptime("{0} {1}".format(self.date, self.time), '%Y-%m-%d %H:%M')

        if ((datetime.time(7, 0) <= current_date_time.time() <= datetime.time(9, 30)
             or datetime.time(16, 0) <= current_date_time.time() <= datetime.time(19, 30))):
            for index, restriction_pair in enumerate(digits_restriction):
                if plate.last_digit in restriction_pair and index == current_date_time.weekday():
                    return False
        return True
