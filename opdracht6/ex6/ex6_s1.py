"""
Programma naam: bruteforce.py
Gemaakt door: Mark Jansen (13385569)
Datum: 18 december, 2022

Samenvatting: Dit programma lost SAT problemen op door
              gebruik te maken van een bruteforce methode.

Gebruik:
- python3 bruteforce.py < <filename>.input
- U ziet het resultaat.
"""
import fileinput
import itertools


def verify_clause(clause, literals):
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
            if literals[literal[1:]] == 0:
                return True
        else:
            if literals[literal] == 1:
                return True
    return False


def is_satisfiable(clauses, literals):
    """
    Call verify clause function to check if
    all the clauses can be satisfied.

    clause: A clause to verify.
    literals: Literals to use during verification.

    Output: True if all satisfy, and
            otherwise false.
    """
    for clause in clauses:
        if verify_clause(clause, literals) is False:
            return False
    return True


def bruteforce(clauses, keys):
    """
    Use bruteforce to find the correct
    literal assignments.

    clause: A clause to verify.
    keys: The literals in the clauses.

    Output: The correct literal and value pairs,
            else and empty dict.
    """
    for values in list(itertools.product([0, 1], repeat=len(keys))):
        literals = {keys[i]: values[i] for i in range(0, len(values))}
        if is_satisfiable(clauses, literals) is True:
            return literals
    return {}


def assign(input, l_cnt):
    """
    Create a dict and assign the value True to the keys
    or false to the keys depending on int val.

    input: A list representing the keys.
    l_cnt: The amount of distinct keys/literals given.

    Output: A dict with keys and values.
    """
    literals = dict()
    for line in input[1:1 + int(l_cnt)]:
        literals[line[0]] = 0
    return literals


if __name__ == "__main__":
    """
    Read the input and command functions to solve
    the satisfiability problem.

    Side-Effect: On succes print l_cnt, c_cnt,
                 keys and their values, and
                 at last the clauses. Else
                 print Niet vervulbaar.
    """
    input = [line.split() for line in fileinput.input()]
    l_cnt, c_cnt = input[0][0], input[0][1]

    literals = assign(input, l_cnt)
    clauses = [line for line in input[1 + int(l_cnt):]]

    result = bruteforce(clauses, list(literals.keys()))

    if result:
        print(l_cnt, c_cnt)
        for x in result.keys():
            print(x, result[x])
        for clause in clauses:
            print(" ".join(clause))
    else:
        print("Niet vervulbaar")
