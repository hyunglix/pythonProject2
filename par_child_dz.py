class Iphone7:
    def __init__(self, wireless_charging=None, user_identification_sensors='Fingerprint', brand='Iphone' ):
        self.operating_memory = 2
        self.mass = 138
        self.battery_capacity = 1960
        self.wireless_charging = wireless_charging
        self.user_identification_sensors = user_identification_sensors
        self.model = 7
        self.brand = brand

class Iphone8(Iphone7):
    def __init__(self):
        super().__init__()
        self.mass = 148
        self.battery_capacity = 1821
        self.model = 8
        self.wireless_charging = 'standard Qi'
    def characteristics(self):
        print(f"Characteristics of {self.brand}{self.model}: \n"
              f"Mass - {self.mass} \n"
              f"Battery Capacity - {self.battery_capacity} \n"
              f"Identification Sensors - {self.user_identification_sensors} \n"
              f"Wireless Charging - {self.wireless_charging} \n"
              f"Operating Memory - {self.operating_memory}")

phone = Iphone8()
phone.characteristics()



