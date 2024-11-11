from clothing import Clothing

def permutate(lst, amount):
    pointers = []
    permutations = []

    for i in range(amount):
        pointers.append(i)

    permutation = []
    for point in pointers:
        permutation.append(lst[point])

    permutations.append(permutation)

    while (pointers[0] < (len(lst) - (amount-1)-1)):
        for i in range(amount-1, -1, -1):
            if (pointers[i] < (len(lst) - (amount-i-1)-1)):
                pointers[i] += 1


                for k in range(i+1, amount, 1):
                    pointers[k] = (pointers[k-1])+1

                permutation = []
                for point in pointers:
                    permutation.append(lst[point])

                permutations.append(permutation)

                break


    return permutations

def calcTemp(cloths: list, typeof = "all") -> float:
    temp = 0

    if typeof == "all":
        for i in cloths:
            temp += i.points
    else:
        for i in cloths:
            if i.type == typeof:
                temp += i.points

    return temp
    

def fit(tops, bottoms, extra, temp) -> list:
    permsTop = []
    permsBot = []
    permsExtra = [[]]
    totals = []

    for i in range(len(tops)):
        permsTop += permutate(tops, i+1)

    for i in range(len(bottoms)):
        permsBot += permutate(bottoms, i+1)

    for i in range(len(extra)):
        permsExtra += permutate(extra, i+1)

    
    for top in permsTop:
        for bot in permsBot:
            for ex in permsExtra:
                totals.append(top + bot + ex)

    del permsTop, permsBot, permsExtra

    minDif = -1

    for perm in totals:
        if minDif == -1 or minDif > abs(calcTemp(perm, "tops") - calcTemp(perm, "bottoms")):
            minDif = abs(calcTemp(perm, "tops") - calcTemp(perm, "bottoms"))

    balanced = []
    for perm in totals:
        total = ""
        for x in perm:
            total += str(x) + " -> "
        if minDif == abs(calcTemp(perm, "tops") - calcTemp(perm, "bottoms")):
            balanced.append(perm)



    minDistance = -1

    for perm in balanced:
        if minDistance == -1 or minDistance > abs(temp - calcTemp(perm)):
            minDistance = abs(temp - calcTemp(perm))

    bestOptions = []
    for perm in balanced:
        total = ""
        for x in perm:
            total += str(x) + " -> "
        if minDistance == abs(temp - calcTemp(perm)):
            bestOptions.append(perm)

    del balanced

    return bestOptions