from experta import Fact

class NoStationFact(Fact):
    pass
class SameLinesFact(Fact):
    pass
class DifferentLinesFact(Fact):
    pass

class FinalStationSelectionFact(Fact):
    CurrentStation = None
    DestinationStation = None

class TicketPriceSelectionFact(Fact):
    StationsNumber = None