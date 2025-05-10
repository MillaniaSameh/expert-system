from experta import Fact, KnowledgeEngine, Rule, NOT, AND, OR, MATCH

from KnowledgeBase.FirstLineFacts import *
from KnowledgeBase.SecondLineFacts import *
from KnowledgeBase.StationsOfIntersectionFacts import *
from KnowledgeBase.FinalStationSelectionFact import *
from Helpers import *

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
            currentStationEnum = get_station_by_number(SecondLine, currentStation)
        else:
            currentStationEnum = get_station_by_number(FirstLine, currentStation)

        if (destinationStation > FirstLine.__len__()):
            destinationStation = destinationStation - FirstLine.__len__()
            destinationStationEnum = get_station_by_number(SecondLine, destinationStation)
        else:
            destinationStationEnum = get_station_by_number(FirstLine, destinationStation)

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
        stationsNumber = abs(cs.value[0] - ds.value[0])
        print(f"\nYour trip includes {stationsNumber} stop{'s' if stationsNumber != 1 else ''}. Enjoy your ride!")

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
                before = abs(station.value[0] - cs.value[0]) # current to intersection on line 1
                after = abs(station.value[1] - ds.value[0]) # intersection to destination on line 2
            else:
                before = abs(station.value[1] - cs.value[0]) # current to intersection on line 2
                after = abs(station.value[0] - ds.value[0]) # intersection to destination on line 1

            routeOptions.append((before, after, before + after, station.value[2]))

        print("\nMultiple route options found:")

        for index, (before, after, total, intersectionPoint) in enumerate(routeOptions, start=1):
            print(
                f'{index}. '
                f'{cs.value[1]} --> {before} stop{"s" if before != 1 else " "} --> '
                f'switch at {intersectionPoint:<11} station --> '
                f'{after} stop{"s" if after != 1 else " "} --> {ds.value[1]} '
                f'— Total: {total} stop{"s" if total != 1 else ""}'
            )

        choice = int(input("\nPlease enter the number of your preferred route: ")) - 1
        stationsBeforeIntersection, stationsAfterIntersection, totalStationsNumber, intersectionPoint = routeOptions[choice]

        print(
            f"\nYour trip includes "
            f"{stationsBeforeIntersection} stop{'s' if stationsBeforeIntersection != 1 else ''} "
            f"before the intersection '{intersectionPoint}' station "
            f"and {stationsAfterIntersection} stop{'s' if stationsAfterIntersection != 1 else ''} afterwards, "
            f"with a total of {totalStationsNumber} stop{'s' if totalStationsNumber != 1 else ''}."
            f"\nEnjoy your ride!"
        )

def main():
    engine = MetroTicket()
    # print(engine.get_rules())
    engine.reset()
    engine.declare(NoStationFact()) 
    engine.run()

if __name__ == "__main__":
    main()
