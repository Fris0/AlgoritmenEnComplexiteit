"""
Programma naam: ex6_s/optimized.py
Gemaakt door: Mark Jansen (13385569)
Datum: 18 december, 2022

Samenvatting: Dit programma lost SAT problemen op door
              gebruik te maken DPLL en unit propagation.

Gebruik:
- python3 bruteforce.py < <filename>.input
- U ziet het resultaat.


"""
import fileinput
import copy
import time


def dpll(clauses, literals):
    """
    Solve a SAT problem with the use of Davis–Putnam–Logemann–Loveland
    to optimize performance. Also makes use of unit clause propagation.

    clauses: list of clauses to satisfy
    literals: lierals of the clauses

    Output: Literals with the correct values s.t
            the problem satisfies, else empty dict.
    """
    if not clauses:
        return literals
    elif any([len(clause) == 0 for clause in clauses]):
        return {}
    else:
        var = clauses[0][0]
        if "~" in var:
            var = var[1:]

        literals[var] = 1
        new_clauses = copy.deepcopy(clauses)
        new_clauses = [clause for clause in new_clauses if var not in clause]
        for clause in new_clauses:
            if "~" + var in clause:
                clause.remove("~" + var)

        assignment = dpll(new_clauses, literals)
        if assignment:
            return assignment

        literals[var] = 0
        new_clauses = clauses
        new_clauses = [clause for clause in new_clauses if "~" +
                       var not in clause]
        for clause in new_clauses:
            if var in clause:
                clause.remove(var)

        assignment = dpll(new_clauses, literals)
        if assignment:
            return assignment

        return {}


def assign(input, l_cnt):
    """
    Create a dict and assign the value 0 to the keys.

    input: A list representing the keys.
    l_cnt: The amount of distinct keys/literals given.

    Output: A dict with key value 0.
    """
    clauses = dict()
    for line in input[1:1 + int(l_cnt)]:
        clauses[line[0]] = 0
    return clauses


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

    result = dpll(clauses, literals)

    if result:
        print(l_cnt, c_cnt)
        for x in literals.keys():
            print(x, literals[x])
        for clause in clauses:
            print(" ".join(clause))
    else:
        print("Niet vervulbaar")
