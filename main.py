class Attraction:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
    
    def get_details(self):
        print(f"Attraction: {self.__name}, Capacity: {self.__capacity}.")
    
    def start(self):
        print("The Attraction is Starting.")

class Thrill_Ride(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._min_height = min_height
    
    def start(self):
        print(f"Thrill Ride {self.__name} is now starting. Hold on Tight!")
    
    def is_eligible(height):
        if height < 140:
            print("Ineligible")
        else:
            print("Eligible")

class Family_Ride(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
    
    def start(self):
        print(f"Family Ride {self.__name} is now starting. Enjoy the fun!")
    
    def is_eligible(self, age):
        if age < 12:
            print("Ineligible")
            return False
        else:
            print("Eligible")
            return True

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def work(self):
        print(f"Staff {self.__name} is performing their role: {self.__role}.")

class Visitor:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
    
    def ride(self, attraction)

