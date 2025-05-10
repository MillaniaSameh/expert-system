from experta import Fact
from enum import Enum

class ElMounibStationFact(Fact):
    pass
class SakiatMekkiStationFact(Fact):
    pass
class OmmElMisryeenStationFact(Fact):
    pass
class GizaStationFact(Fact):
    pass
class FaisalStationFact(Fact):
    pass
class CairoUniversityStationFact(Fact):
    pass
class ElBehoosStationFact(Fact):
    pass
class DokkiStationFact(Fact):
    pass
class OperaStationFact(Fact):
    pass
class SadatStationFact(Fact):
    pass
class NaguibStationFact(Fact):
    pass
class AtabaStationFact(Fact):
    pass
class AlShohadaaStationFact(Fact):
    pass
class MassaraStationFact(Fact):
    pass
class RoadElfaragStationFact(Fact):
    pass
class SaintTeresaStationFact(Fact):
    pass
class KhalafawyStationFact(Fact):
    pass
class MezallatStationFact(Fact):
    pass
class KolietElZeraaStationFact(Fact):
    pass
class ShobraElKheimaStationFact(Fact):
    pass

class SecondLine(Enum):
    ElMounib = (1, "El Mounib", ElMounibStationFact())
    SakiatMekki = (2, "Sakiat Mekki", SakiatMekkiStationFact())
    OmmElMisryeen = (3, "Omm el Misryeen", OmmElMisryeenStationFact())
    Giza = (4, "Giza", GizaStationFact())
    Faisal = (5, "Faisal", FaisalStationFact())
    CairoUniversity = (6, "Cairo University", CairoUniversityStationFact())
    ElBehoos = (7, "El Behoos", ElBehoosStationFact())
    Dokki = (8, "Dokki", DokkiStationFact())
    Opera = (9, "Opera", OperaStationFact())
    Sadat = (10, "Sadat (Tahrir)", SadatStationFact())
    Naguib = (11, "Naguib", NaguibStationFact())
    Ataba = (12, "Ataba", AtabaStationFact())
    AlShohadaa = (13, "Al Shohadaa (ramses)", AlShohadaaStationFact())
    Massara = (14, "Massara", MassaraStationFact())
    RoadElfarag = (15, "Road Elfarag", RoadElfaragStationFact())
    SaintTeresa = (16, "Saint Teresa", SaintTeresaStationFact())
    Khalafawy = (17, "Khalafawy", KhalafawyStationFact())
    Mezallat = (18, "Mezallat", MezallatStationFact())
    KolietElZeraa = (19, "Koliet ElZeraa", KolietElZeraaStationFact())
    ShobraElKheima = (20, "Shobra ElKheima", ShobraElKheimaStationFact())