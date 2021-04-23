import datetime
from restrictions import Verification
from restrictions import LicensePlate


def main():
    plates = [LicensePlate("PDG-6530"), LicensePlate("PDJ-4637")]
    verification = Verification('2021-04-23', '19:30')
    for i in plates:
        print("Can be on road" if verification.can_it_be_on_road(i) else "Can't be on road")


if __name__ != '__main__':
    pass
else:
    main()
