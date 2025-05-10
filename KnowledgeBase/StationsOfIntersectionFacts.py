from experta import Fact
from enum import Enum

class SadatIntersectionStationFact(Fact):
    pass
class AlShohadaaIntersectionStationFact(Fact):
    pass

class StationsOfIntersection(Enum):
    Sadat = (19, 10, "Sadat", SadatIntersectionStationFact())
    AlShohadaa = (22, 13, "Al Shohadaa", AlShohadaaIntersectionStationFact())

