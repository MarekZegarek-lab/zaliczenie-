def convert_temperature():
    value = float(input("Podaj temperaturę: "))
    unit = input("Podaj jednostkę (C/F/K): ").upper()
    if unit == "C":
        print(f"{value} °C = {value * 9/5 + 32} °F = {value + 273.15} K")
    elif unit == "F":
        print(f"{value} °F = {(value - 32) * 5/9} °C = {(value - 32) * 5/9 + 273.15} K")
    elif unit == "K":
        print(f"{value} K = {value - 273.15} °C = {(value - 273.15) * 9/5 + 32} °F")
    else:
        print("Nieznana jednostka")

def convert_weight():
    value = float(input("Podaj wagę/masę: "))
    unit = input("Podaj jednostkę (kg/g/lb): ").lower()
    if unit == "kg":
        print(f"{value} kg = {value * 1000} g = {value * 2.20462} lb")
    elif unit == "g":
        print(f"{value} g = {value / 1000} kg = {value * 0.00220462} lb")
    elif unit == "lb":
        print(f"{value} lb = {value * 0.453592} kg = {value * 453.592} g")
    else:
        print("Nieznana jednostka")

def convert_volume():
    value = float(input("Podaj objętość: "))
    unit = input("Podaj jednostkę (l/ml/gal): ").lower()
    if unit == "l":
        print(f"{value} l = {value * 1000} ml = {value * 0.264172} gal (US)")
    elif unit == "ml":
        print(f"{value} ml = {value / 1000} l = {value * 0.000264172} gal (US)")
    elif unit == "gal":
        print(f"{value} gal (US) = {value * 3.78541} l = {value * 3785.41} ml")
    else:
        print("Nieznana jednostka")

def convert_pressure():
    value = float(input("Podaj ciśnienie: "))
    unit = input("Podaj jednostkę (Pa/bar/atm): ").lower()
    if unit == "pa":
        print(f"{value} Pa = {value / 100000} bar = {value / 101325} atm")
    elif unit == "bar":
        print(f"{value} bar = {value * 100000} Pa = {value * 0.986923} atm")
    elif unit == "atm":
        print(f"{value} atm = {value * 101325} Pa = {value * 1.01325} bar")
    else:
        print("Nieznana jednostka")

def convert_data():
    value = float(input("Podaj ilość danych: "))
    unit = input("Podaj jednostkę (bit/B/KB/MB/GB): ").upper()
    units = {
        "BIT": 1,
        "B": 8,
        "KB": 8 * 1024,
        "MB": 8 * 1024 ** 2,
        "GB": 8 * 1024 ** 3,
    }
    if unit in units:
        bits = value * units[unit]
        print(f"{bits} bit = {bits / 8} B = {bits / (8 * 1024)} KB = {bits / (8 * 1024 ** 2)} MB = {bits / (8 * 1024 ** 3)} GB")
    else:
        print("Nieznana jednostka")

def convert_distance():
    value = float(input("Podaj długość: "))
    unit = input("Podaj jednostkę (km/mi): ").lower()
    if unit == "km":
        print(f"{value} km = {value * 0.621371} mi")
    elif unit == "mi":
        print(f"{value} mi = {value * 1.60934} km")
    else:
        print("Nieznana jednostka")

def main():
    while True:
        print("\n--- Konwerter jednostek ---")
        print("1. Temperatura")
        print("2. Waga/Masa")
        print("3. Objętość")
        print("4. Ciśnienie")
        print("5. Dane cyfrowe")
        print("6. Kilometry/Mile")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            convert_temperature()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_volume()
        elif choice == "4":
            convert_pressure()
        elif choice == "5":
            convert_data()
        elif choice == "6":
            convert_distance()
        elif choice == "0":
            print("Do widzenia!")
            break
        else:
            print("Niepoprawna opcja")

if __name__ == "__main__":
    main()