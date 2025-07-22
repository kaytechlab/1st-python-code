unit_converter = {
    "in": {
        "cm": 0.445,
        "ft": "2.334"
    },
    "cm": {
        "in": 23.11,
        "ft": 32.33
    },
    "ft":{
        "cm": 2.4,
        "in": 28.90
    }
}
def converter():
    while True:
        try:
            convert_from = input("from: ")
            convert_to = input("to: ")
            convert_value = int(input("value: "))

            rate = unit_converter[convert_from][convert_to]
            print(f"conversion from {convert_from} to {convert_to}  = {convert_value * rate}")
        except KeyError:
            print("You encounter a key_vale error")

        except ValueError:
            print("You encounter error")

        except ZeroDivisionError:
            print("You encounter error")

        finally:
            print("cal done")
converter()