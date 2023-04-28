# Exoplanetary Showdown: Invasion Evasion
This is a repo for the game _Exoplanetary Showdown: Invasion Evasion_ made by CoDerection:
* Krishna Ranchhod
* Colden Sapir
* Samuel Harrison
* James Venkatesan
* Harry Shi
## The Game
This is part of a project for a Computer Science class.\
Remember that this game is still in development, so it doesn't work (at all) right now. We'll make it obvious as soon as it does work.
## How the game works
Put simply, there's an attacker, trying to invade the Earth with an alien army. There is also a defender, who is trying to save the Earth from this. The defender can place turrets on the battlefield, and the attacker will summon aliens that will attempt to reach earth, with the hope of damaging the Earth's health. The attacker wins if Earth's health reaches zero (or below), and the defender wins if the Earth's health is greater than zero when the attacker runs out of a certian rescource (this is TBD, but we're thinking it should be time).
## The Battlefield
There are multiple tiles, each with a different cost associated with it for traversal by an alien. The defender can place thier turrets on these tiles with almost no restrictions.
### Types of tile
Not all of these may be implemented. Tiles in order of how alien-friendly they are.
|Type of tile|Alien Traversal Cost|What it does|
|-|-|-|
|Portal|0|Aliens start here.|
|Earth|0|This is the tile where the Earth is.|
|No damage|0|Aliens do not take damage while on these tiles.|
|Speed|1|Speeds up aliens on these tiles.|
|No turret|3|Turrets cannot be placed on this tile.|
|Empty space|3|A normal tile, for use by both the attacker and defender.|
|Slowness|9|Slows down aliens on these tiles.|
|Hazard|10|Aliens will take extra damage in addition to that dealt by turrets.|
|Block|$\infty$|Aliens cannot traverse this tile, turrets cannot be placed on these tiles either.|
|No alien|$\infty$|Aliens cannot traverse this tile.|
### Alien behaviour
Aliens will follow the path of least resistance to get to the earth. When they reach it, they will be able to attack the earth. The earth has some natural defences, and will deal damage to every alien that attacks it.
## Gameplay
To stop the defender from blocking aliens in, they are subject to some turret placement rules.
### Summoning Aliens
The attacker must use a currency to summon aliens. The longer an individual alien survives, the more currency it will earn.
### Summoning Turrets
The defender earns thier currency (for buying turrets) by killing off aliens (this works whether it was the Earth or a turret that killed the alien).
#### Turret Placement Rules
This is the deciding algorithm.
1. Is the turret on a Block, No turret, Portal or Earth tile? If so, go to step 3.
2. Are all Portal tiles connected by at least 1 valid path to the Earth tile? If so, go to step 4.
3. No turret can be placed.
4. Is there an alien on the current tile? If so, go to step 6.
5. Does the defender have the required amount of currency? If so, go to step 8.
6. Is the alien on the current tile a boss? If so, go to step 3.
7. The alien is killed, the currency deducted and the turret is placed.
8. The currency deducted and the turret is placed.
