# PoE2 Currency Reference

Build focus: Lightning+Chaos Invoker Monk (dual 1H Mace + Quarterstaff → Dual Mjölnir)

> Items marked ★ are directly relevant to this build's crafting workflow.

## Core Crafting Orbs

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Blessed Orb | `CurrencyRerollImplicit` | Re-rolls numeric values of implicit mods (Blessed Orb) | Improve implicit on a well-rolled weapon |
| ★ Chaos Orb | `CurrencyRerollRare` | Rerolls all mods on a rare item (Chaos Orb) | Core crafting currency — reroll rares to find desired affix combos |
| ★ Divine Orb | `CurrencyModValues` | Re-rolls numeric values of all mods on a magic/rare item (Divine Orb) | Re-roll tier rolls — use when mod is correct but values are low |
| ★ Eternal Orb | `CurrencyImprintOrb` | Creates an Imprint of a magic item that can be restored (Eternal Orb) | Backup magic item before risky crafting |
| ★ Exalted Orb | `CurrencyAddModToRare` | Adds one mod to a rare item with open affix slot (Exalted Orb) | Add a specific-tier mod after locking good existing mods |
| ★ Fracturing Orb | `CurrencyFractureRare` | Fractures one mod on a rare item — that mod is permanently locked (Fracturing Orb) | Lock a high-tier desired mod before rerolling others |
| ★ Greater Chaos Orb | `CurrencyRerollRare2` | Greater Chaos Orb — rerolls rare mods (higher tier weighting) | Better than Chaos Orb on level 75+ items |
| ★ Greater Exalted Orb | `CurrencyAddModToRare2` | Greater Exalted Orb — adds mod to rare (higher tier weighting) | Prefer for endgame weapon crafting |
| Greater Orb of Augmentation | `CurrencyAddModToMagic2` | Adds a mod to a magic item (if only 1 mod) | Add second mod to a one-affix magic item |
| Greater Orb of Transmutation | `CurrencyUpgradeToMagic2` | Greater version — upgrades normal to magic (better odds on higher tiers) | Prefer on higher-level bases |
| Greater Regal Orb | `CurrencyUpgradeMagicToRare2` | Upgrades a magic item to rare (3–4 mods) | Convert a perfect magic item to rare to gain more mods |
| ★ Hinekora's Lock | `CurrencyHinekorasLock` | Locks an item's mods so Divine Orb cannot reroll them | Use before Divine Orb to protect already-maxed mod values |
| Mirror of Kalandra | `CurrencyDuplicate` | Creates an exact copy of an item (Mirror of Kalandra) | The rarest currency — copy a near-perfect endgame item |
| Orb of Alchemy | `CurrencyUpgradeToRare` | Upgrades a normal item directly to rare (4 random mods) | Skip magic step — go straight to rare base |
| Orb of Alteration | `CurrencyRerollMagic` | Rerolls all mods on a magic item | Spam on a magic base to fish for desired prefix+suffix combo |
| ★ Orb of Annulment | `CurrencyRemoveMod` | Removes one random mod from a rare item (Orb of Annulment) | Remove a bad mod after exalting — risky but powerful |
| Orb of Augmentation | `CurrencyAddModToMagic` | Adds a mod to a magic item (if only 1 mod) | Add second mod to a one-affix magic item |
| Orb of Chance | `CurrencyUpgradeRandomly` | Randomly upgrades a normal item to magic, rare, or unique (Orb of Chance) | Gamble for a unique on a specific base type |
| Orb of Regret | `CurrencyPassiveRefund` | Refunds one passive skill point (Orb of Regret) | Respec passive tree nodes |
| Orb of Scouring | `CurrencyConvertToNormal` | Removes all mods from a rare/magic item (Orb of Scouring) | Reset a bad roll to white; start crafting over |
| Orb of Transmutation | `CurrencyUpgradeToMagic` | Upgrades a normal item to magic (1–2 mods) | First step: turn a white base into a magic item |
| ★ Perfect Chaos Orb | `CurrencyRerollRare3` | Perfect Chaos Orb — rerolls rare mods (highest tier weighting) | Best reroll for endgame bases |
| ★ Perfect Exalted Orb | `CurrencyAddModToRare3` | Perfect Exalted Orb — adds mod with highest tier weighting | Best for finalizing endgame rare weapons |
| Perfect Orb of Augmentation | `CurrencyAddModToMagic3` | Adds a mod to a magic item (if only 1 mod) | Add second mod to a one-affix magic item |
| Perfect Orb of Transmutation | `CurrencyUpgradeToMagic3` | Perfect version — upgrades normal to magic | Best quality normal→magic upgrade |
| Perfect Regal Orb | `CurrencyUpgradeMagicToRare3` | Upgrades a magic item to rare (3–4 mods) | Convert a perfect magic item to rare to gain more mods |
| Regal Orb | `CurrencyUpgradeMagicToRare` | Upgrades a magic item to rare (3–4 mods) | Convert a perfect magic item to rare to gain more mods |
| Sacred Orb | `CurrencyRerollDefences` | Re-rolls defence values on armour (Sacred Orb) | Optimize armour/ES/evasion values |
| Scroll of Wisdom | `CurrencyIdentification` | Identifies an unidentified item | Use on any unidentified magic/rare/unique drop |
| ★ Vaal Orb | `CurrencyCorrupt` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |

