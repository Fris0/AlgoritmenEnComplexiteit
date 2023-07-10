"""
Programma naam: optimized.py
Gemaakt door: Mark Jansen (13385569)
Datum: 18 december, 2022

Samenvatting: Dit programma verifieert een
              de conjunction normal form
              met de gegeven literal waarden.

Gebruik:
- python3 bruteforce.py < <filename>.input
- U ziet het resultaat.
"""
import fileinput


def verify(clause, literals):
    """
    Verify the clause given.

    clause: A clause to verify.
    literals: Literals to use during verification.

    Output: Returns true if a literal
            satisfies the clause, else
            False.

    """
    for literal in clause:
        if "~" in literal:
            if not literals[literal[1:]]:
                return True
        else:
            if literals[literal]:
                return True
    return False


def assign(input, l_cnt):
    """
    Create a dict and assign the value True to the keys
    or false to the keys depending on int val.

    input: A list representing the keys.
    l_cnt: The amount of distinct keys/literals given.

    Output: A dict with keys and values.
    """
    clauses = dict()
    for line in input[1:1 + int(l_cnt)]:
        if int(line[1]) == 1:
            clauses[str(line[0])] = True
        else:
            clauses[str(line[0])] = False
    return clauses


if __name__ == "__main__":
    """
    Read the input and command functions to check
    if the input satisfies.

    Side-Effect: On succes print Vervult formule,
                 else print Vervult formule niet.
    """
    input = [line.split() for line in fileinput.input()]
    l_cnt, c_cnt = input[0][0], input[0][1]

    if l_cnt == "Niet":
        print("Niet vervulbaar")
        exit()

    literals = assign(input, l_cnt)

    satisfiable = True
    for clause in input[1 + int(l_cnt):]:
        if (verify(clause, literals) is False):
            print("Vervult formule niet")
            satisfiable = False
    if satisfiable:
        print("Vervult formule")
