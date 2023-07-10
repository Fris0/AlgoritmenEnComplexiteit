"""
Auteur: Mark Jansen
Studentnummer: 13385569
Gemaakt op: 08-11-2022

Samenvatting:
Een "greedy algoritme" die de hoogste waarde kiest een positie links of rechts
van de volgende rij, relatief tot de huidige positie in de huidige rij.

Gebruik:
- Run de de python code met python3 <pythonfile> < <inputfile>
- Het resultaat wordt met std:out weergegeven.
"""

import fileinput


def calculateMaxPath(all_rows):
    """
    Calculate the max path in a pyramid by storing the max value in the row.
    Uses a top-down and iterative approach.

    Output: The max-path.
    """
    for i in range(len(all_rows) - 2, -1, -1):
        upper_row = all_rows[i]
        lower_row = all_rows[i + 1]
        for j in range(len(upper_row) - 1, -1, -1):
            all_rows[i][j] = max(upper_row[j] + lower_row[j],
                                 upper_row[j] + lower_row[j + 1])
    print(all_rows[0][0])


if __name__ == "__main__":
    """
    Read the lines from an inputfile, store them in a list and run
    the algorithm.

    Side-effect: Calls calculateMaxPath function and passed the list.
    """
    all_rows = []
    for line in fileinput.input(encoding="utf-8"):
        all_rows.append(list(map(int, line.split(" "))))
    calculateMaxPath(all_rows)
