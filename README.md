# Mid or Feed

AI model that could determine a DOTA 2 player's role based on the statistics of their 20 most recent games. See included PDF of report for details.

Submitted as a course requirement for _CS 180 (Artificial Intelligence)_.

Files included:
 - `getMatches.py` - fetches 20 most recent matches of players listed in `accountIDs.txt`
 - `makeLabels.py` - creates label vector from the file `prettyProPlayers.txt`
 - `main.py` - trains an ANN with inputs `feature.csv` and `label.csv`
