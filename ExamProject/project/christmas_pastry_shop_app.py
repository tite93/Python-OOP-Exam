from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPE = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }
    VALID_BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self.__find_delicacy_by_name(name)
        if delicacy:
            raise Exception(f"{delicacy.name} already exists!")

        if type_delicacy not in self.VALID_DELICACY_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        to_add = self.VALID_DELICACY_TYPE[type_delicacy](name, price)
        self.delicacies.append(to_add)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self.__find_booth_by_number(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        to_add = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(to_add)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        available_booth = self.__find_not_reserved_booth(number_of_people)
        if not available_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        available_booth.NUMBER_OF_PEOPLE = number_of_people
        available_booth.price_for_reservation += number_of_people * available_booth.PRICE_PER_PERSON
        available_booth.is_reserved = True
        return f"Booth {available_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        bill = 0
        booth = self.__find_booth_by_number(booth_number)
        if booth:
            bill += booth.price_for_reservation
            for order in booth.delicacy_orders:
                bill += order.price
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        self.income += bill
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_delicacy_by_name(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy
        return None

    def __find_booth_by_number(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth
        return None

    def __find_not_reserved_booth(self, number):
        for booth in self.booths:
            if not booth.is_reserved:
                if booth.capacity >= number:
                    return booth
        return None