## Essences

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| ★ Essence of Abrasion | `CurrencyEssencePhysical` | Forces a guaranteed physical damage mod | ★ Use on mace to guarantee phys damage (scales lightning via conversion) |
| Essence of Alacrity | `CurrencyEssenceSpeedCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Battle | `CurrencyEssenceAttack` | Forces a guaranteed attack-related mod | ★ Use on weapon — attack speed or similar |
| Essence of Command | `CurrencyEssenceAlly` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Delirium | `CurrencyCorruptedEssenceDelirium` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| ★ Essence of Electricity | `CurrencyEssenceLightning` | Forces a guaranteed lightning mod on an item | ★ Guaranteed lightning damage on weapon — use Essence of Electricity on mace |
| Essence of Enhancement | `CurrencyEssenceDefences` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Essence of Flames | `CurrencyEssenceFire` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Grounding | `CurrencyEssenceLightningResist` | Forces a guaranteed lightning mod on an item | ★ Guaranteed lightning damage on weapon — use Essence of Electricity on mace |
| Essence of Haste | `CurrencyEssenceSpeed` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Horror | `CurrencyCorruptedEssenceHorror` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| ★ Essence of Hysteria | `CurrencyCorruptedEssenceHysteria` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| Essence of Ice | `CurrencyEssenceCold` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Insanity | `CurrencyCorruptedEssenceInsanity` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| Essence of Insulation | `CurrencyEssenceFireResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Essence of Opulence | `CurrencyEssenceRarity` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Essence of Ruin | `CurrencyEssenceChaos` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of Seeking | `CurrencyEssenceCritical` | Forces a guaranteed critical strike mod | ★ Use for guaranteed crit chance/multi on weapons |
| Essence of Sorcery | `CurrencyEssenceCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Essence of Thawing | `CurrencyEssenceColdResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Essence of the Abyss | `CurrencyCorruptedEssenceAbyss` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| Essence of the Body | `CurrencyEssenceLife` | Forces a guaranteed maximum life mod | Use on body armour or rings for life |
| ★ Essence of the Breach | `CurrencyCorruptedEssenceBreach` | Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing | Final step on a finished item to gamble for extra power; cannot be modified after |
| Essence of the Infinite | `CurrencyEssenceAttribute` | Forces a guaranteed attribute (Str/Int/Dex) mod | Use on rings/amulets when short on Str/Int requirements |
| Essence of the Mind | `CurrencyEssenceMana` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Glyphic Fossil | `CurrencyDelveCraftingCorruptEssence` | Has a Corrupt Essence modifier | Place in a Resonator to influence item crafting. |
| ★ Greater Essence of Abrasion | `CurrencyGreaterEssencePhysical` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Alacrity | `CurrencyGreaterEssenceSpeedCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Greater Essence of Battle | `CurrencyGreaterEssenceAttack` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Command | `CurrencyGreaterEssenceAlly` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Greater Essence of Electricity | `CurrencyGreaterEssenceLightning` | Greater version — forces higher-tier lightning mod | ★ Better guaranteed lightning mod — use on high-level bases |
| Greater Essence of Enhancement | `CurrencyGreaterEssenceDefences` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Flames | `CurrencyGreaterEssenceFire` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Greater Essence of Grounding | `CurrencyGreaterEssenceLightningResist` | Greater version — forces higher-tier lightning mod | ★ Better guaranteed lightning mod — use on high-level bases |
| Greater Essence of Haste | `CurrencyGreaterEssenceSpeed` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Ice | `CurrencyGreaterEssenceCold` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Insulation | `CurrencyGreaterEssenceFireResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Opulence | `CurrencyGreaterEssenceRarity` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Ruin | `CurrencyGreaterEssenceChaos` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Greater Essence of Seeking | `CurrencyGreaterEssenceCritical` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Sorcery | `CurrencyGreaterEssenceCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of Thawing | `CurrencyGreaterEssenceColdResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of the Body | `CurrencyGreaterEssenceLife` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of the Infinite | `CurrencyGreaterEssenceAttribute` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Greater Essence of the Mind | `CurrencyGreaterEssenceMana` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Lesser Essence of Abrasion | `CurrencyLesserEssencePhysical` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Alacrity | `CurrencyLesserEssenceSpeedCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Lesser Essence of Battle | `CurrencyLesserEssenceAttack` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Command | `CurrencyLesserEssenceAlly` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Lesser Essence of Electricity | `CurrencyLesserEssenceLightning` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Enhancement | `CurrencyLesserEssenceDefences` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Flames | `CurrencyLesserEssenceFire` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Lesser Essence of Grounding | `CurrencyLesserEssenceLightningResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Haste | `CurrencyLesserEssenceSpeed` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Ice | `CurrencyLesserEssenceCold` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Insulation | `CurrencyLesserEssenceFireResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Opulence | `CurrencyLesserEssenceRarity` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Ruin | `CurrencyLesserEssenceChaos` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Lesser Essence of Seeking | `CurrencyLesserEssenceCritical` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Sorcery | `CurrencyLesserEssenceCaster` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of Thawing | `CurrencyLesserEssenceColdResist` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of the Body | `CurrencyLesserEssenceLife` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of the Infinite | `CurrencyLesserEssenceAttribute` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| Lesser Essence of the Mind | `CurrencyLesserEssenceMana` | Upgrades a [ItemRarity|Magic] item to a [ItemRarity|Rare] item, adding a guaranteed modifier | Right click this item then left click a Magic item to apply it. |
| ★ Perfect Essence of Abrasion | `CurrencyPerfectEssencePhysical` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Alacrity | `CurrencyPerfectEssenceSpeedCaster` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| ★ Perfect Essence of Battle | `CurrencyPerfectEssenceAttack` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Command | `CurrencyPerfectEssenceAlly` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| ★ Perfect Essence of Electricity | `CurrencyPerfectEssenceLightning` | Perfect version — forces top-tier lightning mod | ★ Best guaranteed lightning mod for endgame mace |
| Perfect Essence of Enhancement | `CurrencyPerfectEssenceDefences` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Flames | `CurrencyPerfectEssenceFire` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| ★ Perfect Essence of Grounding | `CurrencyPerfectEssenceLightningResist` | Perfect version — forces top-tier lightning mod | ★ Best guaranteed lightning mod for endgame mace |
| Perfect Essence of Haste | `CurrencyPerfectEssenceSpeed` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Ice | `CurrencyPerfectEssenceCold` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Insulation | `CurrencyPerfectEssenceFireResist` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Opulence | `CurrencyPerfectEssenceRarity` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Ruin | `CurrencyPerfectEssenceChaos` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| ★ Perfect Essence of Seeking | `CurrencyPerfectEssenceCritical` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Sorcery | `CurrencyPerfectEssenceCaster` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of Thawing | `CurrencyPerfectEssenceColdResist` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of the Body | `CurrencyPerfectEssenceLife` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of the Infinite | `CurrencyPerfectEssenceAttribute` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Perfect Essence of the Mind | `CurrencyPerfectEssenceMana` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |

## Quality Currency

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Arcanist's Etcher | `CurrencyMagicQuality` | Improves quality of a wand/staff/sceptre | For caster weapons only; not relevant to Monk maces |
| Armourer's Scrap | `CurrencyArmourQuality` | Improves quality of armour | Use on armour before crafting to boost defence values |
| Blacksmith's Whetstone | `CurrencyWeaponQuality` | Improves quality of a martial weapon (+1% per use, up to 20%) | Use on weapons before crafting — quality increases implicit values |
| Cartographer's Chisel | `CurrencyMapQuality` | Improves quality of a map (Cartographer's Chisel) | Use on maps before running to increase item quantity |
| Gemcutter's Prism | `CurrencyGemQuality` | Improves quality of a gem | Use on skill gems to boost quality effects |
| Glassblower's Bauble | `CurrencyFlaskQuality` | Improves quality of a flask | Use on flasks to increase effect/duration |

## Ritual & League Mechanics

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Petition Splinter | `CurrencyRitualShard` |  | This item is no longer usable. |
| Ritual Splinter | `CurrencyRitualSplinter` | 100 splinters combine into a Ritual Vessel | Collect to build Ritual Vessels for replaying ritual monster pools |
| Ritual Vessel | `CurrencyRitualStone` | Stores monsters from a completed Ritual Altar (Ritual Vessel) | Use at a Ritual Altar to add stored monsters to a future map's ritual |
| Vial of the Ritual | `CurrencyIncursionVialLightning` |  | Sacrifice this item on the Altar of Sacrifice along with Dance of the Offered to transform it. |

## Sockets

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Adaptive Catalyst | `CurrencyJewelleryQualityAttribute` | Adds [Quality|quality] that enhances [Attributes|Attribute] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Ancient Collarbone | `AbyssalBenchTicketJewelleryHigh` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Amulet, Ring or Belt | Right click this item then left click a Rare item to apply it. |
| Artificer's Orb | `CurrencyAddEquipmentSocket` | Adds a socket to an item (Artificer's Orb) | Add rune sockets to weapons/armour |
| Artificer's Shard | `CurrencyAddEquipmentSocketShard` | Adds a socket to an item (Artificer's Orb) | Add rune sockets to weapons/armour |
| Binding Shard | `CurrencyUpgradeToRareAndSetSocketsShard` | Upgrades a normal item directly to rare (4 random mods) | Skip magic step — go straight to rare base |
| Carapace Catalyst | `CurrencyJewelleryQualityDefences` | Adds [Quality|quality] that enhances [Armour], [Evasion] and [EnergyShield|Energy Shield] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Chayula's Catalyst | `CurrencyJewelleryQualityChaos` | Adds [Quality|quality] that enhances [Chaos] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Chromatic Orb | `CurrencyRerollSocketColours` | Rerolls socket colours on an item (Chromatic Orb) | Not relevant in PoE2 — socket system changed |
| Esh's Catalyst | `CurrencyJewelleryQualityLightning` | Adds [Quality|quality] that enhances [Lightning] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Flesh Catalyst | `CurrencyJewelleryQualityLife` | Adds [Quality|quality] that enhances Life modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Fundamental Fossil | `CurrencyDelveCraftingSockets` | More Attribute modifiers
No Critical modifiers | Place in a Resonator to influence item crafting. |
| Gnawed Collarbone | `AbyssalBenchTicketJewelleryLow` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Amulet, Ring or Belt | Right click this item then left click a Rare item to apply it. |
| Greater Jeweller's Orb | `CurrencyAddSkillGemSocket4` | Adds a 4th socket to a skill gem (Greater Jeweller's Orb) | Further expand support gem slots |
| Lesser Jeweller's Orb | `CurrencyAddSkillGemSocket3` | Adds a 3rd socket to a skill gem (Lesser Jeweller's Orb) | Add sockets to skill gems to fit more support gems |
| Neural Catalyst | `CurrencyJewelleryQualityMana` | Adds [Quality|quality] that enhances Mana modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Orb of Binding | `CurrencyUpgradeToRareAndSetSockets` | Upgrades a normal item directly to rare (4 random mods) | Skip magic step — go straight to rare base |
| Orb of Extraction | `CurrencyIncursionExtractAllSocketablesBench` | — | — |
| Orb of Extraction | `CurrencyIncursionExtractAllSocketablesCurrency` | Destroys an [Equipment] item, returning any non [SocketBound|Socket-Bound] [Augment|Augments] socketed in it | Right click this item then left click on an item containing socketed [Augment|Augments] to apply it. |
| Orb of Fusing | `CurrencyRerollSocketLinks` | Reforges the links between sockets on an item | Right click this item then left click a socketed item to apply it. The item's quality increases the chances of obtaining more links. |
| Perfect Jeweller's Orb | `CurrencyAddSkillGemSocket5` | Adds a 5th socket to a skill gem (Perfect Jeweller's Orb) | Maximum support gem capacity |
| Preserved Collarbone | `AbyssalBenchTicketJewellery` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Amulet, Ring or Belt | Right click this item then left click a Rare item to apply it. |
| ★ Profane Orb of Sacrifice | `CurrencyIncursionMutateCorruptionEnchantJewellery` | Upgrades a [Corrupted|Corruption] Enchantment on a [ItemRarity|Rare] Amulet, Ring or Belt
and removes a random Modifier | Right click this item then left click on a corrupted item to apply it. |
| Reaver Catalyst | `CurrencyJewelleryQualityAttack` | Adds [Quality|quality] that enhances [Attack] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Sibilant Catalyst | `CurrencyJewelleryQualityCaster` | Adds [Quality|quality] that enhances [Spell|Caster] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Skittering Catalyst | `CurrencyJewelleryQualitySpeed` | Adds [Quality|quality] that enhances Speed modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Tainted Chromatic Orb | `CurrencyHellscapeRerollSocketColours` | Unpredictably reforges the colour of sockets on a corrupted item | Right click this item then left click a corrupted socketed item to apply it. |
| Tainted Jeweller's Orb | `CurrencyHellscapeRerollSocketNumbers` | Unpredictably adds or removes a socket on a corrupted item | Right click this item then left click a corrupted socketed item to apply it. |
| Tainted Orb of Fusing | `CurrencyHellscapeRerollSocketLinks` | Unpredictably adds or removes a link to the largest group of linked sockets on a corrupted item | Right click this item then left click a corrupted socketed item to apply it. |
| Tul's Catalyst | `CurrencyJewelleryQualityCold` | Adds [Quality|quality] that enhances [Cold] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Uul-Netol's Catalyst | `CurrencyJewelleryQualityPhysical` | Adds [Quality|quality] that enhances [Physical] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |
| Vaal Catalysing Infuser | `CurrencyIncursionJewelleryQuality` | Improves the [Quality|quality] of a ring or amulet,
exceeding maximum quality by up to 10% with a chance of [Corrupted|Corrupting] it | Right click this item then left click a ring or amulet to apply it. Can only be used on items at or above maximum quality. |
| Xoph's Catalyst | `CurrencyJewelleryQualityFire` | Adds [Quality|quality] that enhances [Fire] modifiers on a ring or amulet
Replaces other quality types | Right click this item then left click a ring or amulet to apply it. |

## Shards

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Alchemy Shard | `CurrencyUpgradeToRareShard` | Upgrades a normal item directly to rare (4 random mods) | Skip magic step — go straight to rare base |
| Alteration Shard | `CurrencyRerollMagicShard` | Rerolls all mods on a magic item | Spam on a magic base to fish for desired prefix+suffix combo |
| Ancient Shard | `CurrencyRerollUniqueShard` |  | A stack of 20 shards becomes an Ancient Orb. |
| ★ Annulment Shard | `CurrencyRemoveModShard` | Removes one random mod from a rare item (Orb of Annulment) | Remove a bad mod after exalting — risky but powerful |
| Breach Splinter | `CurrencyBreachShard` |  | Combine 300 Splinters to create a Revelatory Wombgift. |
| Chance Shard | `CurrencyUpgradeRandomlyShard` | Randomly upgrades a normal item to magic, rare, or unique (Orb of Chance) | Gamble for a unique on a specific base type |
| ★ Chaos Shard | `CurrencyRerollRareShard` | Rerolls all mods on a rare item (Chaos Orb) | Core crafting currency — reroll rares to find desired affix combos |
| Engineer's Shard | `CurrencyStrongboxQualityShard` |  | A stack of 20 shards becomes an Engineer's Orb. |
| ★ Exalted Shard | `CurrencyAddModToRareShard` | Adds one mod to a rare item with open affix slot (Exalted Orb) | Add a specific-tier mod after locking good existing mods |
| ★ Fracturing Shard | `CurrencyFractureRareShard` | Fractures one mod on a rare item — that mod is permanently locked (Fracturing Orb) | Lock a high-tier desired mod before rerolling others |
| Harbinger's Shard | `CurrencyUpgradeMapTierShard` |  | A stack of 20 shards becomes a Harbinger's Orb. |
| Horizon Shard | `CurrencyRerollMapTypeShard` |  | A stack of 20 shards becomes an Orb of Horizons. |
| Mirror Shard | `CurrencyDuplicateShard` | Creates an exact copy of an item (Mirror of Kalandra) | The rarest currency — copy a near-perfect endgame item |
| Regal Shard | `CurrencyUpgradeMagicToRareShard` | Upgrades a magic item to rare (3–4 mods) | Convert a perfect magic item to rare to gain more mods |
| Runic Splinter | `CurrencyExpeditionShard` |  | This item is no longer usable. |
| Scroll Fragment | `CurrencyIdentificationShard` | Identifies an unidentified item | Use on any unidentified magic/rare/unique drop |
| Shattered Triskelion | `ExpeditionPinnacleKeyShard` |  | Can be repaired at the Verisium Anvil. |
| Simulacrum Splinter | `CurrencyAfflictionShard` |  | Combine 300 Splinters to create a Simulacrum. |
| Splinter of Chayula | `CurrencyBreachChaosShard` |  | Combine 100 splinters to create Chayula's Breachstone. |
| Splinter of Esh | `CurrencyBreachLightningShard` |  | Combine 100 Splinters to create Esh's Breachstone. |
| Splinter of Tul | `CurrencyBreachColdShard` |  | Combine 100 Splinters to create Tul's Breachstone. |
| Splinter of Uul-Netol | `CurrencyBreachPhysicalShard` |  | Combine 100 Splinters to create Uul-Netol's Breachstone. |
| Splinter of Xoph | `CurrencyBreachFireShard` |  | Combine 100 Splinters to create Xoph's Breachstone. |
| Timeless Eternal Empire Splinter | `CurrencyLegionEternalEmpireShard` |  | Combine 100 Splinters to create a Timeless Eternal Emblem. |
| Timeless Karui Splinter | `CurrencyLegionKaruiShard` |  | Combine 100 Splinters to create a Timeless Karui Emblem. |
| Timeless Maraketh Splinter | `CurrencyLegionMarakethShard` |  | Combine 100 Splinters to create a Timeless Maraketh Emblem. |
| Timeless Templar Splinter | `CurrencyLegionTemplarShard` |  | Combine 100 Splinters to create a Timeless Templar Emblem. |
| Timeless Vaal Splinter | `CurrencyLegionVaalShard` |  | Combine 100 Splinters to create a Timeless Vaal Emblem. |
| Transmutation Shard | `CurrencyUpgradeToMagicShard` | Upgrades a normal item to magic (1–2 mods) | First step: turn a white base into a magic item |

## Other / Legacy

| Name | Internal ID | Function | When to Use |
|---|---|---|---|
| Aberrant Fossil | `CurrencyDelveCraftingChaos` | More Chaos modifiers
No Lightning modifiers | Place in a Resonator to influence item crafting. |
| Adaptive Alloy | `CurrencyVerisiumAlloy2` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Aetheric Fossil | `CurrencyDelveCraftingCasterMods` | More Caster modifiers
Fewer Attack modifiers | Place in a Resonator to influence item crafting. |
| Albino Rhoa Feather | `CurrencyRhoaFeather` |  | A discarded Avian feather with an unknown purpose |
| Altered Collarbone | `AbyssalBenchTicketBreach` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Amulet, Ring or Belt with a
chance for otherworldly modifiers | Right click this item then left click a Rare item to apply it. |
| Ancient Concentrated Liquid Fear | `DistilledEmotionTimeLost8` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Concentrated Liquid Isolation | `DistilledEmotionTimeLost10` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Concentrated Liquid Suffering | `DistilledEmotionTimeLost9` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Diluted Liquid Greed | `DistilledEmotionTimeLost3` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Diluted Liquid Guilt | `DistilledEmotionTimeLost2` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Diluted Liquid Ire | `DistilledEmotionTimeLost1` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| ★ Ancient Infuser | `CurrencyIncursionCorruptTablet` | Modifies a [Tablet|Tablet] unpredictably and [Corrupted|Corrupts] it | Right click this item then left click on a Tablet to apply it. |
| Ancient Jawbone | `AbyssalBenchTicketWeaponHigh` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Weapon or [Quiver] | Right click this item then left click a Rare item to apply it. |
| Ancient Liquid Despair | `DistilledEmotionTimeLost7` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Liquid Disgust | `DistilledEmotionTimeLost6` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Liquid Envy | `DistilledEmotionTimeLost5` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Liquid Paranoia | `DistilledEmotionTimeLost4` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Orb | `CurrencyRerollUnique` | Reforges a unique equipment as another of the same item class | Right click this item then left click a unique item to apply it. |
| Ancient Potent Liquid Contempt | `EndgameDistilledEmotionTimeLost3` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Potent Liquid Ferocity | `EndgameDistilledEmotionTimeLost2` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Potent Liquid Melancholy | `EndgameDistilledEmotionTimeLost1` | Removes a random modifer and Augments a [Rarity|Rare] Time-Lost [Jewel] with a
new guaranteed [Crafted] modifier | Right click this item then left click a Rare Time-Lost Jewel to apply it. |
| Ancient Rib | `AbyssalBenchTicketArmourHigh` | [Abyssalify|Desecrates] a [ItemRarity|Rare] [EquipArmour|Armour] | Right click this item then left click a Rare item to apply it. |
| Apprentice Cartographer's Seal | `CurrencySealMapLow` | Uncompletes a white map on the Atlas | Right click this item then left click a white map on the Atlas to apply it. |
| ★ Architect's Orb | `CurrencyIncursionDoubleCorrupt` | Modifies a [Corrupted] [Equipment] or [Jewel] item unpredictably or destroys it | Right click this item then left click on a corrupted item to apply it. |
| Awakened Sextant | `CurrencyAddAtlasModHigh` | Adds or rerolls a modifier on a Voidstone. | Right click this item then left click a Voidstone to apply it. |
| Bestiary Orb | `CurrencyItemiseCapturedMonster` | Stores a Beast in an item | Right click on this item then left click on a Beast in your Menagerie to itemise the Beast. |
| Blazing Flux | `CurrencyArcaneFluxFire` | Transforms all [Cold] and [Lightning] Resistance modifiers on an item to equivalent [Fire] Resistance modifiers | Right click this item then left click on a magic or rare item to apply it. |
| Blessing of Chayula | `CurrencyBreachUpgradeUniqueChaos` | Upgrades a breach unique item or breachstone to a more powerful version | Right click this item then left click an applicable breach unique item to upgrade it. |
| Blessing of Esh | `CurrencyBreachUpgradeUniqueLightning` | Upgrades a breach unique item or breachstone to a more powerful version | Right click this item then left click an applicable breach unique item to upgrade it. |
| Blessing of Tul | `CurrencyBreachUpgradeUniqueCold` | Upgrades a breach unique item or breachstone to a more powerful version | Right click this item then left click an applicable breach unique item to upgrade it. |
| Blessing of Uul-Netol | `CurrencyBreachUpgradeUniquePhysical` | Upgrades a breach unique item or breachstone to a more powerful version | Right click this item then left click an applicable breach unique item to upgrade it. |
| Blessing of Xoph | `CurrencyBreachUpgradeUniqueFire` | Upgrades a breach unique item or breachstone to a more powerful version | Right click this item then left click an applicable breach unique item to upgrade it. |
| Blighted Scouting Report | `AtlasScoutingReportBlighted` | Reroll all of Kirac's Atlas Missions, including at least one Blighted Map. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Bloodstained Fossil | `CurrencyDelveCraftingVaal` | Corrupted
Has a Corrupted implicit modifier | Place in a Resonator to influence item crafting. |
| Bound Fossil | `CurrencyDelveCraftingMinionsAuras` | More Minion, Aura or Curse modifiers | Place in a Resonator to influence item crafting. |
| ★ Brutal Orb of Sacrifice | `CurrencyIncursionMutateCorruptionEnchantWeapon` | Upgrades a [Corrupted|Corruption] Enchantment on a [ItemRarity|Rare] Weapon or Quiver
and removes a random Modifier | Right click this item then left click on a corrupted item to apply it. |
| Celestial Alloy | `CurrencyVerisiumAlloy10` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Charged Compass | `CurrencyItemisedSextantModifier` |  | Right click on this item then left click on a Voidstone to apply the itemised Sextant Modifier to the Voidstone. |
| Chilling Flux | `CurrencyArcaneFluxCold` | Transforms all [Fire] and [Lightning] Resistance modifiers on an item to equivalent [Cold] Resistance modifiers | Right click this item then left click on a magic or rare item to apply it. |
| Comprehensive Scouting Report | `AtlasScoutingReportMoreHidden` | Reroll all of Kirac's Atlas Missions, adding additional mission options. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Concentrated Liquid Fear | `DistilledEmotion8` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Concentrated Liquid Isolation | `DistilledEmotion10` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Concentrated Liquid Suffering | `DistilledEmotion9` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Core Destabiliser | `CurrencyIncursionModifySoulCore` | Modifies a [SoulCore|Soul Core] unpredictably, with a chance to destroy it | Right click this item then left click on a soul core to apply it. |
| Corroded Fossil | `CurrencyDelveCraftingBleedPoison` | More Physical Ailment or Chaos Ailment modifiers
No Elemental modifiers | Place in a Resonator to influence item crafting. |
| ★ Corrupt | `CurrencyIncursionCorrupt1` | — | — |
| Corrupted Verisium | `CurrencyVerisiumMetalVaal1` |  | Can be used at the Verisium Anvil to transform Equipment. |
| Crackling Flux | `CurrencyArcaneFluxLightning` | Transforms all [Fire] and [Cold] Resistance modifiers on an item to equivalent [Lightning] Resistance modifiers | Right click this item then left click on a magic or rare item to apply it. |
| Cryptic Key | `StrongboxKey` | Opens an unopened [Strongbox] allowing it to be opened an additional time | Right click this item then left click a Strongbox to open it. May only be used once per Strongbox. |
| ★ Crystallised Corruption | `CurrencyIncursionDoubleCorruptGem` | Modifies a [Corrupted] Skill Gem unpredictably or destroys it | Right click this item then left click on a corrupted gem to apply it. |
| Cyclonic Alloy | `CurrencyVerisiumAlloy6` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Deft Fossil | `CurrencyDelveCraftingEnchant` | More Critical modifiers
No Attribute modifiers | Place in a Resonator to influence item crafting. |
| Delirious Scouting Report | `AtlasScoutingReportDelirium` | Reroll all of Kirac's Atlas Missions, adding layers of Delirium to all non-Unique Maps. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Dense Fossil | `CurrencyDelveCraftingDefences` | More Defence modifiers
No Life Modifiers | Place in a Resonator to influence item crafting. |
| Deregulation Scroll | `CurrencyHarbingerBlessingHelmet` | Upgrades The Tempest's Binding to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Diluted Liquid Greed | `DistilledEmotion3` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Diluted Liquid Guilt | `DistilledEmotion2` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Diluted Liquid Ire | `DistilledEmotion1` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| ★ Eldritch Chaos Orb | `CurrencyEldritchRerollRare` | If The Searing Exarch is dominant, reroll prefix modifiers. If The Eater of Worlds is dominant, reroll suffix modifiers. | Right click this item then left click a rare item with The Searing Exarch or The Eater of Worlds dominance to apply it. |
| ★ Eldritch Exalted Orb | `CurrencyEldritchAddModToRare` | If The Searing Exarch is dominant, add a prefix modifier. If The Eater of Worlds is dominant, add a suffix modifier. | Right click this item then left click a rare item with The Searing Exarch or The Eater of Worlds dominance to apply it. Rare items can have up to six random modifiers. |
| ★ Eldritch Orb of Annulment | `CurrencyEldritchRemoveMod` | If The Searing Exarch is dominant, remove a prefix modifier. If The Eater of Worlds is dominant, remove a suffix modifier. | Right click this item then left click on a magic or rare item with The Searing Exarch or The Eater of Worlds dominance to apply it. |
| Electroshock Scroll | `CurrencyHarbingerBlessingSword` | Upgrades The Rippling Thoughts to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Elevated Sextant | `CurrencyAddAtlasModMaven` | Adds or rerolls a modifier on a Voidstone. | Right click this item then left click a Voidstone to apply it. |
| Engineer's Orb | `CurrencyStrongboxQuality` | Improves the quality of a Strongbox | Right click this item then left click a Strongbox to apply it. Has greater effect on lower rarity Strongboxes. The maximum quality is 20%. |
| Enkindling Orb | `CurrencyEnkindlingOrb` | Adds an enchantment to a utility flask that will improve it but prevent it from gaining charges during its effect. Replaces any existing enchantment. | Right click this item then left click a flask to apply it. |
| Exceptional Eldritch Ember | `CurrencyEldritchEmber4` | Adds an Exceptional Searing Exarch implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Eater of Worlds implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Exceptional Eldritch Ichor | `CurrencyEldritchIchor4` | Adds an Exceptional Eater of Worlds implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Searing Exarch implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Exceptional Verisium | `CurrencyVerisiumMetal2` |  | Can be used at the Verisium Anvil to transform Equipment. |
| Exotic Coinage | `CurrencyRefreshExpedition` |  | This item is no longer usable. |
| Expansive Alloy | `CurrencyVerisiumAlloy4` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Explorer's Scouting Report | `AtlasScoutingReportExplorers` | Reroll all of Kirac's Atlas Missions, using uncompleted Maps where possible. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Faceted Fossil | `CurrencyDelveCraftingGemLevel` | More Gem modifiers | Place in a Resonator to influence item crafting. |
| Facetor's Lens | `CurrencyAddGemExperience` | Adds stored experience to a gem, up to its maximum level | Right click this item then left click a gem to apply it. |
| ★ Fortified Orb of Sacrifice | `CurrencyIncursionMutateCorruptionEnchantArmour` | Upgrades a [Corrupted|Corruption] Enchantment on a [ItemRarity|Rare] Armour
and removes a random Modifier | Right click this item then left click on a corrupted item to apply it. |
| Founders Verisium | `CurrencyVerisiumMetalKalguur1` |  | Can be used at the Verisium Anvil to transform Equipment. |
| Fractured Fossil | `CurrencyDelveCraftingMirror` | Creates a split copy. Cannot be used to split Influenced,
Enchanted, Fractured, or Synthesised items. | Place in a Resonator to influence item crafting. |
| Fragmentation Scroll | `CurrencyHarbingerBlessingQuiver` | Upgrades The Fracturing Spinner to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Frigid Fossil | `CurrencyDelveCraftingCold` | More Cold modifiers
No Fire modifiers | Place in a Resonator to influence item crafting. |
| Gilded Fossil | `CurrencyDelveCraftingSellPrice` | Item is overvalued by vendors | Place in a Resonator to influence item crafting. |
| Gnawed Jawbone | `AbyssalBenchTicketWeaponLow` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Weapon or [Quiver] | Right click this item then left click a Rare item to apply it. |
| Gnawed Rib | `AbyssalBenchTicketArmourLow` | [Abyssalify|Desecrates] a [ItemRarity|Rare] [EquipArmour|Armour] | Right click this item then left click a Rare item to apply it. |
| Gold | `GoldCoin` | Can be spent at Vendors. |  |
| Golden Vulture Feather | `CurrencyVultureFeather` |  | A discarded Avian feather with an unknown purpose |
| Grand Eldritch Ember | `CurrencyEldritchEmber3` | Adds a Grand Searing Exarch implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Eater of Worlds implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Grand Eldritch Ichor | `CurrencyEldritchIchor3` | Adds a Grand Eater of Worlds implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Searing Exarch implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Greater Eldritch Ember | `CurrencyEldritchEmber2` | Adds a Greater Searing Exarch implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Eater of Worlds implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Greater Eldritch Ichor | `CurrencyEldritchIchor2` | Adds a Greater Eater of Worlds implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Searing Exarch implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Haemocombustion Scroll | `CurrencyHarbingerBlessingStaff` | Upgrades The Enmity Divine to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Harbinger's Orb | `CurrencyUpgradeMapTier` | Reforges a map item as another of a higher tier | Right click this item then left click a map to apply it. |
| Hollow Fossil | `CurrencyDelveCraftingAbyss` | Has an Abyssal socket | Place in a Resonator to influence item crafting. |
| Imprint | `CurrencyImprint` | Creates an Imprint of a magic item that can be restored (Eternal Orb) | Backup magic item before risky crafting |
| Imprinted Bestiary Orb | `CurrencyItemisedCapturedMonster` | — | — |
| Influenced Scouting Report | `AtlasScoutingReportGuardian` | Reroll all of Kirac's Atlas Missions, including at least one Shaper Guardian, Elder Guardian, or Elderslayer Map. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Infused Engineer's Orb | `CurrencyStrongboxQualityInfused` | Greatly improves the quality and rewards of a Strongbox and strengthens its defenders | Right click this item then left click a Strongbox to apply it. |
| Instilling Orb | `CurrencyInstillingOrb` | Adds an enchantment to a utility flask that will cause it to be used when certain conditions are met. Replaces any existing enchantment. | Right click this item then left click a flask to apply it. |
| Jade Kiwi Feather | `CurrencyKiwiFeather` |  | A discarded Avian feather with an unknown purpose |
| Jagged Fossil | `CurrencyDelveCraftingPhysical` | More Physical modifiers
No Chaos modifiers | Place in a Resonator to influence item crafting. |
| Journeyman Cartographer's Seal | `CurrencySealMapMid` | Uncompletes a yellow or white map on the Atlas | Right click this item then left click a yellow or white map on the Atlas to apply it. |
| Lesser Eldritch Ember | `CurrencyEldritchEmber1` | Adds a Lesser Searing Exarch implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Eater of Worlds implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Lesser Eldritch Ichor | `CurrencyEldritchIchor1` | Adds a Lesser Eater of Worlds implicit modifier to a Body Armour, Boots, Gloves or Helmet. This replaces any existing implicit modifiers other than Searing Exarch implicit modifiers. | Right click this item then left click a normal, magic or rare item to apply it. Cannot be used on Shaper, Elder or Elderslayer influenced items. |
| Liquid Despair | `DistilledEmotion7` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Liquid Disgust | `DistilledEmotion6` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Liquid Envy | `DistilledEmotion5` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Liquid Paranoia | `DistilledEmotion4` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Lucent Fossil | `CurrencyDelveCraftingMana` | More Mana modifiers
No Speed modifiers | Place in a Resonator to influence item crafting. |
| Master Cartographer's Seal | `CurrencySealMapHigh` | Uncompletes any map on the Atlas | Right click this item then left click any map on the Atlas to apply it. |
| Medved's Crest of the Circle | `CurrencyVerisiumMetalUnique1` |  | Can be used at the Verisium Anvil to transform [Rarity|Unique] items. |
| Metallic Fossil | `CurrencyDelveCraftingLightning` | More Lightning modifiers
No Physical modifiers | Place in a Resonator to influence item crafting. |
| Mutated Verisium | `CurrencyVerisiumMetalBreach1` |  | Can be used at the Verisium Anvil to transform Equipment. |
| Mystic Alloy | `CurrencyVerisiumAlloy8` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Necromancy Net | `BestiaryNet11` | Can be used on Beast corpses of all levels.
Activate to use this type of Net when capturing Beasts. |  |
| Oil Extractor | `CurrencyExtractOil` | Destroys an Anointed Item to recover one of the Oils that was used to apply that Anointment | Right click this item then left click an Anointed item to destroy it. |
| Olroth's Crest of the Sun | `CurrencyVerisiumMetalUnique4` |  | Can be used at the Verisium Anvil to transform [Rarity|Unique] items. |
| Operative's Scouting Report | `AtlasScoutingReportJuiced` | Reroll all of Kirac's Atlas Missions, granting missions with rewarding implicit modifiers. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Orb of Conflict | `CurrencyConflictOrb` | Unpredictably raise the strength of one Searing Exarch or Eater of Worlds modifier on an item and lower the strength of another. Lesser modifiers that have their strength lowered will be removed. | Right click this item then left click a non-unique item to apply it. Can only be used on items that have both a Searing Exarch and an Eater of Worlds implicit modifier. The chance of raising or lowering a modifier depends on its relative strength. |
| Orb of Dominance | `CurrencyUpgradeInfluenceMod` | Removes one Influenced Modifier from an item with at least two Influenced Modifiers and upgrades another Influenced Modifier. Upgrading a modifier of the highest tier transforms the modifier into an Elevated Modifier. Attempting to upgrade an Elevated Modifier rerolls its values. Can be used on Body Armours, Boots, Gloves and Helmets. | Right click this item then left click an item with at least two Influenced Modifiers to apply it. |
| Orb of Horizons | `CurrencyRerollMapType` | Reforges a map item as another of the same tier | Right click this item then left click a map to apply it. |
| Orb of Unmaking | `CurrencyAtlasPassiveRefund` | Grants an atlas passive skill refund point | Right click on this item to use it. |
| Otherworldly Scouting Report | `AtlasScoutingReportBreachstone` | Reroll all of Kirac's Atlas Missions, including at least one Breachstone. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Perandus Coin | `CurrencyPerandusCoin` |  | Trade coins to Cadiro Perandus. |
| Perfect Flux | `CurrencyUpgradeInherentTo20` | Upgrades the Skills on an item to Level 20 | Right click this item then left click an item to apply it. |
| Perfect Fossil | `CurrencyDelveCraftingQuality` | Improved Quality | Place in a Resonator to influence item crafting. |
| Portal Scroll | `CurrencyPortal` | Creates a portal to town | Right click on this item to use it. |
| Potent Liquid Contempt | `EndgameDistilledEmotion3` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Potent Liquid Ferocity | `EndgameDistilledEmotion2` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Potent Liquid Melancholy | `EndgameDistilledEmotion1` | Removes a random modifer and Augments a [Rarity|Rare] [BasicJewel|Basic Jewel] with a
new guaranteed [Crafted] modifier | Can be used at The Withered Willow to Instil Amulets with a Notable Passive Skill.
Right click this item then left click a Rare Jewel to apply it. |
| Preserved Cranium | `AbyssalBenchTicketJewel` | [Abyssalify|Desecrates] a [ItemRarity|Rare] [Jewel] | Right click this item then left click a Rare item to apply it. |
| Preserved Jawbone | `AbyssalBenchTicketWeapon` | [Abyssalify|Desecrates] a [ItemRarity|Rare] Weapon or [Quiver] | Right click this item then left click a Rare item to apply it. |
| Preserved Rib | `AbyssalBenchTicketArmour` | [Abyssalify|Desecrates] a [ItemRarity|Rare] [EquipArmour|Armour] | Right click this item then left click a Rare item to apply it. |
| Preserved Vertebrae | `AbyssalBenchTicketWaystone` | [Abyssalify|Desecrates] a [ItemRarity|Rare] [Waystone] | Right click this item then left click a Rare item to apply it. |
| Primal Crystallised Lifeforce | `HarvestSeedBlue` |  | Can be used at the Horticrafting bench in your hideout. |
| Prime Regrading Lens | `CurrencyRerollSkillQualityType` | Change the type of quality of a skill gem with quality to another random quality | Right click this item then left click a skill gem to apply it. |
| Prime Sextant | `CurrencyAddAtlasModMid` | Adds or rerolls a modifier on a Voidstone. | Right click this item then left click a Voidstone to apply it. |
| Prismatic Alloy | `CurrencyVerisiumAlloy7` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Prismatic Fossil | `CurrencyDelveCraftingElemental` | More Elemental modifiers
No Physical Ailment or Chaos Ailment modifiers | Place in a Resonator to influence item crafting. |
| Pristine Fossil | `CurrencyDelveCraftingLife` | More Life modifiers
No Defence modifiers | Place in a Resonator to influence item crafting. |
| Prophecy | `CurrencyItemisedProphecy` | — | — |
| Protective Alloy | `CurrencyVerisiumAlloy3` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Rainbow Toucan Feather | `CurrencyToucanFeather` |  | A discarded Avian feather with an unknown purpose |
| Refined Adaptive Catalyst | `CurrencyJewelQualityAttribute` | Adds [Quality|quality] that enhances [Attributes|Attribute] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Carapace Catalyst | `CurrencyJewelQualityDefences` | Adds [Quality|quality] that enhances [Armour], [Evasion] and [EnergyShield|Energy Shield] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Chayula's Catalyst | `CurrencyJewelQualityChaos` | Adds [Quality|quality] that enhances [Chaos] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Esh's Catalyst | `CurrencyJewelQualityLightning` | Adds [Quality|quality] that enhances [Lightning] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Flesh Catalyst | `CurrencyJewelQualityLife` | Adds [Quality|quality] that enhances Life modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Neural Catalyst | `CurrencyJewelQualityMana` | Adds [Quality|quality] that enhances Mana modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Reaver Catalyst | `CurrencyJewelQualityAttack` | Adds [Quality|quality] that enhances [Attack] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Sibilant Catalyst | `CurrencyJewelQualityCaster` | Adds [Quality|quality] that enhances [Spell|Caster] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Skittering Catalyst | `CurrencyJewelQualitySpeed` | Adds [Quality|quality] that enhances Speed modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Tul's Catalyst | `CurrencyJewelQualityCold` | Adds [Quality|quality] that enhances [Cold] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Uul-Netol's Catalyst | `CurrencyJewelQualityPhysical` | Adds [Quality|quality] that enhances [Physical] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Refined Xoph's Catalyst | `CurrencyJewelQualityFire` | Adds [Quality|quality] that enhances [Fire] modifiers on a jewel
Replaces other quality types | Right click this item then left click a jewel to apply it. |
| Reinforced Iron Net | `BestiaryNet5` | Effective against Beasts of levels 37 to 56.
Activate to use this type of Net when capturing Beasts. |  |
| Reinforced Rope Net | `BestiaryNet2` | Effective against Beasts of levels 7 to 23.
Activate to use this type of Net when capturing Beasts. |  |
| Reinforced Steel Net | `BestiaryNet8` | Effective against Beasts of levels 60 to 75.
Activate to use this type of Net when capturing Beasts. |  |
| Revered Starlit Ore | `CurrencyVerisiumOreUniqueTheUnleashed` |  | Can be used at the Verisium Anvil to forge a new [Rarity|Unique] item. |
| ★ Royal Orb of Sacrifice | `CurrencyIncursionMutateCorruptionEnchantJewel` | Upgrades a [Corrupted|Corruption] Enchantment on a [ItemRarity|Rare] Jewel
and removes a random Modifier | Right click this item then left click on a corrupted item to apply it. |
| Runic Alloy | `CurrencyVerisiumAlloy1` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Sacred Crystallised Lifeforce | `HarvestSeedBoss` |  | Can be used at the Horticrafting bench in your hideout. |
| Sanctified Fossil | `CurrencyDelveCraftingLuckyModRolls` | Numeric modifier values are lucky
High Level modifiers are more common | Place in a Resonator to influence item crafting. |
| Scorched Fossil | `CurrencyDelveCraftingFire` | More Fire modifiers
No Cold modifiers | Place in a Resonator to influence item crafting. |
| Secondary Regrading Lens | `CurrencyRerollSupportQualityType` | Change the type of quality of a support gem with quality to another random quality | Right click this item then left click a support gem to apply it. |
| Serrated Fossil | `CurrencyDelveCraftingAttackMods` | More Attack modifiers
Fewer Caster modifiers | Place in a Resonator to influence item crafting. |
| Shuddering Fossil | `CurrencyDelveCraftingSpeed` | More Speed modifiers
No Mana modifiers | Place in a Resonator to influence item crafting. |
| Silver Coin | `CurrencySilverCoin` |  | Cross Navali's palm with silver to receive a prophecy. |
| Simple Iron Net | `BestiaryNet4` | Effective against Beasts of levels 25 to 46.
Activate to use this type of Net when capturing Beasts. |  |
| Simple Rope Net | `BestiaryNet1` | Effective against Beasts of levels 1 to 13.
Activate to use this type of Net when capturing Beasts. |  |
| Simple Sextant | `CurrencyAddAtlasMod` | Adds or rerolls a modifier on a Voidstone. | Right click this item then left click a Voidstone to apply it. |
| Simple Steel Net | `BestiaryNet7` | Effective against Beasts of levels 58 to 70.
Activate to use this type of Net when capturing Beasts. |  |
| Singular Scouting Report | `AtlasScoutingReportUnique` | Reroll all of Kirac's Atlas Missions, including at least one Unique map. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Sovereign Alloy | `CurrencyVerisiumAlloy9` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Specularity Scroll | `CurrencyHarbingerBlessingShield` | Upgrades The Unshattered Will to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Starlit Ore | `CurrencyVerisiumOreUniqueSerlesGrit` |  | Can be used at the Verisium Anvil to forge a new [Rarity|Unique] item. |
| Strong Iron Net | `BestiaryNet6` | Effective against Beasts of levels 48 to 66.
Activate to use this type of Net when capturing Beasts. |  |
| Strong Rope Net | `BestiaryNet3` | Effective against Beasts of levels 15 to 35.
Activate to use this type of Net when capturing Beasts. |  |
| Strong Steel Net | `BestiaryNet9` | Effective against Beasts of levels 64 and above.
Activate to use this type of Net when capturing Beasts. |  |
| Stygian Peacock Feather | `CurrencyPeacockFeather` |  | A discarded Avian feather with an unknown purpose |
| Surveyor's Compass | `CurrencyItemiseSextantModifier` | Stores a Sextant Modifier in an item | Right click on this item then left click on a Voidstone to itemise an applied Sextant Modifier. |
| Swift Alloy | `CurrencyVerisiumAlloy5` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Tailoring Orb | `CurrencyHeistArmourEnchant` | Adds or replaces an enchantment on a body armour. This may reforge the body armour's sockets. | Right click this item then left click on the item you wish to modify. |
| Tainted Armourer's Scrap | `CurrencyHellscapeArmourQuality` | Randomises the quality of a corrupted armour | Right click this item then left click a corrupted armour to apply it. The maximum random quality is 29%. |
| Tainted Blacksmith's Whetstone | `CurrencyHellscapeWeaponQuality` | Randomises the quality of a corrupted weapon | Right click this item then left click a corrupted weapon to apply it. The maximum random quality is 29%. |
| ★ Tainted Chaos Orb | `CurrencyHellscapeRerollRare` | Unpredictably either reforges a corrupted rare item with new random modifiers or removes all of its modifiers | Right click this item then left click a corrupted rare item to apply it. |
| Tainted Divine Teardrop | `CurrencyHellscapeUpgradeModTier` | Unpredictably raises or lowers the tier of each modifier on a corrupted rare item | Right click this item then left click a corrupted rare item to apply it. |
| ★ Tainted Exalted Orb | `CurrencyHellscapeAddModToRare` | Unpredictably adds or removes a modifier on a corrupted rare item | Right click this item then left click a corrupted rare item to apply it. Rare items can have up to six random modifiers. |
| Tainted Mythic Orb | `CurrencyHellscapeUpgradeToUnique` | Unpredictably either upgrades a corrupted item to unique rarity or destroys it | Right click this item then left click a corrupted item to apply it. Cannot apply to Maps. |
| Tangled Fossil | `CurrencyDelveCraftingRandom` | Makes a random modifier type much more likely and prevents 
another random modifier type. Effects revealed once resonator is
fully socketed. | Place in a Resonator to influence item crafting. |
| Tempering Orb | `CurrencyHeistWeaponEnchant` | Adds or replaces an enchantment on a weapon. This may reforge the weapon's sockets. | Right click this item then left click on the item you wish to modify. |
| Thaumaturgic Flux (Level 1) | `CurrencySetKalguuranSkillGemLevel1` | Sets a Kalguuran Skill Gem to level 1 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 10) | `CurrencySetKalguuranSkillGemLevel10` | Upgrades a Kalguuran Skill Gem to level 10 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 11) | `CurrencySetKalguuranSkillGemLevel11` | Upgrades a Kalguuran Skill Gem to level 11 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 12) | `CurrencySetKalguuranSkillGemLevel12` | Upgrades a Kalguuran Skill Gem to level 12 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 13) | `CurrencySetKalguuranSkillGemLevel13` | Upgrades a Kalguuran Skill Gem to level 13 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 14) | `CurrencySetKalguuranSkillGemLevel14` | Upgrades a Kalguuran Skill Gem to level 14 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 15) | `CurrencySetKalguuranSkillGemLevel15` | Upgrades a Kalguuran Skill Gem to level 15 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 16) | `CurrencySetKalguuranSkillGemLevel16` | Upgrades a Kalguuran Skill Gem to level 16 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 17) | `CurrencySetKalguuranSkillGemLevel17` | Upgrades a Kalguuran Skill Gem to level 17 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 18) | `CurrencySetKalguuranSkillGemLevel18` | Upgrades a Kalguuran Skill Gem to level 18 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 19) | `CurrencySetKalguuranSkillGemLevel19` | Upgrades a Kalguuran Skill Gem to level 19 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 2) | `CurrencySetKalguuranSkillGemLevel2` | Upgrades a Kalguuran Skill Gem to level 2 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 20) | `CurrencySetKalguuranSkillGemLevel20` | Upgrades a Kalguuran Skill Gem to level 20 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 3) | `CurrencySetKalguuranSkillGemLevel3` | Upgrades a Kalguuran Skill Gem to level 3 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 4) | `CurrencySetKalguuranSkillGemLevel4` | Upgrades a Kalguuran Skill Gem to level 4 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 5) | `CurrencySetKalguuranSkillGemLevel5` | Upgrades a Kalguuran Skill Gem to level 5 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 6) | `CurrencySetKalguuranSkillGemLevel6` | Upgrades a Kalguuran Skill Gem to level 6 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 7) | `CurrencySetKalguuranSkillGemLevel7` | Upgrades a Kalguuran Skill Gem to level 7 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 8) | `CurrencySetKalguuranSkillGemLevel8` | Upgrades a Kalguuran Skill Gem to level 8 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgic Flux (Level 9) | `CurrencySetKalguuranSkillGemLevel9` | Upgrades a Kalguuran Skill Gem to level 9 | Right click this item then left click a Kalguuran Skill gem to apply it. |
| Thaumaturgical Net | `BestiaryNet10` | Effective against Beasts of levels 68 and above.
Activate to use this type of Net when capturing Beasts. |  |
| The Runebinder's Alloy | `CurrencyVerisiumAlloy12` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| The Runefather's Alloy | `CurrencyVerisiumAlloy13` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Time-light Scroll | `CurrencyHarbingerBlessingBelt` | Upgrades The Flow Untethered to a more powerful version | Right click this item then left click an applicable Harbinger unique item to upgrade it. |
| Transcendent Alloy | `CurrencyVerisiumAlloy11` | Removes a random modifier and augments a [ItemRarity|Rare] item with a new guaranteed modifier | Right click this item then left click a Rare item to apply it. |
| Uhtred's Crest of the Chalice | `CurrencyVerisiumMetalUnique3` |  | Can be used at the Verisium Anvil to transform [Rarity|Unique] items. |
| Uncarved Gemstone | `CurrencySkillGemToken` |  | Trade this in to Siosa inside the Library for a Skill Gem |
| Unshaping Orb | `CurrencyRespecShapersOrb` | Downgrades a map on the Atlas | Right click this item then left click a shaped map on the atlas to downgrade it. You can then earn the Shaper's Orb again to reshape another map afterwards. |
| Vaal Arcanist's Infuser | `CurrencyIncursionCasterWeaponQuality` | Improves the [Quality|quality] of a wand, staff or sceptre,
exceeding maximum quality by up to 10% with a chance of [Corrupted|Corrupting] it | Right click this item then left click a wand, staff or sceptre to apply it. Can only be used on items at or above maximum quality. |
| Vaal Armourer's Infuser | `CurrencyIncursionWeaponOrArmourQualityHigh` | Improves the [Quality|quality] of an [Armour],
exceeding maximum quality by up to 10% with a chance of [Corrupted|Corrupting] it | Right click this item then left click an armour to apply it. Can only be used on items at or above maximum quality. |
| Vaal Blacksmith's Infuser | `CurrencyIncursionMartialWeaponQuality` | Improves the [Quality|quality] of a [MartialWeapon|Martial Weapon],
exceeding maximum quality by up to 10% with a chance of [Corrupted|Corrupting] it | Right click this item then left click a martial weapon to apply it. Can only be used on items at or above maximum quality. |
| Vaal Cultivation Orb | `CurrencyIncursionMutateUnique` | Replaces up to 2 modifiers on a [Corrupted] [UniqueCulture|Vaal Unique]
Replaces other [ItemRarity|Uniques] with a Corrupted Unique of the same Item Class | Right click this item then left click on a unique item to apply it. |
| ★ Vaal Scouting Report | `AtlasScoutingReportCorrupted` | Reroll all of Kirac's Atlas Missions, corrupting all non-Unique Maps. | Right click this item while viewing Kirac's Atlas Missions to use it. |
| Venerable Starlit Ore | `CurrencyVerisiumOreUniqueEyesOfTheRunefather` |  | Can be used at the Verisium Anvil to forge a new [Rarity|Unique] item. |
| Veridical Starlit Ore | `CurrencyVerisiumOreUniqueEventidePetals` |  | Can be used at the Verisium Anvil to forge a new [Rarity|Unique] item. |
| Verisium | `CurrencyVerisiumMetal1` |  | Can be used at the Verisium Anvil to transform Equipment. |
| Vial of Awakening | `CurrencyIncursionVialPoison` |  | Sacrifice this item on the Altar of Sacrifice along with Apep's Slumber to transform it. |
| Vial of Consequence | `CurrencyIncursionVialMinion` |  | Sacrifice this item on the Altar of Sacrifice along with Coward's Chains to transform it. |
| Vial of Dominance | `CurrencyIncursionVialTrap` |  | Sacrifice this item on the Altar of Sacrifice along with Architect's Hand to transform it. |
| Vial of Fate | `CurrencyIncursionVialFire` |  | Sacrifice this item on the Altar of Sacrifice along with Story of the Vaal to transform it. |
| Vial of Sacrifice | `CurrencyIncursionVialBossAmulet` |  | Sacrifice this item on the Altar of Sacrifice along with Sacrificial Heart to transform it. |
| Vial of Summoning | `CurrencyIncursionVialHealing` |  | Sacrifice this item on the Altar of Sacrifice along with Mask of the Spirit Drinker to transform it. |
| Vial of Transcendence | `CurrencyIncursionVialBossJewel` |  | Sacrifice this item on the Altar of Sacrifice along with any Tempered Flesh, Tempered Spirit or Tempered Mind to transform it. |
| Vial of the Ghost | `CurrencyIncursionVialBossFlask` |  | Sacrifice this item on the Altar of Sacrifice along with Soul Catcher to transform it. |
| Vivid Crystallised Lifeforce | `HarvestSeedGreen` |  | Can be used at the Horticrafting bench in your hideout. |
| Void Flux | `CurrencyArcaneFluxChaos` | Transforms all [Fire], [Cold] and [Lightning] Resistance modifiers on an item to equivalent [Chaos] resistance modifiers | Right click this item then left click on a magic or rare item to apply it. |
| Vorana's Crest of the Scythe | `CurrencyVerisiumMetalUnique2` |  | Can be used at the Verisium Anvil to transform [Rarity|Unique] items. |
| Warding Starlit Ore | `CurrencyVerisiumOreUniqueStolvarheim` |  | Can be used at the Verisium Anvil to forge a new [Rarity|Unique] item. |
| Wild Crystallised Lifeforce | `HarvestSeedRed` |  | Can be used at the Horticrafting bench in your hideout. |

