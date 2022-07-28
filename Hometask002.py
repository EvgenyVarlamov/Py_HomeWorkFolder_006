# Самая далекая орбита
from math import pi


def find_farthest_orbit(list_of_orbits):
    lst=[round(pi*list_of_orbits[i][0]*list_of_orbits[i][1], 2) if list_of_orbits[i][0]!=list_of_orbits[i][1] else 0 for i in range(len(list_of_orbits))]
    return list_of_orbits[lst.index(max(lst))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
