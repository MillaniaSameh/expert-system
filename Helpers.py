def get_station_by_number(enum_class, number):
    for station in enum_class:
        if station.value[0] == number:
            return station
    return None

def get_line_name_and_direction(enum_class_name, positiveDirection):
    line = ""
    direction = ""

    if enum_class_name == "FirstLine":
        line = "first line"
        if positiveDirection:
            direction = "Marg Direction"
        else:
            direction = "Helwan Direction"

    if enum_class_name == "SecondLine":
        line = "second line"
        if positiveDirection:
            direction = "Shobra Direction"
        else:
            direction = "El Moneeb Direction"

    return (line, direction)