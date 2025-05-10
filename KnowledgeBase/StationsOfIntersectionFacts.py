from experta import Fact
from enum import Enum

class NoStationFact(Fact):
    pass

class AlShohadaaStationFact(Fact):
    pass
class SadatStationFact(Fact):
    pass

class StationsOfIntersection(Enum):
    AlShohadaa = (1, "Al Shohadaa", AlShohadaaStationFact())
    Sadat = (2, "Sadat", SadatStationFact())

