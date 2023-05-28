from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50
    NUMBER_OF_PEOPLE = 0

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.NUMBER_OF_PEOPLE = number_of_people
        result = number_of_people * self.PRICE_PER_PERSON
        self.is_reserved = True
        self.price_for_reservation = result

