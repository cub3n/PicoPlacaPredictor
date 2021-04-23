import datetime
from restrictions import Verification
from restrictions import LicensePlate


def main():
    plate = input(f"Insert a License Plate ")
    date = input("Insert a date with format (YY-MM-DD) ")
    time = input("Insert a time with the format (HH:MM) ")
    plate_check = LicensePlate(plate)
    verification = Verification(date, time)
    print("Can be on road" if verification.can_it_be_on_road(plate_check) else "Can't be on road")


if __name__ != '__main__':
    pass
else:
    main()
