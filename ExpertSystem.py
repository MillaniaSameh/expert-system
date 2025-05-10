from experta import Fact, KnowledgeEngine, Rule, NOT, AND, OR, MATCH

from KnowledgeBase.FirstLineFacts import *
from KnowledgeBase.SecondLineFacts import *
from KnowledgeBase.StationsOfIntersectionFacts import *
from KnowledgeBase.FinalStationSelectionFact import *
import random

class MetroTicket(KnowledgeEngine):

    @Rule(NoStationFact())
    def no_station(self):
        print("\n++ Welcome to the Software Expert System ++\n")

        stations = list(FirstLine) + list(SecondLine)
        for i in range(0, len(stations), 3):
            row = []
            for j in range(3):
                if i + j < len(stations):
                    num = i + j + 1
                    name = stations[i + j].value[1]
                    row.append(f"{str(num).zfill(2)}. {name:<30}")
            print(" | ".join(row))

        currentStation = int(input("\nPlease enter your current station: "))
        destinationStation = int(input("Please enter your destination station: "))

        if (currentStation > FirstLine.__len__()):
            currentStation = currentStation - FirstLine.__len__()
            currentStationEnum = self.get_station_by_number(SecondLine, currentStation)
        else:
            currentStationEnum = self.get_station_by_number(FirstLine, currentStation)

        if (destinationStation > FirstLine.__len__()):
            destinationStation = destinationStation - FirstLine.__len__()
            destinationStationEnum = self.get_station_by_number(SecondLine, destinationStation)
        else:
            destinationStationEnum = self.get_station_by_number(FirstLine, destinationStation)

        print(f'\n{"Current Station":20}: {currentStationEnum.value[1]:<30} --> {currentStationEnum.__class__.__name__}')
        print(f'{"Destination Station":20}: {destinationStationEnum.value[1]:<30} --> {destinationStationEnum.__class__.__name__}')

        if (currentStationEnum.__class__.__name__ == destinationStationEnum.__class__.__name__):
            self.declare(SameLinesFact())
        else:
            self.declare(DifferentLinesFact())

        self.declare(FinalStationSelectionFact(
            CurrentStation = currentStationEnum, 
            DestinationStation = destinationStationEnum
        ))

        print("\n-------------------------------------------------------------------------------------------------------")

    @Rule(AND(SameLinesFact(), FinalStationSelectionFact(
        CurrentStation = MATCH.cs,
        DestinationStation =  MATCH.ds
    )))
    def same_lines(self, cs, ds):
        print("\n++ Same Line Route ++\n")
        print(f"From: {cs.value[1]:<30} --> {cs.__class__.__name__}")
        print(f"To  : {ds.value[1]:<30} --> {ds.__class__.__name__}")

        totalStationsNumber = abs(ds.value[0] - cs.value[0])

        if ds.value[0] - cs.value[0] < 0:
            currentLine = self.get_line_name_and_direction(cs.__class__.__name__, False)
        else:
            currentLine = self.get_line_name_and_direction(cs.__class__.__name__, True)

        print(
            f"\nTrip description"
            f"\nTake the {currentLine[0]} ({currentLine[1]})"
            f"\n\nNumber of stations"
            f"\n{totalStationsNumber} stop{'s' if totalStationsNumber != 1 else ''}"
        )

        self.declare(TicketPriceSelectionFact(
            StationsNumber = totalStationsNumber
        ))


    @Rule(AND(DifferentLinesFact(), FinalStationSelectionFact(
        CurrentStation = MATCH.cs,
        DestinationStation =  MATCH.ds
    )))
    def different_lines(self, cs, ds):
        print("\n++ Different Line Route ++\n")
        print(f"From: {cs.value[1]:<30} --> {cs.__class__.__name__}")
        print(f"To  : {ds.value[1]:<30} --> {ds.__class__.__name__}")

        routeOptions = []
        for station in StationsOfIntersection:
            if (cs.__class__.__name__ == FirstLine.__name__):
                before = station.value[0] - cs.value[0] # current to intersection on line 1
                after = ds.value[0] - station.value[1] # intersection to destination on line 2
            else:
                before = station.value[1] - cs.value[0] # current to intersection on line 2
                after = ds.value[0] - station.value[0] # intersection to destination on line 1

            routeOptions.append((before, after, abs(before) + abs(after), station.value[2]))

        minTotal = min(route[2] for route in routeOptions)
        bestOptions = [route for route in routeOptions if route[2] == minTotal]
        beforeIntersection, afterIntersection, totalStationsNumber, intersectionPoint = random.choice(bestOptions)

        if beforeIntersection < 0:
            currentLine = self.get_line_name_and_direction(cs.__class__.__name__, False)
        else:
            currentLine = self.get_line_name_and_direction(cs.__class__.__name__, True)

        if afterIntersection < 0:
            destinationLine = self.get_line_name_and_direction(ds.__class__.__name__, False)
        else:
            destinationLine = self.get_line_name_and_direction(ds.__class__.__name__, True)

        print(
            f"\nTrip description"
            f"\nTake the {currentLine[0]} ({currentLine[1]}) "
            f"and change the station at {intersectionPoint} to the "
            f"{destinationLine[0]} ({destinationLine[1]})"
            f"\n\nNumber of stations"
            f"\n{totalStationsNumber} stop{'s' if totalStationsNumber != 1 else ''}"
        )

        self.declare(TicketPriceSelectionFact(
            StationsNumber = totalStationsNumber
        ))

    @Rule(TicketPriceSelectionFact(
        StationsNumber = MATCH.stations
    ))
    def one_region(self, stations):
        if stations <= 9:
            print(f"\nAmount to be paid\n8 EGP (category 1)")
        elif stations <= 16: 
            print(f"\nAmount to be paid\n10 EGP (category 2)")
        elif stations <= 23: 
            print(f"\nAmount to be paid\n15 EGP (category 3)")
        else:
            print(f"\nAmount to be paid\n20 EGP (category 4)")

    def get_station_by_number(self, enum_class, number):
        for station in enum_class:
            if station.value[0] == number:
                return station
        return None

    def get_line_name_and_direction(self, enum_class_name, positiveDirection):
        line = ""
        direction = ""

        if enum_class_name == "FirstLine":
            line = "first line"
            if positiveDirection:
                direction = "ElMarg Direction"
            else:
                direction = "Helwan Direction"

        if enum_class_name == "SecondLine":
            line = "second line"
            if positiveDirection:
                direction = "Shobra Direction"
            else:
                direction = "ElMoneeb Direction"

        return (line, direction)

def main():
    engine = MetroTicket()
    # print(engine.get_rules())
    engine.reset()
    engine.declare(NoStationFact()) 
    engine.run()

if __name__ == "__main__":
    main()