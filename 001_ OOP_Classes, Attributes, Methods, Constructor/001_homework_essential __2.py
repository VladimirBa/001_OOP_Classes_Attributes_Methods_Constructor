class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def c_to_f(self):
        return (self.temperature * 1.8) + 32.0

    def f_to_c(self):
        return (self.temperature - 32.0) * 5 / 9

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def exit(self):
        pass


def main():
    try:
        t = float(input("Enter the value of temperature: "))
    except ValueError:
        print('The value of the temperature has to be number! Enter again.')
        exit()

    unit = input("Enter the scale of the temperature (C - for Celsius; F - for Fahrenheit): ").upper()
    temp = Temperature(t)

    if (t < -273.15 and unit == 'C') or (t < -459.4 and unit == 'F'):
        print('Temperature below "absolute zero" is not possible')
        exit()

    elif unit != 'C' and unit != 'F':
        print('The temperature scale unit has to be "C" or "F" only.')
        exit()

    if unit == 'C':
        print(f"You entered {t} degrees of Celsius that equals {temp.c_to_f():.1f} degrees of Fahrenheit.")
    elif unit == 'F':
        print(f"You entered {t} degrees of Fahrenheit that equals {temp.f_to_c():.1f} degrees of Celsius.")


if __name__ == '__main__':
    main()

