import json
from pathlib import Path

def createXML():
    arcanes = {
        #Cavia
        "Melee_Fortification": [22.5, "Cavia"],
        "Melee_Retaliation"  : [22.5, "Cavia"],

        "Melee_Animosity"    : [12.5, "Cavia"],
        "Melee_Exposure"     : [12.5, "Cavia"],
        "Melee_Influence"    : [12.5, "Cavia"],
        "Melee_Vortex"       : [12.5, "Cavia"],

        "Melee_Crescendo"    : [2.5, "Cavia"],
        "Melee_Duplicate"    : [2.5, "Cavia"],

        #Duviri
        "Arcane_Intention"   : [22.5, "Duviri"],
        "Magus_Aggress"      : [22.5, "Duviri"],

        "Arcane_Power_Ramp"  : [12.5, "Duviri"],
        "Primary_Blight"     : [12.5, "Duviri"],
        "Primary_Exhilarate" : [12.5, "Duviri"],
        "Primary_Obstruct"   : [12.5, "Duviri"],
        "Shotgun_Vendetta"   : [12.5, "Duviri"],
        "Akimbo_Slip_Shot"   : [12.5, "Duviri"],
        "Secondary_Outburst" : [12.5, "Duviri"],

        "Arcane_Reaper"      : [2.5, "Duviri"],
        "Longbow_Sharpshot"  : [2.5, "Duviri"],
        "Secondary_Shiver"   : [2.5, "Duviri"],

        #Eidolon
        "Arcane_Consequence" : [6.67, "Eidolon"],
        "Arcane_Ice"         : [6.67, "Eidolon"],
        "Arcane_Momentum"    : [6.67, "Eidolon"],
        "Arcane_Nullifier"   : [6.67, "Eidolon"],
        "Arcane_Tempo"       : [6.67, "Eidolon"],
        "Arcane_Warmth"      : [6.67, "Eidolon"],

        "Arcane_Acceleration": [2.69, "Eidolon"],
        "Arcane_Agility"     : [2.69, "Eidolon"],
        "Arcane_Awakening"   : [2.69, "Eidolon"],
        "Arcane_Deflection"  : [2.69, "Eidolon"],
        "Arcane_Eruption"    : [2.69, "Eidolon"],
        "Arcane_Guardian"    : [2.69, "Eidolon"],
        "Arcane_Healing"     : [2.69, "Eidolon"],
        "Arcane_Phantasm"    : [2.69, "Eidolon"],
        "Arcane_Strike"      : [2.69, "Eidolon"],
        "Arcane_Resistance"  : [2.69, "Eidolon"],
        "Arcane_Trickery"    : [2.69, "Eidolon"],
        "Arcane_Velocity"    : [2.69, "Eidolon"],
        "Arcane_Victory"     : [2.69, "Eidolon"],

        "Arcane_Aegis"       : [2.5, "Eidolon"],
        "Arcane_Arachne"     : [2.5, "Eidolon"],
        "Arcane_Avenger"     : [2.5, "Eidolon"],
        "Arcane_Fury"        : [2.5, "Eidolon"],
        "Arcane_Precision"   : [2.5, "Eidolon"],
        "Arcane_Pulse"       : [2.5, "Eidolon"],
        "Arcane_Rage"        : [2.5, "Eidolon"],
        "Arcane_Ultimatum"   : [2.5, "Eidolon"],

        "Arcane_Barrier"     : [1.67, "Eidolon"],
        "Arcane_Energize"    : [1.67, "Eidolon"],
        "Arcane_Grace"       : [1.67, "Eidolon"],

        #Holdfasts
        "Arcane_Blessing"    : [5.263, "Holdfasts"],
        "Arcane_Rise"        : [5.263, "Holdfasts"],
        "Molt_Augmented"     : [5.263, "Holdfasts"],
        "Molt_Efficiency"    : [5.263, "Holdfasts"],
        "Molt_Reconstruct"   : [5.263, "Holdfasts"],
        "Molt_Vigor"         : [5.263, "Holdfasts"],
        "Fractalized_Reset"  : [5.263, "Holdfasts"],
        "Primary_Frostbite"  : [5.263, "Holdfasts"],
        "Cascadia_Accuracy"  : [5.263, "Holdfasts"],
        "Cascadia_Empowered" : [5.263, "Holdfasts"],
        "Cascadia_Flare"     : [5.263, "Holdfasts"],
        "Cascadia_Overcharge": [5.263, "Holdfasts"],
        "Conjunction_Voltage": [5.263, "Holdfasts"],
        "Emergence_Dissipate": [5.263, "Holdfasts"],
        "Emergence_Renewed"  : [5.263, "Holdfasts"],
        "Emergence_Savior"   : [5.263, "Holdfasts"],
        "Eternal_Eradicate"  : [5.263, "Holdfasts"],
        "Eternal_Logistics"  : [5.263, "Holdfasts"],
        "Eternal_Onslaught"  : [5.263, "Holdfasts"],

        #Necralisk
        "Arcane_Double_Back" : [8.33, "Necralisk"],
        "Arcane_Steadfast"   : [8.33, "Necralisk"],
        "Theorem_Contagion"  : [8.33, "Necralisk"],
        "Theorem_Demulcent"  : [8.33, "Necralisk"],
        "Theorem_Infection"  : [8.33, "Necralisk"],
        "Primary_Plated_Round":[8.33, "Necralisk"],
        "Secondary_Encumber" : [8.33, "Necralisk"],
        "Secondary_Kinship"  : [8.33, "Necralisk"],
        "Residual_Boils"     : [8.33, "Necralisk"],
        "Residual_Malodor"   : [8.33, "Necralisk"],
        "Residual_Shock"     : [8.33, "Necralisk"],
        "Residual_Viremia"   : [8.33, "Necralisk"],

        #Ostron
        "Magus_Husk"         : [2.5, "Ostron"],
        "Magus_Vigor"        : [2.5, "Ostron"],
        "Virtuos_Null"       : [2.5, "Ostron"],
        "Virtuos_Tempo"      : [2.5, "Ostron"],

        "Exodia_Triumph"     : [4.286, "Ostron"],
        "Exodia_Valor"       : [4.286, "Ostron"],
        "Magus_Cadence"      : [4.286, "Ostron"],
        "Magus_Cloud"        : [4.286, "Ostron"],
        "Magus_Replenish"    : [4.286, "Ostron"],
        "Virtuos_Fury"       : [4.286, "Ostron"],
        "Virtuos_Strike"     : [4.286, "Ostron"],

        "Exodia_Brave"       : [7.5, "Ostron"],
        "Exodia_Force"       : [7.5, "Ostron"],
        "Exodia_Hunt"        : [7.5, "Ostron"],
        "Exodia_Might"       : [7.5, "Ostron"],
        "Magus_Elevate"      : [7.5, "Ostron"],
        "Magus_Nourish"      : [7.5, "Ostron"],
        "Virtuos_Ghost"      : [7.5, "Ostron"],
        "Virtuos_Shadow"     : [7.5, "Ostron"],

        #Solaris/Fortuna
        "Magus_Accelerant"   : [2.5, "Solaris"],
        "Magus_Anomaly"      : [2.5, "Solaris"],
        "Magus_Drive"        : [2.5, "Solaris"],
        "Magus_Firewall"     : [2.5, "Solaris"],
        "Magus_Overload"     : [2.5, "Solaris"],
        "Virtuos_Spike"      : [2.5, "Solaris"],
        "Virtuos_Surge"      : [2.5, "Solaris"],

        "Magus_Glitch"       : [3.75, "Solaris"],
        "Magus_Repair"       : [3.75, "Solaris"],
        "Virtuos_Forge"      : [3.75, "Solaris"],
        "Virtuos_Trojan"     : [3.75, "Solaris"],

        "Pax_Bolt"           : [8.75, "Solaris"],
        "Pax_Charge"         : [8.75, "Solaris"],
        "Pax_Seeker"         : [8.75, "Solaris"],
        "Pax_Soar"           : [8.75, "Solaris"],
        "Magus_Destruct"     : [8.75, "Solaris"],
        "Magus_Lockdown"     : [8.75, "Solaris"],
        "Magus_Melt"         : [8.75, "Solaris"],
        "Magus_Revert"       : [8.75, "Solaris"],

        #Steel path
        "Arcane_Blade_Charger":[9.091, "Steel Path"],
        "Arcane_Bodyguard"   : [9.091, "Steel Path"],
        "Arcane_Pistoleer"   : [9.091, "Steel Path"],
        "Arcane_Primary_Charger":[9.091, "Steel Path"],
        "Arcane_Tanker"      : [9.091, "Steel Path"],
        "Primary_Deadhead"   : [9.091, "Steel Path"],
        "Primary_Dexterity"  : [9.091, "Steel Path"],
        "Primary_Merciless"  : [9.091, "Steel Path"],
        "Secondary_Deadhead" : [9.091, "Steel Path"],
        "Secondary_Dexterity": [9.091, "Steel Path"],
        "Secondary_Merciless": [9.091, "Steel Path"],
        
        #Hollvania
        "Arcane_Bellicose"   : [11.875, "Hollvania"],
        "Arcane_Camisado"    : [11.875, "Hollvania"],
        "Arcane_Crepuscular" : [11.875, "Hollvania"],
        "Arcane_Impetus"     : [11.875, "Hollvania"],
        "Arcane_Truculence"  : [11.875, "Hollvania"],
        "Primary_Crux"       : [11.875, "Hollvania"],
        "Secondary_Enervate" : [11.875, "Hollvania"],
        "Melee_Doughty"      : [11.875, "Hollvania"],

        "Arcane_Escapist"    : [1.67, "Hollvania"],
        "Arcane_Hot_Shot"    : [1.67, "Hollvania"],
        "Arcane_Universal_Fallout": [1.67, "Hollvania"],
        }

    data = [
        {"Arcanes":[{"Name": name, "DropChance": chance[0], "Faction": chance[1]}
        for name, chance in arcanes.items()]}
    ]

    print(data)
    json_path = Path(Path(__file__).parent / "ArcaneList.json")
    json_path.write_text(
        json.dumps(
            data,
            indent=2
        ),
        encoding="utf-8"
    )

createXML()
