from experta import Fact
from enum import Enum

class HelwanStationFact(Fact):
    pass
class AinHelwanStationFact(Fact):
    pass
class HelwanUniversityStationFact(Fact):
    pass
class WadiHofStationFact(Fact):
    pass
class HadayeqHelwanStationFact(Fact):
    pass
class ElMaasaraStationFact(Fact):
    pass
class ToraElAsmantStationFact(Fact):
    pass
class KozzikaStationFact(Fact):
    pass
class ToraElBaladStationFact(Fact):
    pass
class ThakanatElMaadiStationFact(Fact):
    pass
class MaadiStationFact(Fact):
    pass
class HadayeqElMaadiStationFact(Fact):
    pass
class DarElSalamStationFact(Fact):
    pass
class ElZahraaStationFact(Fact):
    pass
class MarGirgisStationFact(Fact):
    pass
class ElMalekElSalehStationFact(Fact):
    pass
class AlSayyedaZeinabStationFact(Fact):
    pass
class SaadZaghloulStationFact(Fact):
    pass
class SadatStationFact(Fact):
    pass
class NaserStationFact(Fact):
    pass
class UrabiStationFact(Fact):
    pass
class AlShohadaaStationFact(Fact):
    pass
class GhamraStationFact(Fact):
    pass
class ElDemerdashStationFact(Fact):
    pass
class ManshietElSadrStationFact(Fact):
    pass
class KobriElQobbaStationFact(Fact):
    pass
class HammamatElQobbaStationFact(Fact):
    pass
class SarayElQobbaStationFact(Fact):
    pass
class HadayeqElZaitounStationFact(Fact):
    pass
class HelmeyetElZaitounStationFact(Fact):
    pass
class ElMatareyyaStationFact(Fact):
    pass
class AinShamsStationFact(Fact):
    pass
class EzbetElNakhlStationFact(Fact):
    pass
class ElMargStationFact(Fact):
    pass
class NewElMargStationFact(Fact):
    pass

class FirstLine(Enum):
    Helwan = (1, "Helwan", HelwanStationFact())
    AinHelwan = (2, "Ain Helwan", AinHelwanStationFact())
    HelwanUniversity = (3, "Helwan University", HelwanUniversityStationFact())
    WadiHof = (4, "Wadi Hof", WadiHofStationFact())
    HadayeqHelwan = (5, "Hadayeq Helwan", HadayeqHelwanStationFact())
    ElMaasara = (6, "El Maasara", ElMaasaraStationFact())
    ToraElAsmant = (7, "Tora ElAsmant", ToraElAsmantStationFact())
    Kozzika = (8, "Kozzika", KozzikaStationFact())
    ToraElBalad = (9, "Tora ElBalad", ToraElBaladStationFact())
    ThakanatElMaadi = (10, "Thakanat ElMaadi", ThakanatElMaadiStationFact())
    Maadi = (11, "Maadi", MaadiStationFact())
    HadayeqElMaadi = (12, "Hadayeq ElMaadi", HadayeqElMaadiStationFact())
    DarElSalam = (13, "Dar ElSalam", DarElSalamStationFact())
    ElZahraa = (14, "ElZahraa'", ElZahraaStationFact())
    MarGirgis = (15, "Mar Girgis", MarGirgisStationFact())
    ElMalekElSaleh = (16, "ElMalek ElSaleh", ElMalekElSalehStationFact())
    AlSayyedaZeinab = (17, "AlSayyeda Zeinab", AlSayyedaZeinabStationFact())
    SaadZaghloul = (18, "Saad Zaghloul (Downtown)", SaadZaghloulStationFact())
    Sadat = (19, "Sadat", SadatStationFact())
    Naser = (20, "Naser (El Asaaf)", NaserStationFact())
    Urabi = (21, "Urabi", UrabiStationFact())
    AlShohadaa = (22, "Al Shohadaa (ramses)", AlShohadaaStationFact())
    Ghamra = (23, "Ghamra", GhamraStationFact())
    ElDemerdash = (24, "ElDemerdash", ElDemerdashStationFact())
    ManshietElSadr = (25, "Manshiet ElSadr", ManshietElSadrStationFact())
    KobriElQobba = (26, "Kobri ElQobba", KobriElQobbaStationFact())
    HammamatElQobba = (27, "Hammamat ElQobba", HammamatElQobbaStationFact())
    SarayElQobba = (28, "Saray ElQobba", SarayElQobbaStationFact())
    HadayeqElZaitoun = (29, "Hadayeq ElZaitoun", HadayeqElZaitounStationFact())
    HelmeyetElZaitoun = (30, "Helmeyet ElZaitoun", HelmeyetElZaitounStationFact())
    ElMatareyya = (31, "ElMatareyya", ElMatareyyaStationFact())
    AinShams = (32, "Ain Shams", AinShamsStationFact())
    EzbetElNakhl = (33, "Ezbet ElNakhl", EzbetElNakhlStationFact())
    ElMarg = (34, "ElMarg", ElMargStationFact())
    NewElMarg = (35, "New ElMarg", NewElMargStationFact())