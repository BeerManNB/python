from copy import copy



# стрит
def straight(b):
    name = 'straight'
    a = copy(b)
    if {1, 2, 3, 4, 5}.issubset(a):
        return 15
    elif {2, 3, 4, 5, 6}.issubset(a):
        return 20
    else:
        return 0


# тройка
def trips(b):
    a = copy(b)
    for i in a:
        if a.count(i) >= 3:
            return i * 3
    return 0


# пара (ищем старшую пару)
def pair(b):
    a = copy(b)
    a.sort(reverse=True)
    for i in a:
        if a.count(i) >= 2:
            return i * 2
    return 0


# фулл хаус (тройка+пары должны быть разных значений)
def full_house(b):
    a = copy(b)
    if trips(a) != 0:
        tr = trips(a) / 3
        for i in range(3):
            a.remove(tr)
        if (a[0] == a[1]) and (a[0] != tr):
            return int(tr * 3 + a[0] * 2)
        else:
            return 0
    else:
        return 0


# две пары (две разные пары)
def two_pairs(b):
    a = copy(b)
    if pair(a) != 0:
        pair1 = pair(a) / 2
        for i in range(2):
            a.remove(pair1)
        pair2 = pair(a) / 2
        if pair2 != 0 and pair1 != pair2:
            return int(pair2 * 2 + pair1 * 2)
        else:
            return 0
    else:
        return 0
