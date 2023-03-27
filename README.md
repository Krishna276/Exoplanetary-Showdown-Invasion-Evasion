# solid-enigma
This is a repo for the game ___ made by CoDerection:
* Krishna Ranchhod
* Colden Sapir
* Samuel Harrison
* James Venkatesan
* Harry Shi
## How the game works
Put simply, there's an attacker, trying to invade the Earth with an alien army. There is also a defender, who is trying to save the Earth from this. The defender can place turrets on the battlefield, and the attacker will summon aliens that will attempt to reach earth, with the hope of damaging the Earth's health. The attacker wins if Earth's health reaches zero (or below), and the defender wins if the Earth's health is greater than zero when the attacker runs out of a certian rescource (this is TBD, but we're thinking it should be time).
## The Battlefield
There are multiple tiles, each with a different cost associated with it for traversal by an alien. The defender can place thier turrets on these tiles with no restrictions, except for that a valid path must exist from all portals to the tile with Earth on it. There may also be certian types of tile that cannot have turrets on them.
### Types of tile
Not all of these may be implemented.
|Type of tile|Attacker Traversal Cost|What it does|
|-|-|-|
|Portal|0|Attackers start here.|
|Earth|0|This is the tile where the Earth is.|
|Empty space|3|A normal tile, for use by both the attacker and defender.|
|Slowness|9|Slows down aliens on these tiles.|
|Speed|1|Speeds up aliens on these tiles.|
|No damage|0|Aliens do not take damage while on these tiles.|
|Hazard|10|Aliens will take extra damage in addition to that dealt by turrets.|
|Block|$\infty$|ALiens cannot traverse this tile, turrets cannot be placed on these tiles either.|
### Alien behaviour
Aliens will follow the path of least resistance to get to the earth. WHen they reach it, they will be able to attack the earth. The earth has some natural defences, and will deal damage to every alien that attacks it.
## Gameplay
The attacker will attack in waves, and the defender can only adjust thier turrets in between (this stops them from just blocking in any aliens on the battlefield).
### Summoning Aliens
The attacker must use a currency to summon aliens. To stop the attacker from summoning an endless wave of enemies, any earnt currency will only be awarded after the wave is completed. The longer an individual alien survives, the more currency it will earn.
### Summoning Turrets
To prevent the defender from blocking in a bunch of aliens, they are not allowed to place turrets during a wave. They earn thier currency (for buying turrets) by killing off aliens (this works whether it was the Earth or a turret that killed the alien).
