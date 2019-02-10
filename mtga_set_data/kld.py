""" WARNING! These cards are no longer in MTGA! This file is likely incorrect, and is left only for reference.

"""

import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


AcrobaticManeuver = Card("acrobatic_maneuver", "Acrobatic Maneuver", ['2', 'W'], ['W'], "Instant", "", "KLD", "Common", 1, 63641)
AerialResponder = Card("aerial_responder", "Aerial Responder", ['1', 'W', 'W'], ['W'], "Creature", "Dwarf Soldier", "KLD", "Uncommon", 2, 63643)
AetherstormRoc = Card("aetherstorm_roc", "Aetherstorm Roc", ['2', 'W', 'W'], ['W'], "Creature", "Bird", "KLD", "Rare", 3, 63645)
AngelofInvention = Card("angel_of_invention", "Angel of Invention", ['3', 'W', 'W'], ['W'], "Creature", "Angel", "KLD", "Mythic Rare", 4, 63647)
AuthorityoftheConsuls = Card("authority_of_the_consuls", "Authority of the Consuls", ['W'], ['W'], "Enchantment", "", "KLD", "Rare", 5, 63649)
AviaryMechanic = Card("aviary_mechanic", "Aviary Mechanic", ['1', 'W'], ['W'], "Creature", "Dwarf Artificer", "KLD", "Common", 6, 63651)
BuilttoLast = Card("built_to_last", "Built to Last", ['W'], ['W'], "Instant", "", "KLD", "Common", 7, 63653)
CapturedbytheConsulate = Card("captured_by_the_consulate", "Captured by the Consulate", ['3', 'W'], ['W'], "Enchantment", "Aura", "KLD", "Rare", 8, 63655)
CataclysmicGearhulk = Card("cataclysmic_gearhulk", "Cataclysmic Gearhulk", ['3', 'W', 'W'], ['W'], "Artifact Creature", "Construct", "KLD", "Mythic Rare", 9, 63657)
ConsulateSurveillance = Card("consulate_surveillance", "Consulate Surveillance", ['3', 'W'], ['W'], "Enchantment", "", "KLD", "Uncommon", 10, 63659)
ConsulsShieldguard = Card("consuls_shieldguard", "Consul's Shieldguard", ['3', 'W'], ['W'], "Creature", "Dwarf Soldier", "KLD", "Uncommon", 11, 63661)
EddytrailHawk = Card("eddytrail_hawk", "Eddytrail Hawk", ['1', 'W'], ['W'], "Creature", "Bird", "KLD", "Common", 12, 63663)
FairgroundsWarden = Card("fairgrounds_warden", "Fairgrounds Warden", ['2', 'W'], ['W'], "Creature", "Dwarf Soldier", "KLD", "Uncommon", 13, 63665)
Fragmentize = Card("fragmentize", "Fragmentize", ['W'], ['W'], "Sorcery", "", "KLD", "Common", 14, 63667)
Fumigate = Card("fumigate", "Fumigate", ['3', 'W', 'W'], ['W'], "Sorcery", "", "KLD", "Rare", 15, 63669)
GearshiftAce = Card("gearshift_ace", "Gearshift Ace", ['1', 'W'], ['W'], "Creature", "Dwarf Pilot", "KLD", "Uncommon", 16, 63671)
GlintSleeveArtisan = Card("glintsleeve_artisan", "Glint-Sleeve Artisan", ['2', 'W'], ['W'], "Creature", "Dwarf Artificer", "KLD", "Common", 17, 63673)
HeraldoftheFair = Card("herald_of_the_fair", "Herald of the Fair", ['2', 'W'], ['W'], "Creature", "Human", "KLD", "Common", 18, 63675)
ImpeccableTiming = Card("impeccable_timing", "Impeccable Timing", ['1', 'W'], ['W'], "Instant", "", "KLD", "Common", 19, 63677)
InspiredCharge = Card("inspired_charge", "Inspired Charge", ['2', 'W', 'W'], ['W'], "Instant", "", "KLD", "Common", 20, 63679)
MasterTrinketeer = Card("master_trinketeer", "Master Trinketeer", ['2', 'W'], ['W'], "Creature", "Dwarf Artificer", "KLD", "Rare", 21, 63681)
NinthBridgePatrol = Card("ninth_bridge_patrol", "Ninth Bridge Patrol", ['1', 'W'], ['W'], "Creature", "Dwarf Soldier", "KLD", "Common", 22, 63683)
PressurePoint = Card("pressure_point", "Pressure Point", ['1', 'W'], ['W'], "Instant", "", "KLD", "Common", 23, 63685)
PropellerPioneer = Card("propeller_pioneer", "Propeller Pioneer", ['3', 'W'], ['W'], "Creature", "Human Artificer", "KLD", "Common", 24, 63687)
Refurbish = Card("refurbish", "Refurbish", ['3', 'W'], ['W'], "Sorcery", "", "KLD", "Uncommon", 25, 63689)
RevokePrivileges = Card("revoke_privileges", "Revoke Privileges", ['2', 'W'], ['W'], "Enchantment", "Aura", "KLD", "Common", 26, 63691)
ServoExhibition = Card("servo_exhibition", "Servo Exhibition", ['1', 'W'], ['W'], "Sorcery", "", "KLD", "Uncommon", 27, 63693)
SkyswirlHarrier = Card("skyswirl_harrier", "Skyswirl Harrier", ['4', 'W'], ['W'], "Creature", "Bird", "KLD", "Common", 28, 63695)
SkywhalersShot = Card("skywhalers_shot", "Skywhaler's Shot", ['2', 'W'], ['W'], "Instant", "", "KLD", "Uncommon", 29, 63697)
TasseledDromedary = Card("tasseled_dromedary", "Tasseled Dromedary", ['W'], ['W'], "Creature", "Camel", "KLD", "Common", 30, 63699)
ThrivingIbex = Card("thriving_ibex", "Thriving Ibex", ['3', 'W'], ['W'], "Creature", "Goat", "KLD", "Common", 31, 63701)
ToolcraftExemplar = Card("toolcraft_exemplar", "Toolcraft Exemplar", ['W'], ['W'], "Creature", "Dwarf Artificer", "KLD", "Rare", 32, 63703)
TrustyCompanion = Card("trusty_companion", "Trusty Companion", ['1', 'W'], ['W'], "Creature", "Hyena", "KLD", "Uncommon", 33, 63705)
VisionaryAugmenter = Card("visionary_augmenter", "Visionary Augmenter", ['2', 'W', 'W'], ['W'], "Creature", "Dwarf Artificer", "KLD", "Uncommon", 34, 63707)
WispweaverAngel = Card("wispweaver_angel", "Wispweaver Angel", ['4', 'W', 'W'], ['W'], "Creature", "Angel", "KLD", "Uncommon", 35, 63709)
AetherMeltdown = Card("aether_meltdown", "Aether Meltdown", ['1', 'U'], ['U'], "Enchantment", "Aura", "KLD", "Uncommon", 36, 63711)
AetherTheorist = Card("aether_theorist", "Aether Theorist", ['1', 'U'], ['U'], "Creature", "Vedalken Rogue", "KLD", "Common", 37, 63713)
AetherTradewinds = Card("aether_tradewinds", "Aether Tradewinds", ['2', 'U'], ['U'], "Instant", "", "KLD", "Common", 38, 63715)
AethersquallAncient = Card("aethersquall_ancient", "Aethersquall Ancient", ['5', 'U', 'U'], ['U'], "Creature", "Leviathan", "KLD", "Rare", 39, 63717)
CeremoniousRejection = Card("ceremonious_rejection", "Ceremonious Rejection", ['U'], ['U'], "Instant", "", "KLD", "Uncommon", 40, 63719)
ConfiscationCoup = Card("confiscation_coup", "Confiscation Coup", ['3', 'U', 'U'], ['U'], "Sorcery", "", "KLD", "Rare", 41, 63721)
CurioVendor = Card("curio_vendor", "Curio Vendor", ['1', 'U'], ['U'], "Creature", "Vedalken", "KLD", "Common", 42, 63723)
DisappearingAct = Card("disappearing_act", "Disappearing Act", ['1', 'U', 'U'], ['U'], "Instant", "", "KLD", "Uncommon", 43, 63725)
DramaticReversal = Card("dramatic_reversal", "Dramatic Reversal", ['1', 'U'], ['U'], "Instant", "", "KLD", "Common", 44, 63727)
EraofInnovation = Card("era_of_innovation", "Era of Innovation", ['1', 'U'], ['U'], "Enchantment", "", "KLD", "Uncommon", 45, 63729)
ExperimentalAviator = Card("experimental_aviator", "Experimental Aviator", ['3', 'U', 'U'], ['U'], "Creature", "Human Artificer", "KLD", "Uncommon", 46, 63731)
FailedInspection = Card("failed_inspection", "Failed Inspection", ['2', 'U', 'U'], ['U'], "Instant", "", "KLD", "Common", 47, 63733)
GearseekerSerpent = Card("gearseeker_serpent", "Gearseeker Serpent", ['5', 'U', 'U'], ['U'], "Creature", "Serpent", "KLD", "Common", 48, 63735)
GlimmerofGenius = Card("glimmer_of_genius", "Glimmer of Genius", ['3', 'U'], ['U'], "Instant", "", "KLD", "Uncommon", 49, 63737)
GlintNestCrane = Card("glintnest_crane", "Glint-Nest Crane", ['1', 'U'], ['U'], "Creature", "Bird", "KLD", "Uncommon", 50, 63739)
HightideHermit = Card("hightide_hermit", "Hightide Hermit", ['4', 'U'], ['U'], "Creature", "Crab", "KLD", "Common", 51, 63741)
InsidiousWill = Card("insidious_will", "Insidious Will", ['2', 'U', 'U'], ['U'], "Instant", "", "KLD", "Rare", 52, 63743)
JanjeetSentry = Card("janjeet_sentry", "Janjeet Sentry", ['2', 'U'], ['U'], "Creature", "Vedalken Soldier", "KLD", "Uncommon", 53, 63745)
LongFinnedSkywhale = Card("longfinned_skywhale", "Long-Finned Skywhale", ['2', 'U', 'U'], ['U'], "Creature", "Whale", "KLD", "Uncommon", 54, 63747)
Malfunction = Card("malfunction", "Malfunction", ['3', 'U'], ['U'], "Enchantment", "Aura", "KLD", "Common", 55, 63749)
MetallurgicSummonings = Card("metallurgic_summonings", "Metallurgic Summonings", ['3', 'U', 'U'], ['U'], "Enchantment", "", "KLD", "Mythic Rare", 56, 63751)
MinisterofInquiries = Card("minister_of_inquiries", "Minister of Inquiries", ['U'], ['U'], "Creature", "Vedalken Advisor", "KLD", "Uncommon", 57, 63753)
NimbleInnovator = Card("nimble_innovator", "Nimble Innovator", ['3', 'U'], ['U'], "Creature", "Vedalken Artificer", "KLD", "Common", 58, 63755)
PadeemConsulofInnovation = Card("padeem_consul_of_innovation", "Padeem, Consul of Innovation", ['3', 'U'], ['U'], "Legendary Creature", "Vedalken Artificer", "KLD", "Rare", 59, 63757)
ParadoxicalOutcome = Card("paradoxical_outcome", "Paradoxical Outcome", ['3', 'U'], ['U'], "Instant", "", "KLD", "Rare", 60, 63759)
RevolutionaryRebuff = Card("revolutionary_rebuff", "Revolutionary Rebuff", ['1', 'U'], ['U'], "Instant", "", "KLD", "Common", 61, 63761)
SaheelisArtistry = Card("saheelis_artistry", "Saheeli's Artistry", ['4', 'U', 'U'], ['U'], "Sorcery", "", "KLD", "Rare", 62, 63763)
SelectforInspection = Card("select_for_inspection", "Select for Inspection", ['U'], ['U'], "Instant", "", "KLD", "Common", 63, 63765)
ShrewdNegotiation = Card("shrewd_negotiation", "Shrewd Negotiation", ['4', 'U'], ['U'], "Sorcery", "", "KLD", "Uncommon", 64, 63767)
TezzeretsAmbition = Card("tezzerets_ambition", "Tezzeret's Ambition", ['3', 'U', 'U'], ['U'], "Sorcery", "", "KLD", "Common", 65, 63769)
ThrivingTurtle = Card("thriving_turtle", "Thriving Turtle", ['U'], ['U'], "Creature", "Turtle", "KLD", "Common", 66, 63771)
TorrentialGearhulk = Card("torrential_gearhulk", "Torrential Gearhulk", ['4', 'U', 'U'], ['U'], "Artifact Creature", "Construct", "KLD", "Mythic Rare", 67, 63773)
VedalkenBlademaster = Card("vedalken_blademaster", "Vedalken Blademaster", ['2', 'U'], ['U'], "Creature", "Vedalken Soldier", "KLD", "Common", 68, 63775)
WeldfastWingsmith = Card("weldfast_wingsmith", "Weldfast Wingsmith", ['3', 'U'], ['U'], "Creature", "Human Artificer", "KLD", "Common", 69, 63777)
WindDrake = Card("wind_drake", "Wind Drake", ['2', 'U'], ['U'], "Creature", "Drake", "KLD", "Common", 70, 63779)
AetherbornMarauder = Card("aetherborn_marauder", "Aetherborn Marauder", ['3', 'B'], ['B'], "Creature", "Aetherborn Rogue", "KLD", "Uncommon", 71, 63781)
AmbitiousAetherborn = Card("ambitious_aetherborn", "Ambitious Aetherborn", ['4', 'B'], ['B'], "Creature", "Aetherborn Artificer", "KLD", "Common", 72, 63783)
DemonofDarkSchemes = Card("demon_of_dark_schemes", "Demon of Dark Schemes", ['3', 'B', 'B', 'B'], ['B'], "Creature", "Demon", "KLD", "Mythic Rare", 73, 63785)
DhundOperative = Card("dhund_operative", "Dhund Operative", ['1', 'B'], ['B'], "Creature", "Human Rogue", "KLD", "Common", 74, 63787)
DiabolicTutor = Card("diabolic_tutor", "Diabolic Tutor", ['2', 'B', 'B'], ['B'], "Sorcery", "", "KLD", "Uncommon", 75, 63789)
DieYoung = Card("die_young", "Die Young", ['1', 'B'], ['B'], "Sorcery", "", "KLD", "Common", 76, 63791)
DukharaScavenger = Card("dukhara_scavenger", "Dukhara Scavenger", ['5', 'B'], ['B'], "Creature", "Crocodile", "KLD", "Common", 77, 63793)
EliminatetheCompetition = Card("eliminate_the_competition", "Eliminate the Competition", ['4', 'B'], ['B'], "Sorcery", "", "KLD", "Rare", 78, 63795)
EmbraalBruiser = Card("embraal_bruiser", "Embraal Bruiser", ['1', 'B'], ['B'], "Creature", "Human Warrior", "KLD", "Uncommon", 79, 63797)
EssenceExtraction = Card("essence_extraction", "Essence Extraction", ['1', 'B', 'B'], ['B'], "Instant", "", "KLD", "Uncommon", 80, 63799)
FortuitousFind = Card("fortuitous_find", "Fortuitous Find", ['2', 'B'], ['B'], "Sorcery", "", "KLD", "Common", 81, 63801)
FoundryScreecher = Card("foundry_screecher", "Foundry Screecher", ['2', 'B'], ['B'], "Creature", "Bat", "KLD", "Common", 82, 63803)
FretworkColony = Card("fretwork_colony", "Fretwork Colony", ['1', 'B'], ['B'], "Creature", "Insect", "KLD", "Uncommon", 83, 63805)
GontiLordofLuxury = Card("gonti_lord_of_luxury", "Gonti, Lord of Luxury", ['2', 'B', 'B'], ['B'], "Legendary Creature", "Aetherborn Rogue", "KLD", "Rare", 84, 63807)
HarshScrutiny = Card("harsh_scrutiny", "Harsh Scrutiny", ['B'], ['B'], "Sorcery", "", "KLD", "Uncommon", 85, 63809)
LawlessBroker = Card("lawless_broker", "Lawless Broker", ['2', 'B'], ['B'], "Creature", "Aetherborn Rogue", "KLD", "Common", 86, 63811)
LiveFast = Card("live_fast", "Live Fast", ['2', 'B'], ['B'], "Sorcery", "", "KLD", "Common", 87, 63813)
LostLegacy = Card("lost_legacy", "Lost Legacy", ['1', 'B', 'B'], ['B'], "Sorcery", "", "KLD", "Rare", 88, 63815)
MakeObsolete = Card("make_obsolete", "Make Obsolete", ['2', 'B'], ['B'], "Instant", "", "KLD", "Uncommon", 89, 63817)
MarionetteMaster = Card("marionette_master", "Marionette Master", ['4', 'B', 'B'], ['B'], "Creature", "Human Artificer", "KLD", "Rare", 90, 63819)
MaulfistSquad = Card("maulfist_squad", "Maulfist Squad", ['3', 'B'], ['B'], "Creature", "Human Artificer", "KLD", "Common", 91, 63821)
MidnightOil = Card("midnight_oil", "Midnight Oil", ['2', 'B', 'B'], ['B'], "Enchantment", "", "KLD", "Rare", 92, 63823)
MindRot = Card("mind_rot", "Mind Rot", ['2', 'B'], ['B'], "Sorcery", "", "KLD", "Common", 93, 63825)
MorbidCuriosity = Card("morbid_curiosity", "Morbid Curiosity", ['1', 'B', 'B'], ['B'], "Sorcery", "", "KLD", "Uncommon", 94, 63827)
NightMarketLookout = Card("night_market_lookout", "Night Market Lookout", ['B'], ['B'], "Creature", "Human Rogue", "KLD", "Common", 95, 63829)
NoxiousGearhulk = Card("noxious_gearhulk", "Noxious Gearhulk", ['4', 'B', 'B'], ['B'], "Artifact Creature", "Construct", "KLD", "Mythic Rare", 96, 63831)
OvalchaseDaredevil = Card("ovalchase_daredevil", "Ovalchase Daredevil", ['3', 'B'], ['B'], "Creature", "Human Pilot", "KLD", "Uncommon", 97, 63833)
PrakhataClubSecurity = Card("prakhata_club_security", "Prakhata Club Security", ['3', 'B'], ['B'], "Creature", "Aetherborn Warrior", "KLD", "Common", 98, 63835)
RushofVitality = Card("rush_of_vitality", "Rush of Vitality", ['1', 'B'], ['B'], "Instant", "", "KLD", "Common", 99, 63837)
SubtleStrike = Card("subtle_strike", "Subtle Strike", ['1', 'B'], ['B'], "Instant", "", "KLD", "Common", 100, 63839)
SyndicateTrafficker = Card("syndicate_trafficker", "Syndicate Trafficker", ['1', 'B'], ['B'], "Creature", "Aetherborn Rogue", "KLD", "Rare", 101, 63841)
ThrivingRats = Card("thriving_rats", "Thriving Rats", ['1', 'B'], ['B'], "Creature", "Rat", "KLD", "Common", 102, 63843)
TidyConclusion = Card("tidy_conclusion", "Tidy Conclusion", ['3', 'B', 'B'], ['B'], "Instant", "", "KLD", "Common", 103, 63845)
UnderhandedDesigns = Card("underhanded_designs", "Underhanded Designs", ['1', 'B'], ['B'], "Enchantment", "", "KLD", "Uncommon", 104, 63847)
WeaponcraftEnthusiast = Card("weaponcraft_enthusiast", "Weaponcraft Enthusiast", ['2', 'B'], ['B'], "Creature", "Aetherborn Artificer", "KLD", "Uncommon", 105, 63849)
AethertorchRenegade = Card("aethertorch_renegade", "Aethertorch Renegade", ['2', 'R'], ['R'], "Creature", "Human Rogue", "KLD", "Uncommon", 106, 63851)
BrazenScourge = Card("brazen_scourge", "Brazen Scourge", ['1', 'R', 'R'], ['R'], "Creature", "Gremlin", "KLD", "Uncommon", 107, 63853)
BuilttoSmash = Card("built_to_smash", "Built to Smash", ['R'], ['R'], "Instant", "", "KLD", "Common", 108, 63855)
CatharticReunion = Card("cathartic_reunion", "Cathartic Reunion", ['1', 'R'], ['R'], "Sorcery", "", "KLD", "Common", 109, 63857)
ChandraTorchofDefiance = Card("chandra_torch_of_defiance", "Chandra, Torch of Defiance", ['2', 'R', 'R'], ['R'], "Legendary Planeswalker", "Chandra", "KLD", "Mythic Rare", 110, 63859)
ChandrasPyrohelix = Card("chandras_pyrohelix", "Chandra's Pyrohelix", ['1', 'R'], ['R'], "Instant", "", "KLD", "Common", 111, 63861)
CombustibleGearhulk = Card("combustible_gearhulk", "Combustible Gearhulk", ['4', 'R', 'R'], ['R'], "Artifact Creature", "Construct", "KLD", "Mythic Rare", 112, 63863)
Demolish = Card("demolish", "Demolish", ['3', 'R'], ['R'], "Sorcery", "", "KLD", "Common", 113, 63865)
FatefulShowdown = Card("fateful_showdown", "Fateful Showdown", ['2', 'R', 'R'], ['R'], "Instant", "", "KLD", "Rare", 114, 63867)
FuriousReprisal = Card("furious_reprisal", "Furious Reprisal", ['3', 'R'], ['R'], "Sorcery", "", "KLD", "Uncommon", 115, 63869)
GiantSpectacle = Card("giant_spectacle", "Giant Spectacle", ['1', 'R'], ['R'], "Enchantment", "Aura", "KLD", "Common", 116, 63871)
HarnessedLightning = Card("harnessed_lightning", "Harnessed Lightning", ['1', 'R'], ['R'], "Instant", "", "KLD", "Uncommon", 117, 63873)
Hijack = Card("hijack", "Hijack", ['1', 'R', 'R'], ['R'], "Sorcery", "", "KLD", "Common", 118, 63875)
IncendiarySabotage = Card("incendiary_sabotage", "Incendiary Sabotage", ['2', 'R', 'R'], ['R'], "Instant", "", "KLD", "Uncommon", 119, 63877)
InventorsApprentice = Card("inventors_apprentice", "Inventor's Apprentice", ['R'], ['R'], "Creature", "Human Artificer", "KLD", "Uncommon", 120, 63879)
LathnuHellion = Card("lathnu_hellion", "Lathnu Hellion", ['2', 'R'], ['R'], "Creature", "Hellion", "KLD", "Rare", 121, 63881)
MadcapExperiment = Card("madcap_experiment", "Madcap Experiment", ['3', 'R'], ['R'], "Sorcery", "", "KLD", "Rare", 122, 63883)
MaulfistDoorbuster = Card("maulfist_doorbuster", "Maulfist Doorbuster", ['3', 'R'], ['R'], "Creature", "Human Warrior", "KLD", "Uncommon", 123, 63885)
PiaNalaar = Card("pia_nalaar", "Pia Nalaar", ['2', 'R'], ['R'], "Legendary Creature", "Human Artificer", "KLD", "Rare", 124, 63887)
QuicksmithGenius = Card("quicksmith_genius", "Quicksmith Genius", ['2', 'R'], ['R'], "Creature", "Human Artificer", "KLD", "Uncommon", 125, 63889)
RecklessFireweaver = Card("reckless_fireweaver", "Reckless Fireweaver", ['1', 'R'], ['R'], "Creature", "Human Artificer", "KLD", "Common", 126, 63891)
RenegadeTactics = Card("renegade_tactics", "Renegade Tactics", ['R'], ['R'], "Sorcery", "", "KLD", "Common", 127, 63893)
RuinousGremlin = Card("ruinous_gremlin", "Ruinous Gremlin", ['R'], ['R'], "Creature", "Gremlin", "KLD", "Common", 128, 63895)
SalivatingGremlins = Card("salivating_gremlins", "Salivating Gremlins", ['2', 'R'], ['R'], "Creature", "Gremlin", "KLD", "Common", 129, 63897)
SkyshipStalker = Card("skyship_stalker", "Skyship Stalker", ['2', 'R', 'R'], ['R'], "Creature", "Dragon", "KLD", "Rare", 130, 63899)
SparkofCreativity = Card("spark_of_creativity", "Spark of Creativity", ['R'], ['R'], "Sorcery", "", "KLD", "Uncommon", 131, 63901)
SpeedwayFanatic = Card("speedway_fanatic", "Speedway Fanatic", ['1', 'R'], ['R'], "Creature", "Human Pilot", "KLD", "Uncommon", 132, 63903)
SpiresideInfiltrator = Card("spireside_infiltrator", "Spireside Infiltrator", ['2', 'R'], ['R'], "Creature", "Human Rogue", "KLD", "Common", 133, 63905)
SpontaneousArtist = Card("spontaneous_artist", "Spontaneous Artist", ['3', 'R'], ['R'], "Creature", "Human Rogue", "KLD", "Common", 134, 63907)
StartYourEngines = Card("start_your_engines", "Start Your Engines", ['3', 'R'], ['R'], "Sorcery", "", "KLD", "Uncommon", 135, 63909)
TerritorialGorger = Card("territorial_gorger", "Territorial Gorger", ['3', 'R'], ['R'], "Creature", "Gremlin", "KLD", "Rare", 136, 63911)
TerroroftheFairgrounds = Card("terror_of_the_fairgrounds", "Terror of the Fairgrounds", ['3', 'R'], ['R'], "Creature", "Gremlin", "KLD", "Common", 137, 63913)
ThrivingGrubs = Card("thriving_grubs", "Thriving Grubs", ['1', 'R'], ['R'], "Creature", "Gremlin", "KLD", "Common", 138, 63915)
WaywardGiant = Card("wayward_giant", "Wayward Giant", ['4', 'R'], ['R'], "Creature", "Giant", "KLD", "Common", 139, 63917)
WeldingSparks = Card("welding_sparks", "Welding Sparks", ['2', 'R'], ['R'], "Instant", "", "KLD", "Common", 140, 63919)
AppetitefortheUnnatural = Card("appetite_for_the_unnatural", "Appetite for the Unnatural", ['2', 'G'], ['G'], "Instant", "", "KLD", "Common", 141, 63921)
ArborbackStomper = Card("arborback_stomper", "Arborback Stomper", ['3', 'G', 'G'], ['G'], "Creature", "Beast", "KLD", "Uncommon", 142, 63923)
ArchitectoftheUntamed = Card("architect_of_the_untamed", "Architect of the Untamed", ['2', 'G'], ['G'], "Creature", "Elf Artificer Druid", "KLD", "Rare", 143, 63925)
ArmorcraftJudge = Card("armorcraft_judge", "Armorcraft Judge", ['3', 'G'], ['G'], "Creature", "Elf Artificer", "KLD", "Uncommon", 144, 63927)
AttunewithAether = Card("attune_with_aether", "Attune with Aether", ['G'], ['G'], "Sorcery", "", "KLD", "Common", 145, 63929)
BlossomingDefense = Card("blossoming_defense", "Blossoming Defense", ['G'], ['G'], "Instant", "", "KLD", "Uncommon", 146, 63931)
BristlingHydra = Card("bristling_hydra", "Bristling Hydra", ['2', 'G', 'G'], ['G'], "Creature", "Hydra", "KLD", "Rare", 147, 63933)
CommencementofFestivities = Card("commencement_of_festivities", "Commencement of Festivities", ['1', 'G'], ['G'], "Instant", "", "KLD", "Common", 148, 63935)
CowlProwler = Card("cowl_prowler", "Cowl Prowler", ['4', 'G', 'G'], ['G'], "Creature", "Wurm", "KLD", "Common", 149, 63937)
CreepingMold = Card("creeping_mold", "Creeping Mold", ['2', 'G', 'G'], ['G'], "Sorcery", "", "KLD", "Uncommon", 150, 63939)
CultivatorofBlades = Card("cultivator_of_blades", "Cultivator of Blades", ['3', 'G', 'G'], ['G'], "Creature", "Elf Artificer", "KLD", "Rare", 151, 63941)
DubiousChallenge = Card("dubious_challenge", "Dubious Challenge", ['3', 'G'], ['G'], "Sorcery", "", "KLD", "Rare", 152, 63943)
DurableHandicraft = Card("durable_handicraft", "Durable Handicraft", ['1', 'G'], ['G'], "Enchantment", "", "KLD", "Uncommon", 153, 63945)
ElegantEdgecrafters = Card("elegant_edgecrafters", "Elegant Edgecrafters", ['4', 'G', 'G'], ['G'], "Creature", "Elf Artificer", "KLD", "Uncommon", 154, 63947)
FairgroundsTrumpeter = Card("fairgrounds_trumpeter", "Fairgrounds Trumpeter", ['2', 'G'], ['G'], "Creature", "Elephant", "KLD", "Uncommon", 155, 63949)
GhirapurGuide = Card("ghirapur_guide", "Ghirapur Guide", ['2', 'G'], ['G'], "Creature", "Elf Scout", "KLD", "Uncommon", 156, 63951)
HighspireArtisan = Card("highspire_artisan", "Highspire Artisan", ['2', 'G'], ['G'], "Creature", "Elf Artificer", "KLD", "Common", 157, 63953)
HunttheWeak = Card("hunt_the_weak", "Hunt the Weak", ['3', 'G'], ['G'], "Sorcery", "", "KLD", "Common", 158, 63955)
KujarSeedsculptor = Card("kujar_seedsculptor", "Kujar Seedsculptor", ['1', 'G'], ['G'], "Creature", "Elf Druid", "KLD", "Common", 159, 63957)
LargerThanLife = Card("larger_than_life", "Larger Than Life", ['1', 'G'], ['G'], "Sorcery", "", "KLD", "Common", 160, 63959)
LongtuskCub = Card("longtusk_cub", "Longtusk Cub", ['1', 'G'], ['G'], "Creature", "Cat", "KLD", "Uncommon", 161, 63961)
NaturesWay = Card("natures_way", "Nature's Way", ['1', 'G'], ['G'], "Sorcery", "", "KLD", "Uncommon", 162, 63963)
NissaVitalForce = Card("nissa_vital_force", "Nissa, Vital Force", ['3', 'G', 'G'], ['G'], "Legendary Planeswalker", "Nissa", "KLD", "Mythic Rare", 163, 63965)
OrnamentalCourage = Card("ornamental_courage", "Ornamental Courage", ['G'], ['G'], "Instant", "", "KLD", "Common", 164, 63967)
OviyaPashiriSageLifecrafter = Card("oviya_pashiri_sage_lifecrafter", "Oviya Pashiri, Sage Lifecrafter", ['G'], ['G'], "Legendary Creature", "Human Artificer", "KLD", "Rare", 165, 63969)
PeemaOutrider = Card("peema_outrider", "Peema Outrider", ['2', 'G', 'G'], ['G'], "Creature", "Elf Artificer", "KLD", "Common", 166, 63971)
RiparianTiger = Card("riparian_tiger", "Riparian Tiger", ['3', 'G', 'G'], ['G'], "Creature", "Cat", "KLD", "Common", 167, 63973)
SageofShailasClaim = Card("sage_of_shailas_claim", "Sage of Shaila's Claim", ['1', 'G'], ['G'], "Creature", "Elf Druid", "KLD", "Common", 168, 63975)
ServantoftheConduit = Card("servant_of_the_conduit", "Servant of the Conduit", ['1', 'G'], ['G'], "Creature", "Elf Druid", "KLD", "Uncommon", 169, 63977)
TakeDown = Card("take_down", "Take Down", ['G'], ['G'], "Sorcery", "", "KLD", "Common", 170, 63979)
ThrivingRhino = Card("thriving_rhino", "Thriving Rhino", ['2', 'G'], ['G'], "Creature", "Rhino", "KLD", "Common", 171, 63981)
VerdurousGearhulk = Card("verdurous_gearhulk", "Verdurous Gearhulk", ['3', 'G', 'G'], ['G'], "Artifact Creature", "Construct", "KLD", "Mythic Rare", 172, 63983)
WildWanderer = Card("wild_wanderer", "Wild Wanderer", ['3', 'G'], ['G'], "Creature", "Elf Druid", "KLD", "Common", 173, 63985)
WildestDreams = Card("wildest_dreams", "Wildest Dreams", ['X', 'X', 'G'], ['G'], "Sorcery", "", "KLD", "Rare", 174, 63987)
WilyBandar = Card("wily_bandar", "Wily Bandar", ['G'], ['G'], "Creature", "Cat Monkey", "KLD", "Common", 175, 63989)
Cloudblazer = Card("cloudblazer", "Cloudblazer", ['3', 'W', 'U'], ['W', 'U'], "Creature", "Human Scout", "KLD", "Uncommon", 176, 63991)
ContrabandKingpin = Card("contraband_kingpin", "Contraband Kingpin", ['U', 'B'], ['U', 'B'], "Creature", "Aetherborn Rogue", "KLD", "Uncommon", 177, 63993)
DepalaPilotExemplar = Card("depala_pilot_exemplar", "Depala, Pilot Exemplar", ['1', 'R', 'W'], ['W', 'R'], "Legendary Creature", "Dwarf Pilot", "KLD", "Rare", 178, 63995)
DovinBaan = Card("dovin_baan", "Dovin Baan", ['2', 'W', 'U'], ['W', 'U'], "Legendary Planeswalker", "Dovin", "KLD", "Mythic Rare", 179, 63997)
EmpyrealVoyager = Card("empyreal_voyager", "Empyreal Voyager", ['1', 'G', 'U'], ['U', 'G'], "Creature", "Vedalken Scout", "KLD", "Uncommon", 180, 63999)
EngineeredMight = Card("engineered_might", "Engineered Might", ['3', 'G', 'W'], ['W', 'G'], "Sorcery", "", "KLD", "Uncommon", 181, 64001)
HazardousConditions = Card("hazardous_conditions", "Hazardous Conditions", ['2', 'B', 'G'], ['B', 'G'], "Sorcery", "", "KLD", "Uncommon", 182, 64003)
KambalConsulofAllocation = Card("kambal_consul_of_allocation", "Kambal, Consul of Allocation", ['1', 'W', 'B'], ['W', 'B'], "Legendary Creature", "Human Advisor", "KLD", "Rare", 183, 64005)
RashmiEternitiesCrafter = Card("rashmi_eternities_crafter", "Rashmi, Eternities Crafter", ['2', 'G', 'U'], ['U', 'G'], "Legendary Creature", "Elf Druid", "KLD", "Mythic Rare", 184, 64007)
RestorationGearsmith = Card("restoration_gearsmith", "Restoration Gearsmith", ['2', 'W', 'B'], ['W', 'B'], "Creature", "Human Artificer", "KLD", "Uncommon", 185, 64009)
SaheeliRai = Card("saheeli_rai", "Saheeli Rai", ['1', 'U', 'R'], ['U', 'R'], "Legendary Planeswalker", "Saheeli", "KLD", "Mythic Rare", 186, 64011)
UnlicensedDisintegration = Card("unlicensed_disintegration", "Unlicensed Disintegration", ['1', 'B', 'R'], ['B', 'R'], "Instant", "", "KLD", "Uncommon", 187, 64013)
VeteranMotorist = Card("veteran_motorist", "Veteran Motorist", ['R', 'W'], ['W', 'R'], "Creature", "Dwarf Pilot", "KLD", "Uncommon", 188, 64015)
VoltaicBrawler = Card("voltaic_brawler", "Voltaic Brawler", ['R', 'G'], ['R', 'G'], "Creature", "Human Warrior", "KLD", "Uncommon", 189, 64017)
WhirlerVirtuoso = Card("whirler_virtuoso", "Whirler Virtuoso", ['1', 'U', 'R'], ['U', 'R'], "Creature", "Vedalken Artificer", "KLD", "Uncommon", 190, 64019)
AccomplishedAutomaton = Card("accomplished_automaton", "Accomplished Automaton", ['7'], [], "Artifact Creature", "Construct", "KLD", "Common", 191, 64021)
AetherfluxReservoir = Card("aetherflux_reservoir", "Aetherflux Reservoir", ['4'], [], "Artifact", "", "KLD", "Rare", 192, 64023)
AetherworksMarvel = Card("aetherworks_marvel", "Aetherworks Marvel", ['4'], [], "Legendary Artifact", "", "KLD", "Mythic Rare", 193, 64025)
AnimationModule = Card("animation_module", "Animation Module", ['1'], [], "Artifact", "", "KLD", "Rare", 194, 64027)
AradaraExpress = Card("aradara_express", "Aradara Express", ['5'], [], "Artifact", "Vehicle", "KLD", "Common", 195, 64029)
BallistaCharger = Card("ballista_charger", "Ballista Charger", ['5'], [], "Artifact", "Vehicle", "KLD", "Uncommon", 196, 64031)
BastionMastodon = Card("bastion_mastodon", "Bastion Mastodon", ['5'], ['W'], "Artifact Creature", "Elephant", "KLD", "Common", 197, 64033)
BomatBazaarBarge = Card("bomat_bazaar_barge", "Bomat Bazaar Barge", ['4'], [], "Artifact", "Vehicle", "KLD", "Uncommon", 198, 64035)
BomatCourier = Card("bomat_courier", "Bomat Courier", ['1'], ['R'], "Artifact Creature", "Construct", "KLD", "Rare", 199, 64037)
ChiefoftheFoundry = Card("chief_of_the_foundry", "Chief of the Foundry", ['3'], [], "Artifact Creature", "Construct", "KLD", "Uncommon", 200, 64039)
CogworkersPuzzleknot = Card("cogworkers_puzzleknot", "Cogworker's Puzzleknot", ['2'], ['W'], "Artifact", "", "KLD", "Common", 201, 64041)
ConsulateSkygate = Card("consulate_skygate", "Consulate Skygate", ['2'], [], "Artifact Creature", "Wall", "KLD", "Common", 202, 64043)
CultivatorsCaravan = Card("cultivators_caravan", "Cultivator's Caravan", ['3'], [], "Artifact", "Vehicle", "KLD", "Rare", 203, 64045)
DeadlockTrap = Card("deadlock_trap", "Deadlock Trap", ['3'], [], "Artifact", "", "KLD", "Rare", 204, 64047)
DecoctionModule = Card("decoction_module", "Decoction Module", ['2'], [], "Artifact", "", "KLD", "Uncommon", 205, 64049)
DemolitionStomper = Card("demolition_stomper", "Demolition Stomper", ['6'], [], "Artifact", "Vehicle", "KLD", "Uncommon", 206, 64051)
DukharaPeafowl = Card("dukhara_peafowl", "Dukhara Peafowl", ['4'], ['U'], "Artifact Creature", "Bird", "KLD", "Common", 207, 64053)
DynavoltTower = Card("dynavolt_tower", "Dynavolt Tower", ['3'], [], "Artifact", "", "KLD", "Rare", 208, 64055)
EagerConstruct = Card("eager_construct", "Eager Construct", ['2'], [], "Artifact Creature", "Construct", "KLD", "Common", 209, 64057)
ElectrostaticPummeler = Card("electrostatic_pummeler", "Electrostatic Pummeler", ['3'], [], "Artifact Creature", "Construct", "KLD", "Rare", 210, 64059)
FabricationModule = Card("fabrication_module", "Fabrication Module", ['3'], [], "Artifact", "", "KLD", "Uncommon", 211, 64061)
FiligreeFamiliar = Card("filigree_familiar", "Filigree Familiar", ['3'], [], "Artifact Creature", "Fox", "KLD", "Uncommon", 212, 64063)
FireforgersPuzzleknot = Card("fireforgers_puzzleknot", "Fireforger's Puzzleknot", ['2'], ['R'], "Artifact", "", "KLD", "Common", 213, 64065)
FleetwheelCruiser = Card("fleetwheel_cruiser", "Fleetwheel Cruiser", ['4'], [], "Artifact", "Vehicle", "KLD", "Rare", 214, 64067)
FoundryInspector = Card("foundry_inspector", "Foundry Inspector", ['3'], [], "Artifact Creature", "Construct", "KLD", "Uncommon", 215, 64069)
GhirapurOrrery = Card("ghirapur_orrery", "Ghirapur Orrery", ['4'], [], "Artifact", "", "KLD", "Rare", 216, 64071)
GlassblowersPuzzleknot = Card("glassblowers_puzzleknot", "Glassblower's Puzzleknot", ['2'], ['U'], "Artifact", "", "KLD", "Common", 217, 64073)
InventorsGoggles = Card("inventors_goggles", "Inventor's Goggles", ['1'], [], "Artifact", "Equipment", "KLD", "Common", 218, 64075)
IronLeagueSteed = Card("iron_league_steed", "Iron League Steed", ['4'], [], "Artifact Creature", "Construct", "KLD", "Uncommon", 219, 64077)
KeytotheCity = Card("key_to_the_city", "Key to the City", ['2'], [], "Artifact", "", "KLD", "Rare", 220, 64079)
MetalspinnersPuzzleknot = Card("metalspinners_puzzleknot", "Metalspinner's Puzzleknot", ['2'], ['B'], "Artifact", "", "KLD", "Common", 221, 64081)
MetalworkColossus = Card("metalwork_colossus", "Metalwork Colossus", ['11'], [], "Artifact Creature", "Construct", "KLD", "Rare", 222, 64083)
MultiformWonder = Card("multiform_wonder", "Multiform Wonder", ['5'], [], "Artifact Creature", "Construct", "KLD", "Rare", 223, 64085)
NarnamCobra = Card("narnam_cobra", "Narnam Cobra", ['2'], ['G'], "Artifact Creature", "Snake", "KLD", "Common", 224, 64087)
OvalchaseDragster = Card("ovalchase_dragster", "Ovalchase Dragster", ['4'], [], "Artifact", "Vehicle", "KLD", "Uncommon", 225, 64089)
Panharmonicon = Card("panharmonicon", "Panharmonicon", ['4'], [], "Artifact", "", "KLD", "Rare", 226, 64091)
PerpetualTimepiece = Card("perpetual_timepiece", "Perpetual Timepiece", ['2'], [], "Artifact", "", "KLD", "Uncommon", 227, 64093)
PrakhataPillarBug = Card("prakhata_pillarbug", "Prakhata Pillar-Bug", ['3'], ['B'], "Artifact Creature", "Insect", "KLD", "Common", 228, 64095)
PropheticPrism = Card("prophetic_prism", "Prophetic Prism", ['2'], [], "Artifact", "", "KLD", "Common", 229, 64097)
RenegadeFreighter = Card("renegade_freighter", "Renegade Freighter", ['3'], [], "Artifact", "Vehicle", "KLD", "Common", 230, 64099)
ScrapheapScrounger = Card("scrapheap_scrounger", "Scrapheap Scrounger", ['2'], ['B'], "Artifact Creature", "Construct", "KLD", "Rare", 231, 64101)
SelfAssembler = Card("selfassembler", "Self-Assembler", ['5'], [], "Artifact Creature", "Assembly-Worker", "KLD", "Common", 232, 64103)
SkySkiff = Card("sky_skiff", "Sky Skiff", ['2'], [], "Artifact", "Vehicle", "KLD", "Common", 233, 64169)
SkysovereignConsulFlagship = Card("skysovereign_consul_flagship", "Skysovereign, Consul Flagship", ['5'], [], "Legendary Artifact", "Vehicle", "KLD", "Mythic Rare", 234, 64107)
SmugglersCopter = Card("smugglers_copter", "Smuggler's Copter", ['2'], [], "Artifact", "Vehicle", "KLD", "Rare", 235, 64171)
SnareThopter = Card("snare_thopter", "Snare Thopter", ['4'], [], "Artifact Creature", "Thopter", "KLD", "Uncommon", 236, 64111)
TorchGauntlet = Card("torch_gauntlet", "Torch Gauntlet", ['2'], [], "Artifact", "Equipment", "KLD", "Common", 237, 64113)
WeldfastMonitor = Card("weldfast_monitor", "Weldfast Monitor", ['3'], ['R'], "Artifact Creature", "Lizard", "KLD", "Common", 238, 64115)
Whirlermaker = Card("whirlermaker", "Whirlermaker", ['3'], [], "Artifact", "", "KLD", "Uncommon", 239, 64117)
WoodweaversPuzzleknot = Card("woodweavers_puzzleknot", "Woodweaver's Puzzleknot", ['2'], ['G'], "Artifact", "", "KLD", "Common", 240, 64119)
WorkshopAssistant = Card("workshop_assistant", "Workshop Assistant", ['3'], [], "Artifact Creature", "Construct", "KLD", "Common", 241, 64121)
AetherHub = Card("aether_hub", "Aether Hub", [], [], "Land", "", "KLD", "Uncommon", 242, 64123)
BloomingMarsh = Card("blooming_marsh", "Blooming Marsh", [], ['B', 'G'], "Land", "", "KLD", "Rare", 243, 64125)
BotanicalSanctum = Card("botanical_sanctum", "Botanical Sanctum", [], ['G', 'U'], "Land", "", "KLD", "Rare", 244, 64127)
ConcealedCourtyard = Card("concealed_courtyard", "Concealed Courtyard", [], ['W', 'B'], "Land", "", "KLD", "Rare", 245, 64129)
InspiringVantage = Card("inspiring_vantage", "Inspiring Vantage", [], ['R', 'W'], "Land", "", "KLD", "Rare", 246, 64131)
InventorsFair = Card("inventors_fair", "Inventors' Fair", [], [], "Legendary Land", "", "KLD", "Rare", 247, 64133)
SequesteredStash = Card("sequestered_stash", "Sequestered Stash", [], [], "Land", "", "KLD", "Uncommon", 248, 64135)
SpirebluffCanal = Card("spirebluff_canal", "Spirebluff Canal", [], ['U', 'R'], "Land", "", "KLD", "Rare", 249, 64137)
Plains = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "KLD", "Basic Land", 250, 64139)
Plains2 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "KLD", "Basic Land", 251, 64141)
Plains3 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "KLD", "Basic Land", 252, 64143)
Island = Card("island", "Island", [], ['U'], "Basic Land", "Island", "KLD", "Basic Land", 253, 64145)
Island2 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "KLD", "Basic Land", 254, 64147)
Island3 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "KLD", "Basic Land", 255, 64149)
Swamp = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "KLD", "Basic Land", 256, 64151)
Swamp2 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "KLD", "Basic Land", 257, 64153)
Swamp3 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "KLD", "Basic Land", 258, 64155)
Mountain = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "KLD", "Basic Land", 259, 64157)
Mountain2 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "KLD", "Basic Land", 260, 64159)
Mountain3 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "KLD", "Basic Land", 261, 64161)
Forest = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "KLD", "Basic Land", 262, 64163)
Forest2 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "KLD", "Basic Land", 263, 64165)
Forest3 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "KLD", "Basic Land", 264, 64167)
ChandraPyrogenius = Card("chandra_pyrogenius", "Chandra, Pyrogenius", ['4', 'R', 'R'], ['R'], "Legendary Planeswalker", "Chandra", "KLD", "Mythic Rare", 265, 65407)
FlameLash = Card("flame_lash", "Flame Lash", ['3', 'R'], ['R'], "Instant", "", "KLD", "Common", 266, 65409)
LiberatingCombustion = Card("liberating_combustion", "Liberating Combustion", ['4', 'R'], ['R'], "Sorcery", "", "KLD", "Rare", 267, 65411)
RenegadeFirebrand = Card("renegade_firebrand", "Renegade Firebrand", ['2', 'R'], ['R'], "Creature", "Human Warrior", "KLD", "Uncommon", 268, 65413)
StoneQuarry = Card("stone_quarry", "Stone Quarry", [], ['R', 'W'], "Land", "", "KLD", "Common", 269, 65415)
NissaNaturesArtisan = Card("nissa_natures_artisan", "Nissa, Nature's Artisan", ['4', 'G', 'G'], ['G'], "Legendary Planeswalker", "Nissa", "KLD", "Mythic Rare", 270, 65417)
GuardianoftheGreatConduit = Card("guardian_of_the_great_conduit", "Guardian of the Great Conduit", ['3', 'G'], ['G'], "Creature", "Elemental", "KLD", "Uncommon", 271, 65419)
TerrainElemental = Card("terrain_elemental", "Terrain Elemental", ['1', 'G'], ['G'], "Creature", "Elemental", "KLD", "Common", 272, 65421)
VerdantCrescendo = Card("verdant_crescendo", "Verdant Crescendo", ['3', 'G'], ['G'], "Sorcery", "", "KLD", "Rare", 273, 65423)
WoodlandStream = Card("woodland_stream", "Woodland Stream", [], ['G', 'U'], "Land", "", "KLD", "Common", 274, 65425)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
Kaladesh = Set("kaladesh", cards=clsmembers)
