import datetime

digits_restrinction = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]


class VerificationError(Exception):
    pass


class LicensePlate:
    def __init__(self, plate_number):
        try:
            given_plate = plate_number.split("-")
            if len(given_plate) != 2 or len(given_plate[0]) != 3 or len(given_plate[1]) != 4:
                raise VerificationError("Invalid plate number, Length ")
            for i in given_plate[0]:
                if i.isdigit():
                    raise VerificationError("Invalid plate number, only characters A-Z on the left")
            for i in given_plate[1]:
                if i.isalpha():
                    raise VerificationError("Invalid plate number, only numbers on the right")
        except (ValueError, IndexError):
            raise VerificationError("Invalid plate number")
        self._plate = plate_number

    @property
    def last_digit(self):
        plate_number = int(self._plate.strip()[-1])
        return plate_number


class Verification:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def can_it_be_on_road(self, plate: LicensePlate):

        try:

            current_date_time = datetime.datetime.strptime("{0} {1}".format(self.date, self.time), '%Y-%m-%d %H:%M')

            if ((datetime.time(7, 0) <= current_date_time.time() <= datetime.time(9, 30)
                 or datetime.time(16, 0) <= current_date_time.time() <= datetime.time(19, 30))):
                for i in digits_restrinction:
                    if plate.last_digit in i and digits_restrinction.index(i) == current_date_time.weekday():
                        return False
            return True
        except (ValueError, IndexError):
            raise VerificationError("Invalid Date")
