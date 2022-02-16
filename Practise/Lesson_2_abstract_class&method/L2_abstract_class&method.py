
from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def __init__(self, price, brand, manufacture_year, device_name):
        self.price = price
        self.brand = brand
        self.manufacture_year = manufacture_year
        self.device_name = device_name

    @abstractmethod
    def info_about_device(self):
        pass

    def get_price(self):
        return self.price

    def get_decive_name(self):
        return self.device_name

class WiFiBox(Device):

    def __init__(self, price, brand, manufacture_year, wifi_version, device_name='WiFiBox'):
        super().__init__(price, brand, manufacture_year, device_name)
        self.wifi_version = wifi_version

    def info_about_device(self):
        print(f'This is {self.device_name} manufactured in {self.manufacture_year} by {self.brand}. Cost of {self.device_name} is ${self.price}. Vesrion: {self.wifi_version}')


class Desktop(Device):

    def __init__(self, price, brand, manufacture_year, ram, device_name='Desktop'):
        super().__init__(price, brand, manufacture_year, device_name)
        self.ram = ram

    def info_about_device(self):
        print(f'This is {self.device_name} manufactured in {self.manufacture_year} by {self.brand}. Cost of {self.device_name} is ${self.price}. Ram: {self.ram}')


class Smartphone(Device):

    def __init__(self, price, brand, manufacture_year, ram, diagonal_screen, device_name='Smartphone'):
        super().__init__(price, brand, manufacture_year, device_name)
        self.ram = ram
        self.diagonal_screen = diagonal_screen

    def info_about_device(self):
        print(f'This is {self.device_name} manufactured in {self.manufacture_year} by {self.brand}. Cost of {self.device_name} is ${self.price}. Ram: {self.ram}. Diagonal screen: {self.diagonal_screen}.')


def get_info(list_of_obj = []):
    for i in list_of_obj:
        i.info_about_device()

def search_by_price(price, list_of_object = []):
    for i in list_of_obj:
        if i.get_price() == price:
            return i.get_decive_name()


def get_highest_price(list_of_obj = []):
    max_price = list_of_obj[0].get_price()
    for i in list_of_obj:
        x = i.get_price()
        if x > max_price:
            max_price = x
    device_name = search_by_price(max_price, list_of_obj)
    print(f'The highest price is {max_price} --> {device_name}')


def get_lowest_price(list_of_obj = []):
    min_price = list_of_obj[0].get_price()
    for i in list_of_obj:
        x = i.get_price()
        if x < min_price:
            min_price = x
    device_name = search_by_price(min_price, list_of_obj)
    print(f'The highest price is {min_price} --> {device_name}')



wifibox = WiFiBox(20, "Sony", 2018, 6)
desktop = Desktop(350, "Asus", 2021, 32)
smartphone = Smartphone(50, "Nokia", 2014, 2, 4)

wifibox2 = WiFiBox(45, "UPC", 2014, 4)
desktop2 = Desktop(400, "HP", 2021, 62)
smartphone2 = Smartphone(10, "Acer", 2014, 2, 5.5)

list_of_obj = [wifibox, desktop, smartphone, wifibox2, desktop2, smartphone2]

get_info(list_of_obj)
get_highest_price(list_of_obj)
get_lowest_price(list_of_obj)

