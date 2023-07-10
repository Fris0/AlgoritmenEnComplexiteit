"""
Auteur: Mark Jansen
Studentnummer: 13385569
Gemaakt op: 17-11-2022

Samenvatting:
Een implementatie van het greedy algoritme Kruskal. Met het Kruskal algoritme
wordt het minimum cost path berekend.

Gebruik:
- Run de de python code met python3 <pythonfile> < <inputfile>
- Het resultaat wordt met std:out weergegeven.
"""

import fileinput


EMPTY = 0  # Geeft aan of de nodes nog niet in een forest zitten.
CYCLE = 1  # Geeft aan dat het pad een cycle vormt.
SOURCE_IN = 2  # Geeft aan dat de source node in een forest zit.
DEST_IN = 3  # Geeft aan dat de dest node in een forest zit.
BOTH_IN = 4  # Geeft aan dat de source en dest node in een forest zit.
NOT_IN = 5  # Geeft aan dat beide nodes niet in een forest zitten.

graph_info = 0
forests = []


def inlist(forests, node_source, node_dest):
    """
    Kijk of een of beide nodes van een pad al in een forest zit en maak
    op basis van die gegevens een nieuwe forest aan of voeg bestaande samen.

    node_source: Een integer die aangeeft vanaf welke locatie hij/zij reist.
    node_dest: Een integer die aangeeft naar welke node hij/zei reist.

    Output: Kijk naar de globale variabelen.
    """
    if len(forests) < 0:
        forests.append([node_source, node_dest])
        return EMPTY
    else:
        source, dest = 0, 0
        source_list, dest_list = [], []
        for forest in forests:
            if node_source in forest and node_dest in forest:
                return CYCLE
            if node_source in forest:
                source = SOURCE_IN
                source_list = forest
            if node_dest in forest:
                dest = DEST_IN
                dest_list = forest
            if source == SOURCE_IN and dest == DEST_IN:
                forests.remove(source_list)
                forests.remove(dest_list)
                forests.append(source_list + dest_list)
                return BOTH_IN

        if source == SOURCE_IN:
            forests.remove(source_list)
            source_list.append(node_dest)
            forests.append(source_list)
            return SOURCE_IN
        elif dest == DEST_IN:
            forests.remove(dest_list)
            dest_list.append(node_source)
            forests.append(dest_list)
            return DEST_IN
        else:
            forests.append([node_source, node_dest])
            return NOT_IN


def solve_problem(graph):
    """
    Lees de paden uit de sorted array, geef het door aan de inlist func
    en voeg de cost aan de total_cost toe op basis van de return value.

    graph: Een array gesorteerd op path cost.

    Output: None.
    Side-effects: Als er één forest is aan het eind van
                  het doorlopen van alle paden, dan
                  total cost naar STD:OUT en anders
                  geen route mogelijk.
    """
    total_cost = 0
    for path in graph:
        bool = inlist(forests, path[0], path[1])
        if bool == CYCLE:
            continue
        elif bool == EMPTY:
            total_cost += path[2]
        elif bool == DEST_IN or bool == SOURCE_IN:
            total_cost += path[2]
        elif bool == BOTH_IN:
            total_cost += path[2]
        elif bool == NOT_IN:
            total_cost += path[2]
        else:
            continue
    if (len(forests) <= 1):
        print(total_cost)
    else:
        print("Geen route mogelijk")


if __name__ == "__main__":
    """
    Lees de lines van standard input en zet ze gesorteerd
    in een lijst op basis van path cost.
    """
    graph = []
    for line in fileinput.input():
        graph_info = list(map(int, line.split(" ")))
        fileinput.close()
        break

    for line in fileinput.input():
        node = list(map(int, line.split(" ")))
        graph.append(node)

    sorted_graph = []
    for j in range(len(graph)):
        for i in range(len(graph)):
            if j == graph[i][2]:
                sorted_graph.append(graph[i])
    solve_problem(sorted_graph)
