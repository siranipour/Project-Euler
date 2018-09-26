import numpy as np
import time
from itertools import permutations


t0 = time.time()

def genTriangle():
    result = []
    go = True
    i = 1
    while go:
        result.append(int(i*(i+1)/2))
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def genSquare():
    result = []
    go = True
    i = 1
    while go:
        result.append(i**2)
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def genPentagon():
    result = []
    go = True
    i = 1
    while go:
        result.append(int(i*(3*i-1)/2))
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def genHexagon():
    result = []
    go = True
    i = 1
    while go:
        result.append(int(i*(2*i-1)))
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def genHeptagon():
    result = []
    go = True
    i = 1
    while go:
        result.append(int(i*(5*i-3)/2))
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def genOctagon():
    result = []
    go = True
    i = 1
    while go:
        result.append(int(i*(3*i-2)))
        if len(str(result[-1])) > 4:
            go = False
        i += 1
    result = [x for x in result if len(str(x)) == 4]

    return result

def isLoop(A = [], B = [], C = [], D = [], E = [], F = []):
    A = np.array([[int(str(i)[:2]) for i in A],[int(str(i)[-2:]) for i in A]])
    B = np.array([[int(str(i)[:2]) for i in B],[int(str(i)[-2:]) for i in B]])
    C = np.array([[int(str(i)[:2]) for i in C],[int(str(i)[-2:]) for i in C]])
    D = np.array([[int(str(i)[:2]) for i in D],[int(str(i)[-2:]) for i in D]])
    E = np.array([[int(str(i)[:2]) for i in E],[int(str(i)[-2:]) for i in E]])
    F = np.array([[int(str(i)[:2]) for i in F],[int(str(i)[-2:]) for i in F]])

    failed = False

    while not failed:
        if not A.size:
            failed = True
            break
        else:
            B = np.array([[x, y] for [x, y] in B.T if x in A[1]]).T

        if not B.size:
            failed = True
            break
        else:
            C = np.array([[x, y] for [x, y] in C.T if x in B[1]]).T

        if not C.size:
            failed = True
            break
        else:
            D = np.array([[x, y] for [x, y] in D.T if x in C[1]]).T

        if not D.size:
            failed = True
            break
        else:
            E = np.array([[x, y] for [x, y] in E.T if x in D[1]]).T

        if not E.size:
            failed = True
            break
        else:
            F = np.array([[x, y] for [x, y] in F.T if x in E[1]]).T

        if not F.size:
            failed = True
            break
        else:
            A = np.array([[x, y] for [x, y] in A.T if x in F[1]]).T
        if A.size == 2 and B.size == 2 and C.size == 2 and D.size == 2 and E.size == 2 and F.size == 2:
            break

    if failed == True:
        return 0
    else:
                print("--START--")
                print(A.T)
                print(B.T)
                print(C.T)
                print(D.T)
                print(E.T)
                print(F.T)
                print("--END--")

A = genTriangle()
B = genSquare()
C = genPentagon()
D = genHexagon()
E = genHeptagon()
F = genOctagon()

perms = list(permutations('ABCDEF'))
for x in perms:
    isLoop(eval(x[0]),eval(x[1]),eval(x[2]),eval(x[3]),eval(x[4]),eval(x[5]))


t1 = time.time()

