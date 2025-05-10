from experta import Fact, KnowledgeEngine, Rule, NOT, AND, OR

from FirstLineFacts import *
from SecondLineFacts import *
from StationsOfIntersectionFacts import *
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

        currentStation = int(input("\nPlease enter your current station:"))
        destinationStation = int(input("Please enter your destination station:"))

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

def main():
    engine = MetroTicket()
    print(engine.get_rules())
    engine.reset()
    engine.declare(NoStationFact()) 
    engine.run()

if __name__ == "__main__":
    main()
