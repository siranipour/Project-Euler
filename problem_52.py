mappings = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17, 8:19, 9:23, 0:29}

def primed_list(x):
    return list(map(lambda y: mappings[int(y)], str(x)))

def primed_product(x):
    product = 1
    for i in primed_list(x):
        product *= i

    return product

found = False

i = 1
while found == False:
    x = primed_product(i)
    if primed_product(2*i) == x and primed_product(3*i) == x and primed_product(4*i) == x and primed_product(5*i) == x and primed_product(6*i) == x:
        print(i)
        found = True
    i +=1
