"""
Auteur: Mark Jansen
Studentnummer: 13385569
Gemaakt op: 2-12-2022

Samenvatting:
Een implementatie van een max matching algoritme. Met dit algoritme
wordt best possible matching gevonden.

Gebruik:
- Run de de python code met python3 <pythonfile> <inputfile>
- Het resultaat wordt naar standard output gestuurd.
"""
import fileinput


def find_match(graph, person, matches, examined, choices):
    """
    Find available matches for a person looking for a job.

    graph: An adjacency matrix representing a directed graph
    person: Column in graph.
    matches: current matches made.
    examined: Possible matches that have been looked at.
    choices: Integer that gives amount of possible thesis's

    Output: An array with filled with -1 if no match
            was made, else distinct student numbers.
    """
    for job in range(choices):
        if graph[person][job] != 0 and examined[job] is False:
            examined[job] = True
            if matches[job] == -1 or find_match(graph, matches[job],
                                                matches, examined, choices):
                matches[job] = person
                return True
    return False


def find_max_matching(graph, choices, stdnt_cnt):
    """
    Find max possible matching in adjacency matrix

    graph: An adjacency matrix representing a directed graph
    choices: Amount of possible thesis's to choose.
    stdnt_count: Integer that gives the amount of students.

    Output: An array with filled with -1 if no match
            was made, else distinct student numbers.
    """
    matches = [-1 for i in range(choices + 1)]
    for person in range(stdnt_cnt):
        examined = [False for i in range(choices + 1)]
        find_match(graph, person, matches, examined, choices)
    return matches


if __name__ == "__main__":
    """
    Read line(s) from input and call match finding function

    Side-effect: Print result of function to standard output.
    """
    choices = 0
    stdnt_cnt = 0
    for line in fileinput.input():
        line = list(map(int, line.split(" ")))
        choices = line[1]
        stdnt_cnt = line[0]
        fileinput.close()
        break

    persons = set()
    preferences = []

    for line in fileinput.input():
        line = list(map(int, line.split(" ")))
        persons.add(line[0])
        preferences.append(line)

    graph = [[0 for j in range(choices)] for i in range(stdnt_cnt)]
    for line in preferences:
        graph[line[0] - 1][line[0] - 1] = 1

    result = set(find_max_matching(graph, choices, stdnt_cnt))
    result.remove(-1)
    result.remove(0)
    print(len(result))
    print(result)
