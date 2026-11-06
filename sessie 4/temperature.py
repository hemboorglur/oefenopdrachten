## NOAH ZEEMAN - 15494365
## NSP2 - ECPC - classes "Class 'Temperature'"
## 6 Nov 26

class Temperature:
    def __init__(self, temperature_celsius): 
        self.temperature= temperature_celsius

    def to_celsius(self): 
        return self.temperature

    def to_kelvin(self):
        return self.temperature + 273.15

        # K = C + 273.15


    def to_fahrenheit(self):
        return round(self.temperature * (9/5) + 32, 2)
        # F = C * 9/5 + 32

    def update_temperature(self, temperature_celsius):
        self.temperature = temperature_celsius
        # update the stored temperature


# test code
temperature = Temperature(37)
print(f"{temperature.temperature=}")
print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=}")
print()

temperature.update_temperature(21)
print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=}")