def get_station_by_number(enum_class, number):
    for station in enum_class:
        if station.value[0] == number:
            return station
    return None