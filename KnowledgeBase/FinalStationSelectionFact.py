from experta import Fact
from enum import Enum

class NoStationFact(Fact):
    pass
class SameLinesFact(Fact):
    pass
class DifferentLinesFact(Fact):
    pass

class FinalStationSelectionFact(Fact):
    CurrentStation = None
    DestinationStation = None