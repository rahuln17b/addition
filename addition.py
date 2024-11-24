def aorb(a, b, possible):
    proba = len(a)/len(possible)

    probb = len(b)/len(possible)

    inter = a.intersection(b)

    probinter = len(inter)/len(possible)

    return (proba + probb - probinter)

a = {2, 4, 6}
b = {3, 4, 5, 6}
possible = {1, 2, 3, 4, 5, 6} 

print(aorb(a, b, possible))