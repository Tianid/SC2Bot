import enum



# 45 unic units (0-44)


class Terran(enum.IntEnum):
  """Terran units."""
  Armory = 29
  Barracks = 21
  BarracksReactor = 38
  BarracksTechLab = 37
  CommandCenter = 18
  EngineeringBay = 22
  Factory = 27
  FactoryReactor = 40
  FactoryTechLab = 39
  FusionCore = 30
  GhostAcademy = 26
  OrbitalCommand = 132
  PlanetaryFortress = 130
  Reactor = 6
  Starport = 28
  StarportReactor = 42
  StarportTechLab = 41
  TechLab = 5

class Protoss(enum.IntEnum):
  """Protoss units."""
  CyberneticsCore = 72
  DarkShrine = 69
  FleetBeacon = 64
  Forge = 63
  Gateway = 62
  Nexus = 59
  RoboticsBay = 70
  RoboticsFacility = 71
  Stargate = 67
  TemplarArchive = 68
  TwilightCouncil = 65
  WarpGate = 133
  ShieldBattery = 1910

class Zerg(enum.IntEnum):
  """Zerg units."""
  BanelingNest = 96
  EvolutionChamber = 90
  GreaterSpire = 102
  Hatchery = 86
  Hive = 101
  HydraliskDen = 91
  InfestationPit = 94
  Lair = 100
  LurkerDen = 504
  NydusNetwork = 95
  RoachWarren = 97
  SpawningPool = 89
  Spire = 92
  UltraliskCavern = 93
