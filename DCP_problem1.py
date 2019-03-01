def isSum(array, n):
    b = [n - i for i in array]
    a = set(b)
    for i in array:
        if i in a:
            return True
    return False

print(isSum([10, 15, 3, 7, 8, 12], 29))