unit_converter ={
    "kg":{
        "gram":1.45,
        "pd":2.45
    },
    "pd":{
        "kg":24.5,
        "gram":1.45
    },
    "gram":{
        "pd":2.45,
        "kg":24.5
    }
}
def converter():
    while True:
        try:
            convert_from = input("from :")
            convert_to = input("to :")
            convert_value =float(input("value: "))

            rate = unit_converter[convert_from][convert_to]
            print(f"convert_from{convert_from} to {convert_to} = {convert_value * rate}")
        except ValueError:
            print("You encounter error")

        except ZeroDivisionError:
            print("You encounter error")

        except KeyError:
            print("You encounter a key_vale error")

converter()